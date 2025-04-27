# Expert Security Profiles

<img width="618" alt="Main" src="https://github.com/user-attachments/assets/dbbf5a4f-7b0b-4f43-9b37-ef77dc761ff1" />

The `tbh_secure_agents` framework includes a `security_profile` parameter in the `Expert` class constructor. This parameter is a key part of the framework's security-first design, providing a mechanism for defining and enforcing different security constraints and capabilities for individual experts.

**Current Status:** Implemented

The `security_profile` parameter is now fully implemented with comprehensive security checks. When you assign a security profile to an expert, the framework automatically enforces specific security rules and behaviors based on this profile name. The security checks are implemented in the `_is_prompt_secure`, `_is_output_secure`, and other security methods throughout the framework.

## How to Set `security_profile`

You assign a string name to the `security_profile` when creating an `Expert` instance:

```python
from tbh_secure_agents import Expert

# Example: Assigning different security profiles
security_researcher = Expert(
    specialty='Security Researcher',
    objective='Identify vulnerabilities in systems',
    background='Expert in cybersecurity',
    security_profile='high_security' # High security profile for sensitive research
)

creative_writer = Expert(
    specialty='Creative Writer',
    objective='Generate fictional content',
    background='Experienced fiction author',
    security_profile='creative_standard' # Profile for general creative tasks
)

code_generator = Expert(
    specialty='Code Generator',
    objective='Generate secure code snippets based on descriptions',
    background='Experienced software developer',
    security_profile='code_restricted' # Profile for code generation with safety checks
)

data_processor = Expert(
    specialty='Data Processor',
    objective='Process user data while protecting privacy',
    background='Data scientist with privacy expertise',
    security_profile='pii_protection' # Profile for handling personally identifiable information
)

default_expert = Expert(
    specialty='General Assistant',
    objective='Perform basic tasks',
    background='Versatile assistant',
    # security_profile defaults to 'default' if not specified
)

print(f"{security_researcher.specialty} profile: {security_researcher.security_profile}")
print(f"{creative_writer.specialty} profile: {creative_writer.security_profile}")
print(f"{code_generator.specialty} profile: {code_generator.security_profile}")
print(f"{data_processor.specialty} profile: {data_processor.security_profile}")
print(f"{default_expert.specialty} profile: {default_expert.security_profile}")
```

## Available Security Profiles

The TBH Secure Agents framework includes the following security profiles:

### General Security Profiles

| Profile Name | Description | Use Cases |
|--------------|-------------|-----------|
| `default` | Basic security checks with standard protections | General purpose tasks with low security requirements |
| `high_security` | Comprehensive security checks with strict enforcement | Handling sensitive information or executing critical operations |
| `pii_protection` | Enhanced checks for personally identifiable information | Processing user data or information that might contain PII |
| `confidential` | Strict checks for confidential information | Handling business-sensitive or classified information |
| `code_restricted` | Enhanced checks for code injection attempts | When processing or generating content that might contain code |

### Specialized Security Profiles

| Profile Name | Description | Use Cases |
|--------------|-------------|-----------|
| `research_standard` | Balanced security for research tasks | Information gathering and research operations |
| `reporting_standard` | Security checks focused on information disclosure | Generating reports and summaries |
| `creative_standard` | Security checks that allow creative freedom while maintaining safety | Creative writing and content generation |
| `marketing_safe` | Checks focused on appropriate content and brand safety | Marketing content generation |
| `web_code_gen` | Security checks for web application code generation | Generating web application code |
| `readme_standard` | Basic checks for documentation generation | Creating documentation files |
| `data_extraction_strict` | Strict checks for data extraction operations | Extracting structured data from unstructured sources |
| `reporting_concise` | Security checks for concise reporting | Generating brief summaries and reports |
| `code_review_strict` | Comprehensive checks for code review operations | Reviewing code for security vulnerabilities |
| `security_advice_standard` | Checks for security advice generation | Providing security recommendations |
| `code_refactor_safe` | Security checks for code refactoring operations | Refactoring code while maintaining security |

## How Security Profiles Work

Security profiles influence the behavior of several security checkpoints in the framework:

1. **Pre-Prompt Security Checks**: Before sending prompts to the LLM, the framework checks if the prompt is secure based on the expert's security profile.

2. **Post-Output Security Checks**: After receiving output from the LLM, the framework validates it against the security profile's requirements.

3. **Operation Security Validation**: Before executing operations, the framework checks if they comply with the security profile's constraints.

4. **Context Passing Security**: When passing context between operations, the framework applies security checks based on the profiles of both the source and target experts.

## Security Profile Implementation

The security profiles are implemented in the framework's security methods. Here are examples of how they work:

