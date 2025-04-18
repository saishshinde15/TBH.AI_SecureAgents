# Usage Guide

![TBH.AI Logo](./assets/logo.png) <!-- Placeholder - Save logo here -->

This guide explains the core concepts of `tbh_secure_agents` and how to use them to build your multi-agent system.

## Core Concepts

The framework revolves around three main components:

1.  **`Agent`**: Represents an autonomous entity designed to perform specific tasks. Each agent has:
    *   A `role` (e.g., 'Researcher', 'Writer').
    *   A `goal` defining its primary objective.
    *   A `backstory` providing context (optional).
    *   An underlying Large Language Model (LLM), defaulting to Google Gemini (`gemini-2.0-flash-lite`).
    *   A `security_profile` (placeholder for future security configurations).
    *   Optionally, a list of `tools` it can use (feature planned).

2.  **`Task`**: Defines a unit of work to be performed by an agent. Each task has:
    *   A `description` clearly stating what needs to be done.
    *   An `expected_output` describing the desired result format (optional).
    *   An assigned `agent` responsible for executing it.
    *   Optional `context` providing necessary background information.

3.  **`Crew`**: Manages a group of agents and orchestrates the execution of a list of tasks. Key aspects include:
    *   A list of `agents`.
    *   A list of `tasks`.
    *   A `process` defining the execution flow (currently supports 'sequential', where tasks run one after another, passing results as context).

## Basic Workflow

Building an application with `tbh_secure_agents` typically involves these steps:

1.  **Import necessary classes:**
    ```python
    from tbh_secure_agents import Agent, Task, Crew
    ```

2.  **Define your Agents:** Create instances of the `Agent` class, specifying their roles, goals, and any other relevant parameters. Remember to handle API key configuration securely (preferably via the `GOOGLE_API_KEY` environment variable).
    ```python
    # Ensure GOOGLE_API_KEY is set in your environment
    # OR pass api_key='YOUR_KEY' for testing only (insecure)

    researcher = Agent(
        role='Senior Security Researcher',
        goal='Find the latest information on AI security vulnerabilities',
        backstory='An expert in cybersecurity with a focus on AI systems.'
        # api_key=YOUR_API_KEY # Testing only
    )

    writer = Agent(
        role='Technical Writer',
        goal='Summarize complex security information into concise reports',
        backstory='Skilled in communicating technical details clearly.'
        # api_key=YOUR_API_KEY # Testing only
    )
    ```

3.  **Define your Tasks:** Create instances of the `Task` class, providing clear descriptions and assigning the appropriate agent.
    ```python
    task1 = Task(
        description='Research and identify the top 3 AI security vulnerabilities reported in the last month.',
        expected_output='A list of the top 3 vulnerabilities with brief descriptions.',
        agent=researcher # Assign agent
    )

    task2 = Task(
        description='Based on the research findings, write a concise 2-paragraph summary for a non-technical audience.',
        expected_output='A short summary explaining the vulnerabilities simply.',
        agent=writer # Assign agent
        # Context will be passed automatically by the Crew in sequential mode
    )
    ```

4.  **Assemble the Crew:** Create an instance of the `Crew` class, passing in the list of agents and tasks. Specify the execution process (e.g., 'sequential').
    ```python
    security_crew = Crew(
        agents=[researcher, writer],
        tasks=[task1, task2],
        process='sequential'
    )
    ```

5.  **Kick off the process:** Call the `kickoff()` method on your `Crew` instance to start the execution.
    ```python
    try:
        result = security_crew.kickoff()
        print("Crew finished successfully!")
        print("\nFinal Result:")
        print(result)
    except Exception as e:
        print(f"An error occurred during crew execution: {e}")
    ```

## Example

Refer to the example scripts provided in the repository (e.g., `example_usage.py`, `example_usage_2.py`) for practical demonstrations of these concepts. The first example (`example_usage.py`) implements the Researcher/Writer scenario described above.

## Next Steps

*   Explore implementing custom security profiles.
*   Investigate adding tools to agents.
*   Experiment with different agent roles and task sequences.
*   Refer to the `security_focus.md` document for details on the framework's security approach (planned).
