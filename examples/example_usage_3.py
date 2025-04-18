# example_usage_3.py
# Demonstrates a third use case: Basic Flask App Generation & README

import os
from tbh_secure_agents import Agent, Task, Crew

# --- !!! SECURITY WARNING !!! ---
# The following line includes the API key directly in the code.
# This is INSECURE and ONLY for temporary testing due to environment variable issues.
# DO NOT commit this code or use this method in production.
# Use environment variables (`GOOGLE_API_KEY`) for secure key management.
# --- !!! /SECURITY WARNING !!! ---
TESTING_API_KEY = "" # Key provided by user

print("--- Initializing Agents (Use Case 3) ---")
# Define Agents for the new use case
try:
    flask_dev = Agent(
        role='Python Web Developer',
        goal='Generate Python code for a simple Flask web application.',
        backstory='Experienced in creating basic web server applications using Flask.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='web_code_gen', # Example profile
        api_key=TESTING_API_KEY
    )

    readme_writer = Agent(
        role='Technical Writer for Developers',
        goal='Write clear setup and usage instructions for Python applications.',
        backstory='Specializes in creating README files for software projects.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='readme_standard', # Example profile
        api_key=TESTING_API_KEY
    )
except Exception as e:
    print(f"\nError initializing agents: {e}")
    exit()

print("\n--- Defining Tasks (Use Case 3) ---")
# Define Tasks for the new use case
task_flask_code = Task(
    description='Generate the complete Python code for a minimal Flask application in a single file named `app.py`. It should have one route ("/") that returns the text "Hello, Secure World!". Include necessary imports and the standard `if __name__ == "__main__":` block to run the development server.',
    expected_output='Complete Python code for the Flask app.',
    agent=flask_dev
)

task_readme = Task(
    description='Based *only* on the provided Flask application code, write the content for a `README.md` file. The README should explain: 1. What the application does. 2. How to set up a virtual environment and install Flask (`pip install Flask`). 3. How to run the application (`python app.py`). 4. What output to expect in the terminal and how to access the app in a web browser.',
    expected_output='Markdown content suitable for a README file.',
    agent=readme_writer
    # Context (the Flask code) will be passed from task_flask_code
)

print("\n--- Creating Crew (Use Case 3) ---")
# Create Crew
flask_crew = Crew(
    agents=[flask_dev, readme_writer],
    tasks=[task_flask_code, task_readme],
    process='sequential'
)

print("\n--- Running Crew (Use Case 3) ---")
# Run the Crew
try:
    final_readme_content = flask_crew.kickoff()

    print("\n--- Crew Execution Finished (Use Case 3) ---")

    generated_flask_code = task_flask_code.result # Get the code from the first task

    print("\nGenerated Flask App Code (`app.py`):")
    print("------------------------------------")
    print(generated_flask_code if generated_flask_code else "# Error generating Flask code.")
    print("------------------------------------")

    print("\nGenerated README.md Content:")
    print("----------------------------")
    print(final_readme_content if final_readme_content else "# Error generating README content.")
    print("----------------------------")

except Exception as e:
    print(f"\nAn error occurred during crew execution: {e}")

print("\n--- Example Script 3 Finished ---")
