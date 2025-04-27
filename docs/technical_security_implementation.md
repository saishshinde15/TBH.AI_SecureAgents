# Technical Security Implementation in TBH Secure Agents Framework

![TBH Secure Agents Logo](./assets/logo.png)

This document provides technical details about the security implementation in the TBH Secure Agents framework, focusing on the code-level implementation of security features.

## Security Architecture Overview

The TBH Secure Agents framework implements a multi-layered security architecture with eight security checkpoints distributed across three levels:

1. **Expert Level**: Security checks related to LLM interactions
2. **Operation Level**: Security checks related to operation execution
3. **Squad Level**: Security checks related to multi-agent orchestration

Each security checkpoint is implemented as a method that returns a boolean value indicating whether the security check passed or failed. When a security check fails, the framework takes appropriate action, such as aborting the operation or returning an error message.

## Expert-Level Security Implementation

### Pre-Prompt Security Check (`_is_prompt_secure`)

This method in the `Expert` class validates prompts before they are sent to the LLM:

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

    # 3. Check for attempts to extract system prompts
    system_prompt_extraction_patterns = [
        r"what were your instructions",
        r"what is your system prompt",
        # ... more patterns
    ]

    for pattern in system_prompt_extraction_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            logger.warning(f"Prompt security check FAILED: Detected attempt to extract system prompt")
            return False

    # 4. Apply profile-specific checks
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

### Post-Output Security Check (`_is_output_secure`)

This method in the `Expert` class validates LLM outputs before they are returned:

```python
def _is_output_secure(self, output: str) -> bool:
    """
    Performs security checks on LLM outputs before they are returned.
    Detects and prevents potential data leakage and harmful content.
    """
    logger.debug(f"Performing output security check for Expert '{self.specialty}', Profile '{self.security_profile}'")

    if not output:
        logger.warning("Output security check: Empty output received")
        return False

    # 1. Check for potential PII leakage
    pii_patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b(\+\d{1,3}[\s-])?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
        'credit_card': r'\b(?:\d{4}[- ]?){3}\d{4}\b',
        'ip_address': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        # ... more patterns
    }

    # Apply PII detection based on security profile
    if self.security_profile in ['high_security', 'pii_protection', 'confidential']:
        for pii_type, pattern in pii_patterns.items():
            if re.search(pattern, output, re.IGNORECASE):
                logger.warning(f"Output security check FAILED: Detected potential {pii_type} in output")
                return False

    # 2. Check for harmful content
    harmful_content_patterns = [
        r'\b(?:bomb|explosive|terrorist|terrorism|attack plan)\b',
        r'\b(?:hack|exploit|vulnerability|attack vector|zero-day)\b',
        # ... more patterns
    ]

    for pattern in harmful_content_patterns:
        if re.search(pattern, output, re.IGNORECASE):
            logger.warning(f"Output security check FAILED: Detected potentially harmful content")
            return False

    # All checks passed
    logger.debug(f"Output security check PASSED for Expert '{self.specialty}'")
    return True
```

## Operation-Level Security Implementation

### Pre-Execution Security Check (`_pre_execution_secure`)

This method in the `Operation` class validates operations before execution:

```python
def _pre_execution_secure(self) -> bool:
    """
    Performs security checks before executing an operation.
    Validates the operation instructions, context, and expert assignment to prevent exploitation.
    """
    logger.debug(f"Performing operation pre-execution check for '{self.instructions[:50]}...'")

    # 1. Check if operation has valid instructions
    if not self.instructions or len(self.instructions.strip()) < 10:
        logger.warning(f"Operation pre-execution security check FAILED: Instructions too short or empty")
        return False

    # 2. Check for excessive instruction length (potential resource exhaustion)
    if len(self.instructions) > 10000:
        logger.warning(f"Operation pre-execution security check FAILED: Instructions too long")
        return False

    # 3. Check for potentially dangerous operations based on keywords
    dangerous_operation_patterns = [
        r'\b(?:system|exec|eval|subprocess)\s*\(',
        r'\b(?:rm\s+-rf|rmdir\s+/|format\s+[a-z]:)',
        # ... more patterns
    ]

    for pattern in dangerous_operation_patterns:
        if re.search(pattern, self.instructions, re.IGNORECASE):
            logger.warning(f"Operation pre-execution security check FAILED: Potentially dangerous operation")
            return False

    # All checks passed
    logger.debug(f"Operation pre-execution security check PASSED for '{self.instructions[:50]}...'")
    return True
```

