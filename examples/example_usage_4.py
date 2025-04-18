# example_usage_4.py
# Demonstrates a fourth use case: Information Extraction & Reporting

import os
from tbh_secure_agents import Agent, Task, Crew

# --- !!! SECURITY WARNING !!! ---
# The following line includes the API key directly in the code.
# This is INSECURE and ONLY for temporary testing due to environment variable issues.
# DO NOT commit this code or use this method in production.
# Use environment variables (`GOOGLE_API_KEY`) for secure key management.
# --- !!! /SECURITY WARNING !!! ---
TESTING_API_KEY = "" # Key provided by user

# --- Input Data ---
source_text = """
Dr. Evelyn Reed, a renowned astrophysicist based in Geneva, presented her groundbreaking research
on dark matter detection using novel sensor arrays deployed via high-altitude balloons over Antarctica.
Her work, funded by the Global Science Foundation, suggests that previously undetected particles
might interact weakly with standard matter under specific cryogenic conditions. The project,
codenamed 'Cosmic Whisper', aims to map these interactions over the next five years.
"""
# --- /Input Data ---


print("--- Initializing Agents (Use Case 4) ---")
# Define Agents for the new use case
try:
    extractor = Agent(
        role='Data Analyst specializing in Text Analysis',
        goal='Extract key named entities (people, organizations, locations, projects, concepts) from provided text.',
        backstory='Expert in identifying structured information within unstructured text.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='data_extraction_strict', # Example profile
        api_key=TESTING_API_KEY
    )

    reporter = Agent(
        role='Report Generator',
        goal='Synthesize extracted information into a clear, concise bullet-point summary.',
        backstory='Skilled at summarizing key findings for quick review.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='reporting_concise', # Example profile
        api_key=TESTING_API_KEY
    )
except Exception as e:
    print(f"\nError initializing agents: {e}")
    exit()

print("\n--- Defining Tasks (Use Case 4) ---")
# Define Tasks for the new use case
task_extract = Task(
    description=f'From the following text, identify and list the key named entities (People, Organizations, Locations, Project Names, Key Concepts). Text:\n\n{source_text}',
    expected_output='A list or structured representation of the extracted entities.',
    agent=extractor
)

task_report = Task(
    description='Based *only* on the provided list of extracted entities, generate a short bullet-point report summarizing the key information.',
    expected_output='A concise summary in bullet points.',
    agent=reporter
    # Context (extracted entities) will be passed from task_extract
)

print("\n--- Creating Crew (Use Case 4) ---")
# Create Crew
analysis_crew = Crew(
    agents=[extractor, reporter],
    tasks=[task_extract, task_report],
    process='sequential'
)

print("\n--- Running Crew (Use Case 4) ---")
# Run the Crew
try:
    final_report = analysis_crew.kickoff()

    print("\n--- Crew Execution Finished (Use Case 4) ---")

    extracted_entities = task_extract.result # Get the entities from the first task

    print("\nExtracted Entities:")
    print("---------------------")
    print(extracted_entities if extracted_entities else "# Error extracting entities.")
    print("---------------------")

    print("\nGenerated Summary Report:")
    print("-------------------------")
    print(final_report if final_report else "# Error generating report.")
    print("-------------------------")

except Exception as e:
    print(f"\nAn error occurred during crew execution: {e}")

print("\n--- Example Script 4 Finished ---")
