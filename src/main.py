#!/usr/bin/env python
import sys
from dotenv import load_dotenv, dotenv_values
import os

# Load values directly from .env file
config = dotenv_values(".env")
print("Values from .env file:")
print(f"OPENAI_API_KEY from file: {config.get('OPENAI_API_KEY')[:10]}...")
print(f"AGENTOPS_API_KEY from file: {config.get('AGENTOPS_API_KEY')}")

# Force set the environment variables
os.environ['OPENAI_API_KEY'] = config.get('OPENAI_API_KEY')
os.environ['AGENTOPS_API_KEY'] = config.get('AGENTOPS_API_KEY')

# Verify the environment variables
print("\nEnvironment variables after setting:")
print(f"OPENAI_API_KEY in environment: {os.environ.get('OPENAI_API_KEY')[:10]}...")
print(f"AGENTOPS_API_KEY in environment: {os.environ.get('AGENTOPS_API_KEY')}")

from crew import App1Crew
import agentops

agentops.init()


def run():
    """
    Run the crew.
    """
    
    cv_path = os.path.expanduser("~/data/cv.txt")
    
    if not os.path.exists(cv_path):
        raise FileNotFoundError(f"CV file not found at: {cv_path}")
    
    print(f"Using CV file at: {cv_path}")
    
    crew_instance = App1Crew()
    
    crew_instance.tasks_config['read_profile']['description'] = \
        crew_instance.tasks_config['read_profile']['description'].replace(
            '/Users/rcisneros/data/cv.txt', 
            cv_path
        )
    
    crew_instance.crew().kickoff(inputs={'topic': 'AI LLMs'})


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        App1Crew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        App1Crew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        App1Crew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


if __name__ == '__main__':
    run()