### Post-Execution Security Check (`_post_execution_secure`)

This method in the `Operation` class validates operation results:

```python
def _post_execution_secure(self, result: Optional[str]) -> bool:
    """
    Performs security checks on operation results after execution.
    Validates the output for reliability, consistency, and security concerns.
    """
    logger.debug(f"Performing operation post-execution check for '{self.instructions[:50]}...'")

    # 1. Check if result exists
    if not result:
        logger.warning(f"Operation post-execution security check FAILED: Empty result")
        return False

    # 2. Check for hallucination indicators
    hallucination_patterns = [
        r"I don't actually (have|know|possess)",
        r"I'm making this up",
        r"I'm not sure (about|if) this is (correct|accurate|right)",
        # ... more patterns
    ]

    for pattern in hallucination_patterns:
        if re.search(pattern, result, re.IGNORECASE):
            logger.warning(f"Operation post-execution security check FAILED: Potential hallucination")
            return False

    # 3. Check for format compliance if output_format is specified
    if self.output_format:
        # Basic format compliance checks based on output_format specification
        if "json" in self.output_format.lower() and not (result.strip().startswith('{') and result.strip().endswith('}')):
            logger.warning(f"Operation post-execution security check FAILED: Result not in expected format")
            return False

    # All checks passed
    logger.debug(f"Operation post-execution security check PASSED for '{self.instructions[:50]}...'")
    return True
```

## Squad-Level Security Implementation

### Squad Security Validation (`_validate_squad_security`)

This method in the `Squad` class validates the entire squad configuration:

```python
def _validate_squad_security(self) -> bool:
    """
    Validates the security of the squad configuration before execution.
    Checks for potential security issues in the squad setup.
    """
    logger.debug("Validating squad security...")

    # 1. Check if there are any experts and operations
    if not self.experts:
        logger.error("Squad security validation failed: No experts in squad")
        return False

    if not self.operations:
        logger.error("Squad security validation failed: No operations in squad")
        return False

    # 2. Check for excessive resource usage
    total_instruction_length = sum(len(operation.instructions) for operation in self.operations)
    if total_instruction_length > 100000:  # Arbitrary limit
        logger.error(f"Squad security validation failed: Total operation instructions too long")
        return False

    # All checks passed
    logger.debug("Squad security validation passed")
    return True
```

### Operation Security Validation (`_validate_operation_security`)

This method in the `Squad` class validates individual operations:

```python
def _validate_operation_security(self, operation: Operation, index: int) -> bool:
    """
    Validates the security of an operation before execution.
    """
    # 1. Check for potentially dangerous operations based on keywords
    dangerous_patterns = [
        r'\b(?:system|exec|eval|subprocess)\s*\(',
        r'\b(?:rm\s+-rf|rmdir\s+/|format\s+[a-z]:)',
        # ... more patterns
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, operation.instructions, re.IGNORECASE):
            logger.error(f"Operation security validation failed: Potentially dangerous operation")
            return False

    # 2. Check expert-operation compatibility
    if operation.expert and hasattr(operation.expert, 'security_profile'):
        if operation.expert.security_profile == 'code_restricted' and 'execute code' in operation.instructions.lower():
            logger.error(f"Operation security validation failed: Operation not compatible with expert")
            return False

    # All checks passed
    return True
```

### Context Passing Security (`_is_safe_for_context_passing`)

This method in the `Squad` class validates context before passing it between operations:

```python
def _is_safe_for_context_passing(self, previous_result: str, next_operation: Operation) -> bool:
    """
    Checks if a previous operation's result is safe to pass as context to the next operation.
    """
    # 1. Check for excessive length
    if len(previous_result) > 50000:
        logger.warning("Context passing check: Previous result too long")
        return False

    # 2. Check for potentially harmful content
    harmful_patterns = [
        r'\b(?:bomb|explosive|terrorist|terrorism|attack plan)\b',
        r'\b(?:hack|exploit|vulnerability|attack vector|zero-day)\b',
        # ... more patterns
    ]

    for pattern in harmful_patterns:
        if re.search(pattern, previous_result, re.IGNORECASE):
            logger.warning("Context passing check: Potentially harmful content")
            return False

    # 3. Check for potential prompt injection attempts in the previous result
    injection_patterns = [
        r"ignore (previous|prior|above) instructions",
        r"disregard (previous|prior|above) instructions",
        # ... more patterns
    ]

    for pattern in injection_patterns:
        if re.search(pattern, previous_result, re.IGNORECASE):
            logger.warning("Context passing check: Potential prompt injection")
            return False

    # All checks passed
    return True
```

