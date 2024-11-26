import getpass
import os
import textwrap
import re
import nest_asyncio
import streamlit as st
from llama_index.readers.github import GithubRepositoryReader, GithubClient
from llama_index.core import download_loader
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.deeplake import DeepLakeVectorStore
from llama_index.core.storage.storage_context import StorageContext

# Apply nest_asyncio to avoid event loop errors
nest_asyncio.apply()

# Constants
DATASET_PATH = "hub://rajp20023/repository_vector_store"


def parse_github_url(url):
    pattern = r"https://github\.com/([^/]+)/([^/]+)"
    match = re.match(pattern, url)
    return match.groups() if match else (None, None)


def validate_owner_repo(owner, repo):
    return bool(owner) and bool(repo)


def initialize_github_client():
    github_token = os.getenv("GITHUB_TOKEN")
    return GithubClient(github_token)


def main():
    st.title("GitHub Repository Chatbot")
    st.sidebar.header("API Tokens")

    # Prompt user for required tokens using Streamlit sidebar
    github_token = st.sidebar.text_input(
        "Enter your GitHub token:", type="password"
    )
    activeloop_token = st.sidebar.text_input(
        "Enter your ActiveLoop token:", type="password"
    )
    openai_api_key = st.sidebar.text_input(
        "Enter your OpenAI API key:", type="password"
    )

    if github_token and activeloop_token and openai_api_key:
        # Set environment variables
        os.environ["GITHUB_TOKEN"] = github_token
        os.environ["ACTIVELOOP_TOKEN"] = activeloop_token
        os.environ["OPENAI_API_KEY"] = openai_api_key

        # Check for required environment variables
        if not os.getenv("OPENAI_API_KEY"):
            st.error("OpenAI API key not found in environment variables")
            return

        if not os.getenv("GITHUB_TOKEN"):
            st.error("GitHub token not found in environment variables")
            return

        if not os.getenv("ACTIVELOOP_TOKEN"):
            st.error("Activeloop token not found in environment variables")
            return

        # Initialize GitHub client and loader
        github_client = initialize_github_client()
        download_loader("GithubRepositoryReader")

        github_url = st.text_input("Please enter the GitHub repository URL:")

        if github_url:
            owner, repo = parse_github_url(github_url)

            if validate_owner_repo(owner, repo):
                if "docs" not in st.session_state:
                    with st.spinner(
                        f"Loading {repo} repository by {owner}..."
                    ):
                        loader = GithubRepositoryReader(
                            github_client,
                            owner=owner,
                            repo=repo,
                            filter_file_extensions=(
                                [".py", ".js", ".ts", ".md"],
                                GithubRepositoryReader.FilterType.INCLUDE,
                            ),
                            verbose=False,
                            concurrent_requests=5,
                        )
                        docs = loader.load_data(branch="main")
                        st.session_state["docs"] = docs
                        st.success("Documents uploaded successfully!")
                        st.write("Documents uploaded:")
                        for doc in docs:
                            st.write(doc.metadata)

                # Create vector store and upload data if not already done
                if "query_engine" not in st.session_state:
                    st.write("Uploading to vector store...")
                    vector_store = DeepLakeVectorStore(
                        dataset_path=DATASET_PATH,
                        overwrite=True,
                        runtime={"tensor_db": True},
                    )

                    storage_context = StorageContext.from_defaults(
                        vector_store=vector_store
                    )
                    index = VectorStoreIndex.from_documents(
                        st.session_state["docs"],
                        storage_context=storage_context,
                    )
                    st.session_state["query_engine"] = index.as_query_engine()

                # Interactive query session
                st.write("# Chat with the Repository")
                user_question = st.text_input(
                    "Please enter your question (or type 'exit' to quit):"
                )
                if user_question:
                    if user_question.lower() == "exit":
                        st.write("Exiting, thanks for chatting!")
                    else:
                        st.write(f"Your question: {user_question}")
                        st.write("=" * 50)
                        answer = st.session_state["query_engine"].query(
                            user_question
                        )
                        st.write(
                            f"Answer: {textwrap.fill(str(answer), 100)} \n"
                        )
            else:
                st.error("Invalid GitHub URL. Please try again.")


if __name__ == "__main__":
    main()
