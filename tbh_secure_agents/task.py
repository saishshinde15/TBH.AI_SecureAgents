# tbh_secure_agents/task.py
# Author: Saish (TBH.AI)

"""
Defines the Task class for the TBH Secure Agents framework.
Tasks represent units of work to be performed by agents.
"""

import logging # Import logging
from typing import Optional, Any
from .agent import Agent # Now we can import Agent

# Get a logger for this module
logger = logging.getLogger(__name__)

class Task:
    """
    Represents a specific task to be executed by an agent.

    Attributes:
        description (str): A clear description of the task.
        expected_output (str, optional): A description of the expected outcome or format.
        agent (Optional[Agent]): The agent assigned to this task. Can be assigned later.
        context (Optional[str]): Additional context or data needed for the task.
        # Add attributes like dependencies, priority, security_requirements, etc.
    """
    def __init__(self, description: str, expected_output: Optional[str] = None, agent: Optional[Agent] = None, context: Optional[str] = None, **kwargs):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent
        self.context = context
        self.result: Optional[str] = None # To store the outcome after execution
        # Initialize other relevant attributes

    def execute(self) -> str:
        """
        Executes the task, likely by calling the assigned agent's execution method.
        Includes security checks before and after execution.
        """
        if not self.agent:
            logger.error(f"Task execution failed: No agent assigned to task '{self.description[:50]}...'.") # Use logger
            raise ValueError("Task cannot be executed without an assigned agent.")

        # Placeholder call, actual logic is in _pre_execution_secure
        logger.debug(f"Performing pre-execution check for task '{self.description[:50]}...'")
        if not self._pre_execution_secure(): # Example placeholder check
            logger.error(f"Task pre-execution security check failed for '{self.description[:50]}...'. Aborting.")
        #     return "Error: Task failed pre-execution security check."

        logger.info(f"Task '{self.description[:50]}...' starting execution by agent '{self.agent.role}'.") # Use logger

        # Assuming the agent has an 'execute_task' method that accepts description and context
        try:
            # Pass the task description and any available context to the agent
            self.result = self.agent.execute_task(
                task_description=self.description,
                context=self.context # Pass context here
            )
            # Placeholder call, actual logic is in _post_execution_secure
            logger.debug(f"Performing post-execution check for task '{self.description[:50]}...'")
            if not self._post_execution_secure(self.result): # Example placeholder check
                logger.warning(f"Task post-execution security check failed for '{self.description[:50]}...'. Result may be compromised.")
                # TODO: Decide how to handle insecure result (e.g., return error, return sanitized, log only)

            logger.info(f"Task '{self.description[:50]}...' finished execution successfully.")
            return self.result
        except Exception as e:
            # Basic error logging implemented
            logger.error(f"Error executing task '{self.description[:50]}...': {e}", exc_info=True)
            # TODO: Decide whether to raise, return an error string, or handle differently based on policy
            raise # Re-raise for now, allows Crew to handle it

    # --- Placeholder Security Methods ---

    def _pre_execution_secure(self) -> bool:
        """Placeholder for task-specific pre-execution security checks. Needs implementation."""
        logger.debug(f"Performing task pre-execution check for '{self.description[:50]}...'")
        # TODO: Implement actual task-specific security logic (e.g., check context, task description itself)
        is_secure = True # Defaulting to secure
        if not is_secure:
            logger.warning(f"Task pre-execution security check FAILED for '{self.description[:50]}...'.")
        return is_secure

    def _post_execution_secure(self, result: Optional[str]) -> bool:
        """Placeholder for task-specific post-execution security checks. Needs implementation."""
        logger.debug(f"Performing task post-execution check for '{self.description[:50]}...'")
        # TODO: Implement actual task-specific security logic (e.g., validate result against expected_output format, check for sensitive info leakage based on task type)
        is_secure = True # Defaulting to secure
        if not is_secure:
            logger.warning(f"Task post-execution security check FAILED for '{self.description[:50]}...'.")
        return is_secure

    def __str__(self):
        return f"Task(description='{self.description}', agent='{self.agent.role if self.agent else 'Unassigned'}')"
