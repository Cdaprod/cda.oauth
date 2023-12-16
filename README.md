# FastAPI OAuth Integration

This project demonstrates a FastAPI application with OAuth integration for Google and GitHub. It allows users to authenticate using their Google or GitHub accounts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- HTTPX (for HTTP client functionality)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/your-repo-name.git
   ```

2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```

3. Install the required packages:
   ```bash
   pip install fastapi uvicorn httpx
   ```

4. Create a `.env` file in the root directory of the project and fill in your OAuth credentials and redirect URIs as shown in the `.env` example above.

### Running the Application

1. Run the server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the application at `http://localhost:8000`.

3. To initiate the OAuth process, navigate to `/google/login` or `/github/login`.

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### Acknowledgments

- FastAPI Team
- Google OAuth
- GitHub OAuth


### Note on Security and .env File
- **Never commit your `.env` file to your repository.** It contains sensitive information like client IDs and secrets. Always ensure it's listed in your `.gitignore` file.
- This `README.md` provides basic instructions for getting started, running the application, and contributing. Modify it as needed for your specific project.

### Repository Structure
Make sure your repository includes the following:
- Python files for your FastAPI application (e.g., `main.py`, `google_auth.py`, `github_auth.py`).
- A `.env` file (locally) with your credentials.
- A `.gitignore` file that includes `.env`.