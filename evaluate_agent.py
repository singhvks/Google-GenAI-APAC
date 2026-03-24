import os
import logging
from dotenv import load_dotenv
from agent import root_agent
from google.adk import evaluate

# Load environment variables
load_dotenv()

def run_evaluation():
    """Runs the agent evaluation using the configuration file."""
    logging.basicConfig(level=logging.INFO)
    
    # Ensure the output directory exists
    if not os.path.exists("./eval_results"):
        os.makedirs("./eval_results")

    print("Starting Agent Evaluation...")
    
    # Run evaluation
    # Note: In a real environment, you would use 'adk eval' CLI or this programmatic interface
    # results = evaluate(
    #     agent=root_agent,
    #     config_path="eval_config.yaml"
    # )
    
    # print(f"Evaluation complete. Results saved to ./eval_results")
    # return results
    
    print("Evaluation script prepared. Use 'adk eval' command or call this script to run.")

if __name__ == "__main__":
    run_evaluation()
