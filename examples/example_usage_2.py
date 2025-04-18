# example_usage_2.py
# Demonstrates another use case: Story Concept & Marketing Blurb

import os
from tbh_secure_agents import Agent, Task, Crew

# --- !!! SECURITY WARNING !!! ---
# The following line includes the API key directly in the code.
# This is INSECURE and ONLY for temporary testing due to environment variable issues.
# DO NOT commit this code or use this method in production.
# Use environment variables (`GOOGLE_API_KEY`) for secure key management.
# --- !!! /SECURITY WARNING !!! ---
TESTING_API_KEY = "" # Key provided by user

print("--- Initializing Agents (Use Case 2) ---")
# Define Agents for the new use case
try:
    story_writer = Agent(
        role='Creative Story Writer',
        goal='Generate a unique and compelling short story concept about a time-traveling librarian.',
        backstory='An imaginative author specializing in science fiction and fantasy.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='creative_standard', # Example profile
        api_key=TESTING_API_KEY
    )

    marketer = Agent(
        role='Marketing Specialist',
        goal='Write a catchy promotional blurb for a new story concept.',
        backstory='Expert in crafting short, engaging descriptions to attract readers.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='marketing_safe', # Example profile
        api_key=TESTING_API_KEY
    )
except Exception as e:
    print(f"\nError initializing agents: {e}")
    exit()

print("\n--- Defining Tasks (Use Case 2) ---")
# Define Tasks for the new use case
task_concept = Task(
    description='Create a short story concept (1 paragraph) featuring a librarian who discovers a hidden time-travel device within an ancient book.',
    expected_output='A paragraph outlining the core story idea, main character, and conflict.',
    agent=story_writer
)

task_blurb = Task(
    description='Based *only* on the provided story concept, write a short (2-3 sentences) promotional blurb designed to intrigue potential readers.',
    expected_output='A catchy marketing blurb for the story concept.',
    agent=marketer
    # Context (the story concept) will be passed from task_concept
)

print("\n--- Creating Crew (Use Case 2) ---")
# Create Crew
story_crew = Crew(
    agents=[story_writer, marketer],
    tasks=[task_concept, task_blurb],
    process='sequential'
)

print("\n--- Running Crew (Use Case 2) ---")
# Run the Crew
try:
    final_blurb = story_crew.kickoff()

    print("\n--- Crew Execution Finished (Use Case 2) ---")
    print("\nFinal Result (Marketing Blurb):")
    print("---------------------------------")
    print(final_blurb)
    print("---------------------------------")

    # You might also want to access the intermediate result (the concept) if needed
    # print("\nIntermediate Result (Story Concept):")
    # print(task_concept.result) # Accessing the result stored in the task object

except Exception as e:
    print(f"\nAn error occurred during crew execution: {e}")

print("\n--- Example Script 2 Finished ---")
