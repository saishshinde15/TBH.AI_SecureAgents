# example_usage_7.py
# Demonstrates assigning and conceptually using security_profile (Translation Example)

import os
# import logging # Removed logging
import re # Import regex for conceptual PII masking
from tbh_secure_agents import Agent, Task, Crew

# --- Configuration ---
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Removed logging
# logger = logging.getLogger(__name__) # Removed logging

# --- Define Agents with Specific Security Profiles ---
print("--- Initializing Agents with Security Profiles ---")
try:
    # Agent for general translation tasks
    general_translator = Agent(
        role='Multilingual Translator',
        goal='Translate text accurately between languages.',
        backstory='A standard translation agent.',
        security_profile='translator_general'
        # CONCEPTUAL IMPLEMENTATION:
        # - _is_output_secure might perform basic harmful content checks.
    )

    # Agent designed to avoid leaking PII during translation
    pii_safe_translator = Agent(
        role='PII-Aware Multilingual Translator',
        goal='Translate text accurately between languages while masking potential PII.',
        backstory='A translation agent specifically trained and configured to handle potentially sensitive text.',
        security_profile='translator_no_pii' # Profile implying stricter output filtering
        # CONCEPTUAL IMPLEMENTATION:
        # - _is_output_secure would actively scan for and mask PII patterns (like emails, phone numbers).
    )

except Exception as e:
    print(f"\nError initializing agents: {e}. Make sure GOOGLE_API_KEY is set.") # Replaced logger.error
    exit()

# --- Define Task with Potentially Sensitive Data ---
print("\n--- Defining Task ---")

text_to_translate = "Please contact support@example.com for assistance."
target_language = "Spanish"

translation_task_details = f"Translate the following text to {target_language}: '{text_to_translate}'"

# Create two separate tasks, one for each agent profile, to see the conceptual difference
task_general = Task(
    description=translation_task_details,
    expected_output=f'The text translated into {target_language}.',
    agent=general_translator
)

task_pii_safe = Task(
    description=translation_task_details,
    expected_output=f'The text translated into {target_language}, with PII masked.',
    agent=pii_safe_translator
)

# --- Assemble and Run Crews ---
# We run two separate crews here to isolate the agent behavior based on profile.
print("\n--- Creating and Running General Translation Crew ---")
try:
    crew_general = Crew(agents=[general_translator], tasks=[task_general])
    result_general = crew_general.kickoff()
    print("General Translation Crew Finished.") # Replaced logger.info
except Exception as e:
    print(f"Error in General Translation Crew: {e}") # Replaced logger.error
    result_general = "# Error during general translation"

print("\n--- Creating and Running PII-Safe Translation Crew ---")
try:
    crew_pii_safe = Crew(agents=[pii_safe_translator], tasks=[task_pii_safe])
    result_pii_safe = crew_pii_safe.kickoff()
    print("PII-Safe Translation Crew Finished.") # Replaced logger.info
except Exception as e:
    print(f"Error in PII-Safe Translation Crew: {e}") # Replaced logger.error
    result_pii_safe = "# Error during PII-safe translation"


# --- Display Results ---
# NOTE: Since the actual PII masking logic isn't implemented in _is_output_secure,
# both agents will likely return the same raw translation from the LLM.
# This example highlights where the profile *would* conceptually trigger different behavior.

print("\n" + "="*20 + " Task Result (General Translator) " + "="*20)
print(f"Profile: {general_translator.security_profile}")
print(result_general if result_general else "# Task Error/No Result")
print("="*70)

print("\n" + "="*20 + " Task Result (PII-Safe Translator) " + "="*20)
print(f"Profile: {pii_safe_translator.security_profile}")
print(result_pii_safe if result_pii_safe else "# Task Error/No Result")
print("="*70)


print("\n--- Example Script 7 Finished ---") # Replaced logger.info
print("WARNING: This example demonstrates PROFILE ASSIGNMENT CONCEPT ONLY.") # Replaced logger.warning
print("WARNING: Actual PII masking based on profile requires implementation in Agent's _is_output_secure method.") # Replaced logger.warning
