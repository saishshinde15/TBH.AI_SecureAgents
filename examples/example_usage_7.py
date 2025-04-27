# example_usage_7.py
# Demonstrates assigning and conceptually using security_profile (Translation Example)

import os
# import logging # Removed logging
import re # Import regex for conceptual PII masking
from tbh_secure_agents import Expert, Operation, Squad

# --- Configuration ---
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Removed logging
# logger = logging.getLogger(__name__) # Removed logging

# --- Define Experts with Specific Security Profiles ---
print("--- Initializing Experts with Security Profiles ---")
try:
    # Expert for general translation tasks
    general_translator = Expert(
        specialty='Multilingual Translator',
        objective='Translate text accurately between languages.',
        background='A standard translation expert.',
        security_profile='translator_general'
        # CONCEPTUAL IMPLEMENTATION:
        # - _is_output_secure might perform basic harmful content checks.
    )

    # Expert designed to avoid leaking PII during translation
    pii_safe_translator = Expert(
        specialty='PII-Aware Multilingual Translator',
        objective='Translate text accurately between languages while masking potential PII.',
        background='A translation expert specifically trained and configured to handle potentially sensitive text.',
        security_profile='translator_no_pii' # Profile implying stricter output filtering
        # CONCEPTUAL IMPLEMENTATION:
        # - _is_output_secure would actively scan for and mask PII patterns (like emails, phone numbers).
    )

except Exception as e:
    print(f"\nError initializing experts: {e}. Make sure GOOGLE_API_KEY is set.") # Replaced logger.error
    exit()

# --- Define Operation with Potentially Sensitive Data ---
print("\n--- Defining Operation ---")

text_to_translate = "Please contact support@example.com for assistance."
target_language = "Spanish"

translation_task_details = f"Translate the following text to {target_language}: '{text_to_translate}'"

# Create two separate operations, one for each expert profile, to see the conceptual difference
operation_general = Operation(
    instructions=translation_task_details,
    output_format=f'The text translated into {target_language}.',
    expert=general_translator
)

operation_pii_safe = Operation(
    instructions=translation_task_details,
    output_format=f'The text translated into {target_language}, with PII masked.',
    expert=pii_safe_translator
)

# --- Assemble and Run Squads ---
# We run two separate squads here to isolate the expert behavior based on profile.
print("\n--- Creating and Running General Translation Squad ---")
try:
    squad_general = Squad(experts=[general_translator], operations=[operation_general])
    result_general = squad_general.deploy()
    print("General Translation Squad Finished.") # Replaced logger.info
except Exception as e:
    print(f"Error in General Translation Squad: {e}") # Replaced logger.error
    result_general = "# Error during general translation"

print("\n--- Creating and Running PII-Safe Translation Squad ---")
try:
    squad_pii_safe = Squad(experts=[pii_safe_translator], operations=[operation_pii_safe])
    result_pii_safe = squad_pii_safe.deploy()
    print("PII-Safe Translation Squad Finished.") # Replaced logger.info
except Exception as e:
    print(f"Error in PII-Safe Translation Squad: {e}") # Replaced logger.error
    result_pii_safe = "# Error during PII-safe translation"


# --- Display Results ---
# NOTE: Since the actual PII masking logic isn't implemented in _is_output_secure,
# both experts will likely return the same raw translation from the LLM.
# This example highlights where the profile *would* conceptually trigger different behavior.

print("\n" + "="*20 + " Operation Result (General Translator) " + "="*20)
print(f"Profile: {general_translator.security_profile}")
print(result_general if result_general else "# Operation Error/No Result")
print("="*70)

print("\n" + "="*20 + " Operation Result (PII-Safe Translator) " + "="*20)
print(f"Profile: {pii_safe_translator.security_profile}")
print(result_pii_safe if result_pii_safe else "# Operation Error/No Result")
print("="*70)


print("\n--- Example Script 7 Finished ---") # Replaced logger.info
print("WARNING: This example demonstrates PROFILE ASSIGNMENT CONCEPT ONLY.") # Replaced logger.warning
print("WARNING: Actual PII masking based on profile requires implementation in Expert's _is_output_secure method.") # Replaced logger.warning
