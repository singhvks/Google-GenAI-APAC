# Food Explorer Agent

Explore the world of food with an intelligent AI agent powered by Google ADK.

## Features
- **Intelligent Research**: Automatically searches Wikipedia for city-specific food and geography information.
- **Friendly Interface**: Provides concise and engaging responses to user queries.
- **Enterprise Ready**: Designed for deployment on Google Cloud Run with built-in logging and monitoring.

## Getting Started

### Prerequisites
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Google Cloud SDK (`gcloud`)

### Setup
1.  **Clone the repository**:
    ```bash
    git clone [your-repo-url]
    cd Google-GenAI-APAC
    ```

2.  **Configure environment variables**:
    Update the `.env` file with your project details:
    ```bash
    PROJECT_ID=your-project-id
    PROJECT_NUMBER=your-project-number
    SA_NAME=lab2-cr-service
    SERVICE_ACCOUNT=lab2-cr-service@your-project-id.iam.gserviceaccount.com
    MODEL="gemini-2.5-flash"
    ```

3.  **Install dependencies**:
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt
    ```

## Usage
To run the agent locally (using ADK server):
```bash
uvx --from google-adk==1.14.0 adk run
```

## Testing and Evaluation
### Running Tests
```bash
pytest tests/test_agent.py
```

### Running Evaluation
```bash
adk eval --config eval_config.yaml
```

## Deployment
To deploy the agent to Google Cloud Run, follow the steps in [Deployment Steps.md](Deployment%20Steps.md). The main command is:
```bash
source .env
uvx --from google-adk==1.14.0 \
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=europe-west1 \
  --service_name=zoo-tour-guide \
  --with_ui \
  . \
  -- \
  --labels=dev-tutorial=codelab-adk \
  --service-account=$SERVICE_ACCOUNT
```

## Documentation
- [System Design Document](./System%20Design.md)
- [Deployment Steps](./Deployment%20Steps.md)