# Source the .env file to set the environment variables
source .env

# Set the GCP project from the environment variable
gcloud config set project $PROJECT_ID

# Enable required Google Cloud services
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  aiplatform.googleapis.com \
  compute.googleapis.com

# Create the working directory and move into it (if not already there)
# Note: Assuming you are running this from the repository root
# cd && mkdir -p Google-GenAI-APAC && cd Google-GenAI-APAC
# cloudshell open-workspace ~/Google-GenAI-APAC

# Set up the Python environment
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Create the service account using values from .env
gcloud iam service-accounts create ${SA_NAME} \
    --display-name="Service Account for lab 2"
    
# Grant the "Vertex AI User" role to your service account
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT" \
  --role="roles/aiplatform.user"

# Run the deployment command using parameters from .env
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
