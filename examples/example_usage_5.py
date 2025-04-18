# example_usage_5.py
# Demonstrates a more complex use case: Code Review, Security Advice, Refactoring

import os
from tbh_secure_agents import Agent, Task, Crew

# --- !!! SECURITY WARNING !!! ---
# Using a hardcoded API key for testing ONLY. Replace with environment variables for production.
TESTING_API_KEY = "" # Key provided by user
# --- !!! /SECURITY WARNING !!! ---

# --- Input Code Snippet ---
original_code = """
import os
import subprocess

# WARNING: This code has potential security issues for demonstration purposes.
def execute_command(user_input):
    # Directly using user input in a shell command is dangerous
    command = "echo 'User provided: ' && echo " + user_input
    print(f"Executing: {command}")
    # Using shell=True with user input is highly risky
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
"""
# --- /Input Code Snippet ---

print("--- Initializing Agents (Use Case 5) ---")
try:
    reviewer = Agent(
        role='Security Code Reviewer',
        goal='Identify potential security vulnerabilities in Python code snippets, focusing on command injection and unsafe practices.',
        backstory='Experienced in static code analysis and identifying common security pitfalls.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='code_review_strict',
        api_key=TESTING_API_KEY
    )

    advisor = Agent(
        role='Security Best Practices Advisor',
        goal='Provide specific, actionable recommendations to fix identified security vulnerabilities in Python code.',
        backstory='Expert in secure coding practices and mitigating risks like command injection.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='security_advice_standard',
        api_key=TESTING_API_KEY
    )

    refactorer = Agent(
        role='Python Code Refactorer',
        goal='Rewrite Python code snippets to incorporate security improvements based on provided suggestions.',
        backstory='Skilled in modifying code while preserving intended functionality but enhancing security.',
        llm_model_name='gemini-2.0-flash-lite',
        security_profile='code_refactor_safe',
        api_key=TESTING_API_KEY
    )
except Exception as e:
    print(f"\nError initializing agents: {e}")
    exit()

print("\n--- Defining Tasks (Use Case 5) ---")
task_review = Task(
    description=f'Review the following Python code for potential security vulnerabilities, especially related to command injection and the use of subprocess with shell=True. List the identified issues clearly. Code:\n```python\n{original_code}\n```',
    expected_output='A list of identified security vulnerabilities.',
    agent=reviewer
)

task_suggest = Task(
    description='Based *only* on the provided security review findings, suggest specific code changes or alternative approaches to mitigate the identified vulnerabilities in the original code snippet.',
    expected_output='Actionable suggestions for improving the code\'s security.',
    agent=advisor
    # Context: Review findings from task_review
)

task_refactor = Task(
    description=f'Rewrite the original Python code snippet provided below, incorporating *only* the security suggestions provided in the context. Ensure the core functionality (executing some form of command safely, if possible, or demonstrating safe handling) is addressed. Original Code:\n```python\n{original_code}\n```',
    expected_output='The refactored Python code snippet incorporating security improvements.',
    agent=refactorer
    # Context: Security suggestions from task_suggest
)

print("\n--- Creating Crew (Use Case 5) ---")
security_analysis_crew = Crew(
    agents=[reviewer, advisor, refactorer],
    tasks=[task_review, task_suggest, task_refactor],
    process='sequential'
)

print("\n--- Running Crew (Use Case 5) ---")
try:
    final_refactored_code = security_analysis_crew.kickoff()

    print("\n--- Crew Execution Finished (Use Case 5) ---")

    review_findings = task_review.result
    suggestions = task_suggest.result

    print("\nOriginal Code:")
    print("----------------")
    print(original_code)
    print("----------------")

    print("\nSecurity Review Findings:")
    print("-------------------------")
    print(review_findings if review_findings else "# Error generating review.")
    print("-------------------------")

    print("\nImprovement Suggestions:")
    print("------------------------")
    print(suggestions if suggestions else "# Error generating suggestions.")
    print("------------------------")

    print("\nRefactored Code:")
    print("------------------")
    print(final_refactored_code if final_refactored_code else "# Error generating refactored code.")
    print("------------------")

except Exception as e:
    print(f"\nAn error occurred during crew execution: {e}")

print("\n--- Example Script 5 Finished ---")