### Final Result Audit (`_audit_squad_results`)

This method in the `Squad` class performs a final security audit on the squad execution results:

```python
def _audit_squad_results(self, final_output: Optional[str]) -> bool:
    """
    Performs a security audit on the final results of the squad execution.
    """
    logger.debug("Performing squad result audit...")

    # 1. Check if there is a final output
    if not final_output:
        logger.warning("Squad result audit: No final output")
        return True  # Not necessarily a failure

    # 2. Check for excessive output length
    if len(final_output) > 100000:  # Arbitrary limit
        logger.warning("Squad result audit failed: Final output too long")
        return False

    # 3. Check execution metrics for anomalies
    if hasattr(self, 'execution_metrics'):
        # Check for operations that took too long
        if self.execution_metrics.get('total_execution_time', 0) > 300:  # 5 minutes
            logger.warning("Squad result audit: Execution took unusually long")
            # Warning only, not a failure

    # All checks passed
    logger.debug("Squad result audit passed")
    return True
```

## Security Profile Implementation

Security profiles are implemented as string identifiers that determine which security checks are applied. The framework includes several predefined security profiles:

- `default`: Basic security checks with standard protections
- `high_security`: Comprehensive security checks with strict enforcement
- `pii_protection`: Enhanced checks for personally identifiable information
- `confidential`: Strict checks for confidential information
- `code_restricted`: Enhanced checks for code injection attempts

Each security checkpoint method checks the security profile of the expert or operation and applies appropriate security checks based on the profile.

## Pattern Matching Implementation

The framework uses regular expressions for pattern matching to detect security issues. The patterns are organized into categories:

- **Hijacking Patterns**: Patterns that indicate attempts to hijack the expert
- **System Prompt Extraction Patterns**: Patterns that indicate attempts to extract system prompts
- **PII Patterns**: Patterns that match personally identifiable information
- **Harmful Content Patterns**: Patterns that match harmful or inappropriate content
- **Hallucination Patterns**: Patterns that indicate LLM hallucinations
- **Dangerous Operation Patterns**: Patterns that match potentially dangerous operations
- **Data Exfiltration Patterns**: Patterns that match attempts to exfiltrate data
- **Privilege Escalation Patterns**: Patterns that match attempts to escalate privileges
- **Denial of Service Patterns**: Patterns that match attempts to cause denial of service
- **Injection Patterns**: Patterns that match prompt injection attempts

## Execution Metrics Implementation

The framework tracks execution metrics for security monitoring:

```python
self.execution_metrics = {
    'start_time': time.time(),
    'operations_completed': 0,
    'operations_failed': 0,
    'total_operations': len(self.operations),
    'execution_path': []
}
```

Each operation execution is recorded in the `execution_path` with details such as start time, end time, execution time, and status. These metrics are used for security auditing and anomaly detection.

## Logging Implementation

The framework uses Python's logging module for comprehensive logging of security events:

```python
logger.debug(f"Performing prompt security check for Expert '{self.specialty}', Profile '{self.security_profile}'")
logger.warning(f"Prompt security check FAILED: Detected potential hijacking pattern: '{pattern}'")
logger.error(f"Squad security validation failed: No experts in squad")
```

Log messages include detailed information about the security check, the reason for failure, and the context in which the failure occurred. This provides a comprehensive audit trail for security events.

## Future Technical Enhancements

The framework is designed to be extensible, allowing for future technical enhancements:

1. **Machine Learning-Based Security**: Implementing machine learning models for more sophisticated pattern detection and anomaly detection.

2. **Formal Verification**: Implementing formal verification of critical security components to ensure correctness.

3. **Security Metrics**: Implementing more sophisticated security metrics and analytics for monitoring and auditing.

4. **Threat Intelligence Integration**: Incorporating external threat intelligence feeds to stay ahead of emerging threats.

5. **Tool Access Control**: Implementing fine-grained control over which tools experts can access, with security profile-based permissions.
