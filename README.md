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
*   **Result Destination:** Save operation and squad results to files in various formats (TXT, MD, HTML, JSON, CSV, PDF).
*   **Comprehensive Security Documentation:** Detailed guides on security profiles, checkpoints, and implementation details.

## Installation

The package is available on PyPI and can be installed with a simple pip command:

```bash
pip install tbh-secure-agents
```

Note that the package name uses hyphens (`tbh-secure-agents`) rather than underscores when installing with pip.

This package is licensed under the Apache License 2.0 with a custom addendum. While the code is open source, it includes specialized security implementations designed to protect multi-agent systems. The package provides you with the necessary interfaces and components to build secure multi-agent systems.

## Project Structure

The TBH Secure Agents framework is organized into the following directories:

* **`tbh_secure_agents/`**: Core package code
  * **`security/`**: Security-related components
  * **`security_validation/`**: Security validation system
  * **`security_profiles/`**: Security profile definitions and management

* **`docs/`**: Comprehensive documentation
  * **[Installation Guide](./docs/installation.md)**
  * **[Usage Guide](./docs/usage_guide.md)**
  * **[Security Features](./docs/security_features_comprehensive.md)**
  * **[Guardrails Guide](./docs/guardrails_comprehensive.md)**
  * **[Result Destination Guide](./docs/result_destination.md)**
  * **[Error Messages Guide](./docs/error_messages_guide.md)**
  * **[Security Profiles Guide](./docs/security_profiles_guide.md)**
  * **[Version Changes](./docs/version_changes.md)**
  * **[Word Documentation](./docs/word_docs/)**: Microsoft Word versions of all documentation

* **`examples/`**: Example code demonstrating framework usage
  * **[Basic Examples](./examples/basic/)**: Simple examples demonstrating core functionality
  * **[Advanced Examples](./examples/advanced/)**: More complex examples showcasing advanced features
  * **[Security Examples](./examples/security/)**: Examples focused on security features
  * **[Result Destination Examples](./examples/result_destination/)**: Examples demonstrating the result_destination feature
  * **[Guardrails Examples](./examples/guardrails/)**: Examples showing how to use guardrails

* **`tests/`**: Comprehensive test suite
  * Unit tests, integration tests, and security validation tests

* **`scripts/`**: Utility scripts for development and maintenance
  * Build scripts, update scripts, and other utilities

* **`outputs/`**: Directory for generated outputs (not included in repository)
  * Generated reports, visualizations, and test results

## Getting Started (Quick Example)

Here's a simple example of how to use the package:

```python
from tbh_secure_agents import Expert, Operation, Squad
import os

# Create outputs directory
os.makedirs("outputs/examples", exist_ok=True)

# Define experts with specific specialties and security profiles
content_writer = Expert(
    specialty="Content Writer",
    objective="Create engaging and informative content",
    background="Experienced in creating clear, concise, and engaging content.",
    security_profile="minimal"  # Using minimal security for simplicity
)

data_analyst = Expert(
    specialty="Data Analyst",
    objective="Analyze data and provide insights",
    background="Skilled in interpreting data and extracting meaningful insights.",
    security_profile="minimal"  # Using minimal security for simplicity
)

# Define operations with result destinations
content_operation = Operation(
    instructions="Write a short blog post about the benefits of artificial intelligence in healthcare.",
    output_format="A well-structured blog post with a title, introduction, main points, and conclusion.",
    expert=content_writer,
    result_destination="outputs/examples/healthcare_ai_blog.md"  # Save result to a markdown file
)

analysis_operation = Operation(
    instructions="Analyze the following data and provide insights: Patient wait times decreased by 30% after implementing AI scheduling. Diagnostic accuracy improved by 15%. Treatment planning time reduced by 25%.",
    output_format="A concise analysis with key insights and recommendations.",
    expert=data_analyst,
    result_destination="outputs/examples/healthcare_data_analysis.txt"  # Save result to a text file
)

# Create a squad with template variables in operations
template_expert = Expert(
    specialty="Healthcare Specialist",
    objective="Provide {output_type} about healthcare technology",
    background="Expert in healthcare technology with a focus on {focus_area}.",
    security_profile="minimal"  # Using minimal security for simplicity
)

# Create an operation with template variables and conditional formatting
template_operation = Operation(
    instructions="""
    Write a {length} summary about {topic} in healthcare.

    {tone, select,
      formal:Use a professional, academic tone suitable for medical professionals.|
      conversational:Use a friendly, approachable tone suitable for patients and the general public.|
      technical:Use precise technical language appropriate for healthcare IT specialists.
    }

    {include_statistics, select,
      true:Include relevant statistics and data points to support your summary.|
      false:Focus on qualitative information without specific statistics.
    }
    """,
    expert=template_expert,
    result_destination="outputs/examples/healthcare_summary.html"  # Save result to an HTML file
)

# Form a squad with result destination
healthcare_squad = Squad(
    experts=[content_writer, data_analyst, template_expert],
    operations=[content_operation, analysis_operation, template_operation],
    process="sequential",  # Operations run in sequence, passing results as context
    result_destination={
        "format": "json",
        "file_path": "outputs/examples/healthcare_squad_result.json"  # Save squad result to a JSON file
    }
)

# Define guardrail inputs
guardrails = {
    "output_type": "insights",
    "focus_area": "AI implementation",
    "length": "one-page",
    "topic": "artificial intelligence",
    "tone": "conversational",
    "include_statistics": "true"
}

# Deploy the squad with guardrails
result = healthcare_squad.deploy(guardrails=guardrails)

print("Squad result:", result[:100] + "...")  # Print a preview of the result
print("Results saved to the outputs/examples directory")
```

## Contributing

Contributions are welcome! Please see the `CONTRIBUTING.md` file and follow these guidelines:

1. **Code Organization**:
   - Core package code goes in `tbh_secure_agents/`
   - Tests go in `tests/`
   - Examples go in `examples/`
   - Documentation goes in `docs/`
   - Utility scripts go in `scripts/`
   - Generated outputs go in `outputs/` (not committed to repository)

2. **Development Workflow**:
   - Create a feature branch from `main`
   - Write tests for new features
   - Ensure all tests pass before submitting a pull request
   - Update documentation as needed

3. **Security Focus**:
   - All contributions must maintain or enhance the security focus of the framework
   - Follow security best practices in all code
   - Document security implications of new features

For more details, refer to the documentation in the `docs/` directory for project structure and goals.

## License

This project is licensed under the Apache License 2.0 - see the `LICENSE` file for details.

The Apache License 2.0 was chosen to provide a balance between open-source accessibility and protection for contributors. It allows for free use, modification, and distribution while requiring preservation of copyright and license notices. It also provides an express grant of patent rights from contributors to users.

## Contact

TBH.AI
Saish - saish.shinde.jb@gmail.com
