# Usage Guide

![TBH Secure Agents Logo](./assets/logo.png)

This guide explains the core concepts of `tbh_secure_agents` and how to use them to build your multi-agent system.

## Core Concepts

The framework revolves around three main components:

1.  **`Expert`**: Represents an autonomous entity designed to perform specific operations. Each expert has:
    *   A `specialty` (e.g., 'Researcher', 'Writer').
    *   An `objective` defining its primary purpose.
    *   A `background` providing context (optional).
    *   An underlying Large Language Model (LLM), defaulting to Google Gemini (`gemini-2.0-flash-lite`).
    *   A `security_profile` (placeholder for future security configurations).
    *   Optionally, a list of `tools` it can use (feature planned).

2.  **`Operation`**: Defines a unit of work to be performed by an expert. Each operation has:
    *   `instructions` clearly stating what needs to be done.
    *   An `output_format` describing the desired result format (optional).
    *   An assigned `expert` responsible for executing it.
    *   Optional `context` providing necessary background information.

3.  **`Squad`**: Manages a group of experts and orchestrates the execution of a list of operations. Key aspects include:
    *   A list of `experts`.
    *   A list of `operations`.
    *   A `process` defining the execution flow (currently supports 'sequential', where operations run one after another, passing results as context).

## Basic Workflow

Building an application with `tbh_secure_agents` typically involves these steps:

1.  **Import necessary classes:**
    ```python
    from tbh_secure_agents import Expert, Operation, Squad
    ```

2.  **Define your Experts:** Create instances of the `Expert` class, specifying their specialty, objective, and any other relevant parameters. Remember to handle API key configuration securely (preferably via the `GOOGLE_API_KEY` environment variable).
    ```python
    # Ensure GOOGLE_API_KEY is set in your environment
    # OR pass api_key='YOUR_KEY' for testing only (insecure)

    researcher = Expert(
        specialty='Senior Security Researcher',
        objective='Find the latest information on AI security vulnerabilities',
        background='An expert in cybersecurity with a focus on AI systems.'
        # api_key=YOUR_API_KEY # Testing only
    )

    writer = Expert(
        specialty='Technical Writer',
        objective='Summarize complex security information into concise reports',
        background='Skilled in communicating technical details clearly.'
        # api_key=YOUR_API_KEY # Testing only
    )
    ```

3.  **Define your Operations:** Create instances of the `Operation` class, providing clear instructions and assigning the appropriate expert.
    ```python
    operation1 = Operation(
        instructions='Research and identify the top 3 AI security vulnerabilities reported in the last month.',
        output_format='A list of the top 3 vulnerabilities with brief descriptions.',
        expert=researcher # Assign expert
    )

    operation2 = Operation(
        instructions='Based on the research findings, write a concise 2-paragraph summary for a non-technical audience.',
        output_format='A short summary explaining the vulnerabilities simply.',
        expert=writer # Assign expert
        # Context will be passed automatically by the Squad in sequential mode
    )
    ```

4.  **Assemble the Squad:** Create an instance of the `Squad` class, passing in the list of experts and operations. Specify the execution process (e.g., 'sequential').
    ```python
    security_squad = Squad(
        experts=[researcher, writer],
        operations=[operation1, operation2],
        process='sequential'
    )
    ```

5.  **Define Guardrails (Optional):** Create a dictionary of guardrail inputs to guide the experts' behavior during execution.
    ```python
    guardrails = {
        "time_period": "last 30 days",
        "focus_area": "large language models",
        "audience": "executive leadership",
        "max_length": 500
    }
    ```

6.  **Deploy the Squad:** Call the `deploy()` method on your `Squad` instance, optionally passing guardrails, to start the execution.
    ```python
    try:
        # Deploy with guardrails
        result = security_squad.deploy(guardrails=guardrails)

        # Or deploy without guardrails
        # result = security_squad.deploy()

        print("Squad finished successfully!")
        print("\nFinal Result:")
        print(result)
    except Exception as e:
        print(f"An error occurred during squad execution: {e}")
    ```

## Example

Refer to the example scripts provided in the repository (e.g., `example_usage.py`, `example_usage_2.py`) for practical demonstrations of these concepts. The first example (`example_usage.py`) implements the Researcher/Writer scenario described above.

## Advanced Features

### Guardrails

Guardrails provide a way to pass dynamic inputs to your Squad during deployment. These inputs can be used to guide the experts' responses, enforce constraints, and provide additional context without modifying your core operations.

```python
# Define guardrail inputs
guardrails = {
    "topic": "AI ethics",
    "tone": "balanced",
    "include_examples": True,
    "max_length": 1000
}

# Deploy with guardrails
result = squad.deploy(guardrails=guardrails)
```

For more details on using guardrails, see the [Guardrails Guide](./guardrails_guide.md).

## Next Steps

*   Explore implementing custom security profiles.
*   Investigate adding tools to experts.
*   Experiment with different expert roles and operation sequences.
*   Try using guardrails to dynamically control expert behavior.
*   Refer to the `security_focus.md` document for details on the framework's security approach.
