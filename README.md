# TBH Secure Agents

<img width="618" alt="Main" src="https://github.com/user-attachments/assets/dbbf5a4f-7b0b-4f43-9b37-ef77dc761ff1" /> <!-- Placeholder badge --> <!-- Placeholder badge -->

**A secure multi-agent framework by TBH.AI focused on high security, reliability, and safe AI orchestration.**

This package provides tools and structures for building multi-agent systems with a strong emphasis on security principles. It enables developers to create, manage, and deploy teams of AI experts (agents) that can work together on complex tasks while maintaining robust security controls to prevent common vulnerabilities in AI systems.

TBH Secure Agents addresses critical security concerns in multi-agent systems including agent hijacking, data leakage, exploitation between agents, and reliability issues. The framework is designed for developers who need to build secure, production-ready multi-agent applications.

Developed by Saish at TBH.AI.

## Key Features

*   **High Security Focus:** Built with security best practices from the ground up, including:
    * Agent hijacking prevention
    * Data leakage protection
    * Multi-agent exploitation prevention
    * Reliability enhancements to reduce hallucinations
*   **Modular Expert Design:** Easily define and customize experts with specific specialties and security profiles.
*   **Flexible Operation Management:** Define complex workflows and operations with clear input/output specifications.
*   **Dynamic Guardrails:** Pass runtime inputs to guide expert behavior and enforce constraints during deployment.
*   **Secure Communication:** Mechanisms for secure inter-expert communication with context validation.
*   **Comprehensive Security Documentation:** Detailed guides on security profiles, checkpoints, and implementation details.

## Installation

The package is available on PyPI and can be installed with a simple pip command:

```bash
pip install tbh-secure-agents
```

Note that the package name uses hyphens (`tbh-secure-agents`) rather than underscores when installing with pip.

This is a closed-source package with proprietary security implementations. The installation provides you with the necessary interfaces to build secure multi-agent systems without exposing the internal security mechanisms.

## Documentation

Full documentation, including installation instructions, usage guides, and details on the security focus, can be found in the `docs/` directory:

*   **[Installation Guide](./docs/installation.md)**
*   **[Usage Guide](./docs/usage_guide.md)**
*   **[Security Features](./docs/security_features_comprehensive.md)**
*   **[Guardrails Guide](./docs/guardrails_comprehensive.md)**
*   **[Version Changes](./docs/version_changes.md)**

## Examples

The `examples/` directory contains various examples demonstrating the framework's capabilities:

*   **[Guardrails Examples](./examples/guardrails/)**: A collection of examples showing how to use guardrails with varying complexity levels (easy, medium, hard)
*   **[Security Testing](./examples/security_testing/)**: Examples of security testing and validation
*   **[Main Example](./examples/main_example/)**: A comprehensive example showing the core functionality

## Getting Started (Quick Example)

Here's a simple example of how to use the package:

```python
from tbh_secure_agents import Expert, Operation, Squad

# Define experts with specific specialties and security contexts
security_researcher = Expert(
    specialty='Security Researcher',
    objective='Identify vulnerabilities',
    background='Experienced in security analysis',
    security_profile='high_security'
)

reporting_expert = Expert(
    specialty='Technical Writer',
    objective='Summarize findings securely',
    background='Specializes in clear technical documentation',
    security_profile='medium_security'
)

# Define operations
research_operation = Operation(
    instructions='Analyze system X for security flaws',
    output_format='A detailed analysis with vulnerability findings',
    expert=security_researcher
)

reporting_operation = Operation(
    instructions='Compile a secure report of findings',
    output_format='A concise executive summary with key vulnerabilities',
    expert=reporting_expert
)

# Form a squad
security_squad = Squad(
    experts=[security_researcher, reporting_expert],
    operations=[research_operation, reporting_operation],
    process='sequential'  # Operations run in sequence, passing results as context
)

# Define guardrail inputs (dynamic constraints and parameters)
guardrails = {
    "scope": "network infrastructure only",
    "compliance_framework": "NIST",
    "max_findings": 5,
    "priority_level": "critical"
}

# Deploy the squad with guardrails
result = security_squad.deploy(guardrails=guardrails)

print(result)  # Securely handled output
```

## Contributing

Contributions are welcome! Please see the `CONTRIBUTING.md` file (to be created) and refer to the documentation in the `docs/` directory for project structure and goals.

## License

This project is licensed under the Apache License 2.0 - see the `LICENSE` file for details.

## Contact

TBH.AI
Saish - saish.shinde.jb@gmail.com
