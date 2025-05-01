# TBH Secure Agents: Version Changes

<img width="618" alt="Main" src="https://github.com/user-attachments/assets/dbbf5a4f-7b0b-4f43-9b37-ef77dc761ff1" />

This document outlines the key changes and enhancements in the latest version of the TBH Secure Agents framework.

## New Guardrails System

The most significant enhancement in this version is the introduction of a comprehensive guardrails system that allows for dynamic control of expert behavior at runtime.

### Template Variables

You can now use template variables in expert profiles and operation instructions:

```python
# Expert with template variables
expert = Expert(
    specialty="Content Writer specializing in {domain}",
    objective="Create {content_type} content for {audience}",
    background="You have experience writing {tone} content about {domain}."
)

# Operation with template variables
operation = Operation(
    instructions="Write a {length} article about {topic} for {audience}.",
    output_format="A well-formatted {content_type}"
)
```

These variables are replaced with values from the guardrails when the squad is deployed:

```python
result = squad.deploy(guardrails={
    "domain": "healthcare",
    "content_type": "blog post",
    "audience": "medical professionals",
    "tone": "professional",
    "length": "1000-word",
    "topic": "AI in medical diagnosis"
})
```

### Conditional Formatting with Select Syntax

The new select syntax allows for conditional content based on guardrail values:

```python
operation = Operation(
    instructions="""
    Write a report about {topic}.

    {tone, select,
      formal:Use a professional, academic tone suitable for scholarly publications.|
      conversational:Use a friendly, approachable tone as if speaking directly to the reader.|
      technical:Use precise technical language appropriate for experts in the field.
    }

    {include_examples, select,
      true:Include practical examples to illustrate key points.|
      false:Focus on theoretical concepts without specific examples.
    }
    """,
    expert=content_expert
)
```

This powerful feature enables dynamic instruction generation based on runtime parameters.

## Enhanced Security Features

We've consolidated and enhanced the security features in this version:

### 1. Improved Prompt Injection Defenses

- Enhanced contextual analysis of prompts
- More sophisticated pattern detection for injection attempts
- Better detection of authority-based and emotional manipulation tactics

### 2. Enhanced Data Leakage Prevention

- Expanded PII detection including international formats
- New output sanitization capabilities to redact sensitive information
- Security profile-specific handling of sensitive data

### 3. Strengthened Multi-Agent Security

- Dynamic trust relationships between experts
- Operation authenticity verification
- Enhanced context passing security
- Expert compatibility validation

### 4. Improved Reliability Mechanisms

- Enhanced hallucination detection
- Better consistency checking
- More sophisticated format compliance validation
- Improved relevance checking for outputs

## Documentation Improvements

We've reorganized and enhanced the documentation:

- Consolidated security documentation into a comprehensive guide (`security_features_comprehensive.md`)
- Created a comprehensive guardrails guide with security focus (`guardrails_comprehensive.md`)
- Added detailed examples for guardrails and select syntax with real-world use cases
- Improved best practices sections with security recommendations
- Added security-focused examples (`security_guardrails.py`)
- Consolidated redundant documentation for better maintainability

## API Changes

The API has been updated to support the new features:

### Template Variable Support

- Added support for template variables in expert profiles (specialty, objective, background)
- Added support for template variables in operation instructions and output formats
- Implemented the `_format_with_inputs` method to handle template variable replacement
- Enhanced security methods to be more flexible with template variables
- Modified the relevance checking to handle template variables appropriately

## Examples

We've added new examples to demonstrate the new features:

- `examples/example_guardrails.py`: Basic example of guardrails usage
- `examples/advanced_guardrails.py`: Advanced example with complex template variables and conditional formatting
- `examples/security_guardrails.py`: Security-focused example demonstrating how to use guardrails to implement dynamic security controls

## Future Directions

In future versions, we plan to:

1. Expand the guardrails system with more advanced features
2. Add support for more complex conditional logic
3. Enhance the security features with machine learning-based anomaly detection
4. Improve the integration with external systems
5. Add more specialized security profiles for different use cases
