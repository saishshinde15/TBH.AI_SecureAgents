# Security Checkpoints in TBH Secure Agents

The `tbh_secure_agents` framework is designed with security in mind, incorporating explicit points within the agent and task execution lifecycle where custom security logic can be implemented. These are currently placeholder methods that always return `True`, but they provide the structure for adding robust validation.

Here's a breakdown of the four main security checkpoints:

## 1. Task Pre-Execution Check (`Task._pre_execution_secure()`)

*   **File:** `tbh_secure_agents/task.py`
*   **Called By:** `Task.execute()`
*   **When:** Immediately after `Task.execute()` is called, *before* the task description or context is passed to the assigned agent's `execute_task()` method.
*   **Purpose:** To perform task-level validation *before* the agent begins processing. This is the place to check:
    *   If the input `context` provided to the task is safe or sanitized.
    *   If the task `description` itself contains disallowed instructions or patterns.
    *   If the assigned `agent` has the necessary permissions or `security_profile` to execute this *type* of task.
    *   Any other task-specific preconditions based on security policy.
*   **Current Behavior:** Returns `True`. If implemented to return `False`, the task execution could be aborted before involving the agent.

## 2. Agent Prompt Check (`Agent._is_prompt_secure()`)

*   **File:** `tbh_secure_agents/agent.py`
*   **Called By:** `Agent.execute_task()`
*   **When:** After the agent has constructed the full prompt (including role, goal, backstory, context, and task description) but *before* this prompt is sent to the underlying LLM (e.g., Google Gemini).
*   **Purpose:** To validate the final prompt that the LLM will process. This is crucial for preventing:
    *   Prompt injection attacks.
    *   Requests that violate the agent's defined `security_profile` or operational constraints.
    *   Accidental inclusion of sensitive data in the prompt being sent to the external LLM service.
*   **Current Behavior:** Returns `True`. If implemented to return `False`, the LLM call is skipped, and an error is returned.

## 3. Agent Output Check (`Agent._is_output_secure()`)

*   **File:** `tbh_secure_agents/agent.py`
*   **Called By:** `Agent.execute_task()`
*   **When:** Immediately *after* the LLM returns its response but *before* the agent returns this result back to the calling `Task`.
*   **Purpose:** To validate or sanitize the raw output received from the LLM. This is the place to:
    *   Scan the output for harmful content, hate speech, etc.
    *   Detect and filter/mask sensitive data leakage (PII, secrets).
    *   Validate if the output format matches expectations for the agent's role.
    *   Apply any necessary sanitization based on the agent's `security_profile`.
*   **Current Behavior:** Returns `True`. If implemented to return `False`, the potentially insecure output is rejected, and an error is returned.

## 4. Task Post-Execution Check (`Task._post_execution_secure()`)

*   **File:** `tbh_secure_agents/task.py`
*   **Called By:** `Task.execute()`
*   **When:** After the agent's `execute_task()` method has successfully returned a result (which has already passed `_is_output_secure`).
*   **Purpose:** To perform final validation on the result *in the context of the specific task*. This allows for checks like:
    *   Does the final result conform to the `expected_output` format defined for this specific `Task`?
    *   Does the result securely fulfill the task's objective?
    *   Are there any final task-specific sanitizations or transformations needed before considering the task complete?
*   **Current Behavior:** Returns `True`. If implemented to return `False`, a warning is logged, but the result is currently still returned (behavior upon failure could be customized).

By implementing logic within these four placeholder methods, developers can create layered security controls tailored to their application's specific needs and threat model.
