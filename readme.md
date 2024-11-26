# GitHub Repository Chatbot

This is a Streamlit-based chatbot application that allows users to interact with GitHub repositories. The application reads data from a GitHub repository and allows you to ask questions about the repository content.

## Features
- Retrieve repository information from GitHub using a given repository URL.
- Query the contents of the repository through a chatbot interface.
- Uses DeepLake as the vector store for managing repository data.
- Integrates OpenAI API for answering user questions.

## Prerequisites
To run this project, ensure you have the following:
- Python 3.8 or higher
- GitHub token with repository access
- ActiveLoop token
- OpenAI API key

## Creating the Required Tokens
1. **GitHub Token**:
   - Go to [GitHub Settings](https://github.com/settings/tokens).
   - In the upper-right corner of any page on GitHub, click your profile photo, then click **Settings**.
   - In the left sidebar, click **Developer settings**.
   - In the left sidebar, under **Personal access tokens**, click **Fine-grained tokens**.
   - Click **Generate new token**.
   - Under **Token name**, enter a name for the token.
   - Under **Expiration**, select an expiration for the token. Infinite lifetimes are allowed but may be blocked by a maximum lifetime policy set by your organization or enterprise owner.
   - Optionally, under **Description**, add a note to describe the purpose of the token.
   - Under **Resource owner**, select a resource owner. The token will only be able to access resources owned by the selected resource owner.
   - Under **Repository access**, select which repositories you want the token to access. You should choose the minimal repository access that meets your needs. Tokens always include read-only access to all public repositories on GitHub.
   - If you selected **Only select repositories** in the previous step, under the **Selected repositories** dropdown, select the repositories that you want the token to access.
   - Under **Permissions**, select which permissions to grant the token. Choose the minimal permissions necessary for your needs.
   - Click **Generate token** and copy it for use in the application.

2. **ActiveLoop Token**:
   - Go to [ActiveLoop Login](https://app.activeloop.ai/).
   - Sign in or create an account.
   - Navigate to your profile settings and select **API Tokens**.
   - Click on **Generate New Token**.
   - Copy the generated token for use in the application.

3. **OpenAI API Key**:
   - Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys).
   - Sign in or create an account.
   - Click on **Create new secret key**.
   - Copy the API key for use in the application.

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your_username/your_repository_name.git
   cd your_repository_name
   ```

2. **Create a Virtual Environment and Activate It**
   ```sh
   python -m venv venv
   # Activate the virtual environment
   # For Windows
   venv\Scripts\activate
   # For Unix or MacOS
   source venv/bin/activate
   ```

3. **Install the Required Packages**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Application**
   ```sh
   streamlit run github_streamlit_chatbot.py
   ```

2. **Access the Chatbot**
   Open the local URL provided by Streamlit (usually http://localhost:8501) in your browser.

3. **Provide Tokens and Repository URL**
   - Enter your GitHub token, ActiveLoop token, and OpenAI API key in the sidebar.
   - Enter the GitHub repository URL you want to analyze.

4. **Chat with the Repository**
   - Once the repository is processed, you can ask questions about its contents in the chatbot interface.

## Environment Variables
The application requires the following tokens:
- **GitHub Token**: Access to the GitHub repository.
- **ActiveLoop Token**: Required for the DeepLake vector store.
- **OpenAI API Key**: Used to generate responses for user questions.

These tokens will be entered directly into the Streamlit sidebar during the application runtime.

## File Structure
- `github_streamlit_chatbot.py`: Main Python script to run the chatbot.
- `requirements.txt`: List of required Python packages.

## Requirements
The following libraries are used in the project:
- `streamlit`
- `nest-asyncio`
- `llama-index`
- `deeplake`

## Deployment
To deploy the application on GitHub:
1. **Commit Changes**
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Use Streamlit Sharing**
   You can use [Streamlit Sharing](https://streamlit.io/sharing) to deploy your app online.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Contact
For any questions or feedback, please reach out to the repository owner.

