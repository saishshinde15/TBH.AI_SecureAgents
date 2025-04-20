# Using Agent Security Profiles (Planned Feature)

The `tbh_secure_agents` framework includes a `security_profile` parameter in the `Agent` class constructor. This parameter is a key part of the framework's security-first design, intended to provide a mechanism for defining and potentially enforcing different security constraints and capabilities for individual agents.

**Current Status:** Alpha (Placeholder)

**IMPORTANT:** As of the current version (`0.0.1`), the `security_profile` parameter is primarily a **placeholder**. While you can assign a string value to it during agent initialization, the framework **does not yet automatically enforce specific security rules or behaviors based on this profile name.** The logic to interpret the profile and apply corresponding constraints needs to be implemented by the developer within the placeholder security methods or through future framework enhancements.

## How to Set `security_profile`

You assign a string name to the `security_profile` when creating an `Agent` instance:

```python
from tbh_secure_agents import Agent

# Example: Assigning different security profiles
research_agent = Agent(
    role='Researcher',
    goal='Gather information from trusted sources.',
    security_profile='high_trust_sources_only' # Profile for agents restricted to specific data sources
)

creative_agent = Agent(
    role='Creative Writer',
    goal='Generate fictional content.',
    security_profile='creative_standard' # Profile for general creative tasks
)

code_gen_agent = Agent(
    role='Code Generator',
    goal='Generate code snippets based on descriptions.',
    security_profile='code_generation_safe' # Profile for code generation with safety checks
)

default_agent = Agent(
    role='General Assistant',
    goal='Perform basic tasks.',
    # security_profile defaults to 'default' if not specified
)

print(f"{research_agent.role} profile: {research_agent.security_profile}")
print(f"{creative_agent.role} profile: {creative_agent.security_profile}")
print(f"{code_gen_agent.role} profile: {code_gen_agent.security_profile}")
print(f"{default_agent.role} profile: {default_agent.security_profile}")
```

## Intended Purpose and Future Implementation

The `security_profile` string is designed to act as an identifier for a specific set of security rules or configurations that should apply to that agent. The intended uses include:

1.  **Controlling LLM Interactions:**
    *   Potentially configuring stricter `safety_settings` or `generation_config` for the underlying LLM (e.g., Gemini) based on the profile (e.g., a 'child_safe' profile might have stricter content filters). *(Requires implementation)*
    *   Limiting the types of prompts the agent is allowed to send (e.g., preventing a 'read_only' profile from generating modification commands). *(Requires implementation in `_is_prompt_secure`)*

2.  **Governing Tool Access (Future Feature):**
    *   Restricting which tools an agent can access or use based on its profile (e.g., only agents with an 'executor' profile can run shell commands). *(Requires tool integration and profile checks)*

3.  **Tailoring Security Checks:**
    *   Implementing different logic within the placeholder security methods (`_is_prompt_secure`, `_is_output_secure`) based on the agent's `self.security_profile`. For example, an agent with a 'sensitive_data_handler' profile might have much stricter output scanning rules in `_is_output_secure` to prevent PII leakage compared to a 'public_summarizer' profile. *(Requires implementation in placeholder methods)*

4.  **Crew-Level Validation:**
    *   Allowing the `Crew` to validate if an agent with a specific profile is suitable or permitted for a given `Task` before execution begins. *(Requires implementation in `Crew`)*

## Implementing Profile Logic (Current Approach with Examples)

Currently, to make the `security_profile` functional, you would need to:

1.  **Define your profiles:** Decide on meaningful profile names (e.g., 'strict_pii', 'web_research_only', 'code_execution_sandbox', 'creative_standard').
2.  **Implement checks:** Modify the placeholder security methods in `agent.py` (and potentially `task.py`) to check `self.security_profile` and apply different logic accordingly.

### Example 1: Checking Output (`_is_output_secure` in `agent.py`)