### Example 1: Prompt Security Checks (`_is_prompt_secure` in `agent.py`)

```python
def _is_prompt_secure(self, prompt: str) -> bool:
    """
    Performs security checks on prompts before they are sent to the LLM.
    Detects and prevents potential prompt injection and hijacking attempts.
    """
    logger.debug(f"Performing prompt security check for Expert '{self.specialty}', Profile '{self.security_profile}'")

    # 1. Check for excessive length (potential resource exhaustion attack)
    max_prompt_length = 10000  # Reasonable limit to prevent resource exhaustion
    if len(prompt) > max_prompt_length:
        logger.warning(f"Prompt security check FAILED: Prompt exceeds maximum length")
        return False

    # 2. Check for common hijacking patterns
    hijacking_patterns = [
        r"ignore previous instructions",
        r"ignore your previous instructions",
        r"disregard your instructions",
        # ... more patterns
    ]

    for pattern in hijacking_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            logger.warning(f"Prompt security check FAILED: Detected potential hijacking pattern: '{pattern}'")
            return False

    # 3. Apply profile-specific checks
    if self.security_profile == 'high_security':
        # Additional checks for high security profiles
        high_security_patterns = [
            r"execute code",
            r"run command",
            r"system\s*\(",
            # ... more patterns
        ]

        for pattern in high_security_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                logger.warning(f"Prompt security check FAILED: High security profile detected unauthorized pattern")
                return False

    # All checks passed
    logger.debug(f"Prompt security check PASSED for Expert '{self.specialty}'")
    return True
```

### Example 2: Output Security Checks (`_is_output_secure` in `agent.py`)

```python
def _is_output_secure(self, output: str) -> bool:
    """
    Performs security checks on LLM outputs before they are returned.
    Detects and prevents potential data leakage and harmful content.
    """
    logger.debug(f"Performing output security check for Expert '{self.specialty}', Profile '{self.security_profile}'")

    # Apply PII detection based on security profile
    if self.security_profile in ['high_security', 'pii_protection', 'confidential']:
        pii_patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\b(\+\d{1,3}[\s-])?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
            # ... more patterns
        }

        for pii_type, pattern in pii_patterns.items():
            if re.search(pattern, output, re.IGNORECASE):
                logger.warning(f"Output security check FAILED: Detected potential {pii_type} in output")
                return False

    # Check for code injection attempts in the output
    if self.security_profile in ['high_security', 'code_restricted']:
        code_patterns = [
            r'<script.*?>.*?</script>',
            r'javascript:',
            r'eval\(',
            # ... more patterns
        ]

        for pattern in code_patterns:
            if re.search(pattern, output, re.IGNORECASE):
                logger.warning(f"Output security check FAILED: Detected potential code injection in output")
                return False

    # All checks passed
    logger.debug(f"Output security check PASSED for Expert '{self.specialty}'")
    return True
```

### Example 3: Operation Security Validation (`_validate_operation_security` in `crew.py`)

```python
def _validate_operation_security(self, operation: Operation, index: int) -> bool:
    """
    Validates the security of an operation before execution.
    """
    # Check for potentially dangerous operations based on keywords
    dangerous_patterns = [
        r'\b(?:system|exec|eval|subprocess)\s*\(',
        r'\b(?:rm\s+-rf|rmdir\s+/|format\s+[a-z]:)',
        # ... more patterns
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, operation.instructions, re.IGNORECASE):
            logger.error(f"Operation security validation failed: Potentially dangerous operation detected")
            return False

    # Check expert-operation compatibility
    if operation.expert and hasattr(operation.expert, 'security_profile'):
        if operation.expert.security_profile == 'code_restricted' and 'execute code' in operation.instructions.lower():
            logger.error(f"Operation security validation failed: Operation not compatible with expert security profile")
            return False

    # All checks passed
    return True
```

## Best Practices for Using Security Profiles

1. **Match Profiles to Tasks**: Assign security profiles based on the specific requirements of each task.

2. **Combine Profiles Strategically**: When using multiple experts, consider how their security profiles interact, especially in sequential operations.

3. **Start Strict, Relax if Needed**: Begin with stricter profiles and relax them only if necessary, rather than starting with minimal security.

4. **Monitor and Audit**: Regularly review the logs to ensure security profiles are working as expected.

5. **Update Profiles**: As new security threats emerge, update your security profiles to address them.

## Security Profile Inheritance

When operations are executed in a sequential process, security considerations from earlier operations can influence later ones. The framework implements security profile inheritance to ensure consistent security enforcement throughout the execution chain.

For example, if an operation with a `high_security` profile passes context to an operation with a `default` profile, the framework will apply additional security checks to ensure the integrity of the execution chain is maintained.

