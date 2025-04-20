# example_usage_6.py
# Demonstrates assigning and conceptually using security_profile (Medium Example)

import os
# import logging # Removed logging
from tbh_secure_agents import Agent, Task, Crew

# --- Configuration ---
# Ensure the GOOGLE_API_KEY environment variable is set before running.
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Removed logging
# logger = logging.getLogger(__name__) # Removed logging

# --- Define Agents with Different Security Profiles ---
print("--- Initializing Agents with Security Profiles ---")
try:
    # This agent is intended for summarizing public info, potentially less strict checks.
    safe_summarizer = Agent(
        role='News Summarizer',
        goal='Summarize publicly available news articles concisely.',
        backstory='An efficient agent focused on extracting key points from text.',
        security_profile='summarizer_standard' # Profile for standard summarization tasks
        # CONCEPTUAL IMPLEMENTATION:
        # - _is_output_secure might check for basic harmful content.
        # - _is_prompt_secure might have moderate restrictions.
    )

    # This agent might be intended to access internal/sensitive data, requiring stricter checks.
    restricted_researcher = Agent(
        role='Internal Knowledge Researcher',
        goal='Retrieve specific information from internal company knowledge bases.',
        backstory='An agent designed for accessing and processing proprietary information securely.',
        security_profile='internal_research_strict' # Profile implying stricter controls
        # CONCEPTUAL IMPLEMENTATION:
        # - _is_prompt_secure might disallow prompts asking about non-internal topics or trying to exfiltrate data.
        # - _is_output_secure might strictly scan for any accidental leakage of sensitive keywords or PII.
        # - Task._pre_execution_secure might check if this agent is assigned only to tasks tagged as 'internal_data'.
    )

except Exception as e:
    print(f"\nError initializing agents: {e}. Make sure GOOGLE_API_KEY is set.") # Replaced logger.error
    exit()

# --- Define Tasks ---
# Note: The tasks themselves don't automatically interact with the profile yet.
# The profile's effect would come from implemented logic in the security methods.
print("\n--- Defining Tasks ---")

task1_summarize = Task(
    description="Summarize the following hypothetical news excerpt about AI advancements: 'Recent breakthroughs in AI have led to models capable of complex reasoning. Concerns about ethical implications and job displacement are growing.'",
    expected_output='A concise one-sentence summary.',
    agent=safe_summarizer # Assigning the agent with the 'summarizer_standard' profile
)

task2_internal_lookup = Task(
    description="Hypothetically retrieve the Q3 sales target for 'Project Phoenix' from the internal database.",
    expected_output='The Q3 sales target figure or "Data not found".',
    agent=restricted_researcher # Assigning the agent with the 'internal_research_strict' profile
    # CONCEPTUAL: If Crew had validation, it might check if 'internal_research_strict'
    # profile is allowed for tasks involving hypothetical database lookups.
)

# --- Assemble and Run the Crew ---
# This example runs them sequentially just to show both agents.
# In a real scenario, they might operate independently or in different crews.
print("\n--- Creating Crew ---")
try:
    demonstration_crew = Crew(
        agents=[safe_summarizer, restricted_researcher],
        tasks=[task1_summarize, task2_internal_lookup],
        process='sequential'
    )

    print("\n--- Running Crew ---")
    final_result = demonstration_crew.kickoff() # Result of the last task

    print("\n--- Crew Execution Finished ---")

    # Print results from both tasks
    print("\n" + "="*20 + " Task 1 (Summarizer) Result " + "="*20)
    print(task1_summarize.result if task1_summarize.result else "# Task 1 Error/No Result")
    print("="*61)

    print("\n" + "="*20 + " Task 2 (Researcher) Result " + "="*20)
    print(task2_internal_lookup.result if task2_internal_lookup.result else "# Task 2 Error/No Result")
    print("="*61)


except ValueError as ve:
    print(f"Crew initialization error: {ve}") # Replaced logger.error
except Exception as e:
    print(f"\nAn error occurred during crew execution: {e}") # Replaced logger.error

print("\n--- Example Script 6 Finished ---")
print("WARNING: Security profile enforcement currently requires manual implementation in Agent/Task security methods.") # Replaced logger.warning