```python
# Hypothetical helper functions (you would need to implement these)
def contains_pii(text: str) -> bool:
    # Logic to detect Personally Identifiable Information
    # ...
    return False # Placeholder

def contains_harmful_content(text: str) -> bool:
    # Logic to detect harmful content based on policy
    # ...
    return False # Placeholder

# --- Inside Agent class in agent.py ---
def _is_output_secure(self, output: str) -> bool:
    logger.debug(f"Performing output security check for Agent '{self.role}', Profile '{self.security_profile}'")
    is_secure = True # Assume secure by default

    if self.security_profile == 'strict_pii':
        # For this profile, disallow any detected PII
        if contains_pii(output):
            logger.warning(f"Output security check FAILED (PII detected) for Agent '{self.role}' (Profile: {self.security_profile}).")
            is_secure = False

    elif self.security_profile == 'creative_standard':
        # For this profile, check for generally harmful content
        if contains_harmful_content(output):
            logger.warning(f"Output security check FAILED (Harmful content) for Agent '{self.role}' (Profile: {self.security_profile}).")
            is_secure = False

    # Add checks for other profiles...

    # Default check for 'default' or unhandled profiles (could be lenient or strict)
    elif self.security_profile == 'default':
         # Maybe apply basic harmful content check for default
         if contains_harmful_content(output):
             logger.warning(f"Output security check FAILED (Harmful content) for Agent '{self.role}' (Profile: {self.security_profile}).")
             is_secure = False

    if not is_secure:
        logger.warning(f"Overall Output security check FAILED for Agent '{self.role}'.")

    return is_secure
```

### Example 2: Checking Prompt (`_is_prompt_secure` in `agent.py`)

```python
# Hypothetical helper function
def contains_disallowed_patterns(text: str, profile: str) -> bool:
    # Logic to check for patterns disallowed by a specific profile
    if profile == 'web_research_only':
        # Example: Disallow prompts asking to write files or execute code
        if "write file" in text.lower() or "execute command" in text.lower():
            return True
    # Add checks for other profiles...
    return False # Placeholder

# --- Inside Agent class in agent.py ---
def _is_prompt_secure(self, prompt: str) -> bool:
    logger.debug(f"Performing prompt security check for Agent '{self.role}', Profile '{self.security_profile}'")
    is_secure = True # Assume secure by default

    if contains_disallowed_patterns(prompt, self.security_profile):
        logger.warning(f"Prompt security check FAILED (Disallowed pattern) for Agent '{self.role}' (Profile: {self.security_profile}).")
        is_secure = False

    # Add other general prompt checks if needed (e.g., length limits)
    # ...

    if not is_secure:
        logger.warning(f"Overall Prompt security check FAILED for Agent '{self.role}'.")

    return is_secure
```

### Example 3: Task Pre-Check (`_pre_execution_secure` in `task.py`)

```python
# --- Inside Task class in task.py ---
def _pre_execution_secure(self) -> bool:
    logger.debug(f"Performing task pre-execution check for '{self.description[:50]}...'")
    is_secure = True # Assume secure by default

    # Check if the assigned agent's profile is suitable for this task type
    # (This requires more context about the task, maybe add a 'task_type' attribute to Task)
    # Example: Assume a hypothetical 'task_type' attribute exists
    # if hasattr(self, 'task_type') and self.task_type == 'code_execution':
    #     if not self.agent or self.agent.security_profile != 'code_execution_sandbox':
    #         logger.warning(f"Task pre-execution check FAILED: Agent profile '{self.agent.security_profile if self.agent else 'None'}' not allowed for task type 'code_execution'.")
    #         is_secure = False

    # Check the input context for sensitive data if the task requires it
    # if self.context and contains_sensitive_info(self.context): # Hypothetical function
    #     logger.warning(f"Task pre-execution check FAILED: Input context contains sensitive info.")
    #     is_secure = False

    if not is_secure:
        logger.warning(f"Overall Task pre-execution security check FAILED for '{self.description[:50]}...'.")

    return is_secure

```

As the `tbh_secure_agents` framework evolves, more built-in support for interpreting and enforcing security profiles based on these principles is planned. For now, the `security_profile` parameter serves as a crucial hook for developers to implement their own custom, profile-based security logic within the provided checkpoint methods.
