# TBH Secure Agents Examples

<img width="618" alt="Main" src="https://github.com/user-attachments/assets/dbbf5a4f-7b0b-4f43-9b37-ef77dc761ff1" />

This directory contains examples demonstrating various features and capabilities of the TBH Secure Agents framework. These examples are designed to help you understand how to use the framework effectively and securely.

## Example Categories

### [Guardrails Examples](./guardrails/)

A collection of examples demonstrating the guardrails feature with varying complexity levels:

- **Easy**: Simple examples with basic template variables
- **Medium**: More complex examples with conditional formatting
- **Hard**: Advanced examples with nested conditional logic and complex data structures
- **Security-focused**: Examples showing how to use guardrails to implement dynamic security controls

Each example includes both the code and the output, making it easy to see how guardrails affect the results.

### [Security Testing](./security_testing/)

Examples demonstrating how to test and validate the security features of the framework:

- Basic security testing
- Enhanced security testing
- Multi-agent security testing
- Reliability testing

These examples show how to verify that your multi-agent systems are secure and reliable.

### [Main Example](./main_example/)

A comprehensive example demonstrating the core functionality of the framework, including:

- Creating experts with different specialties
- Defining operations with specific instructions
- Forming squads to execute operations
- Deploying squads with guardrails

### Other Examples

- **Code Security Review**: Example of using the framework to perform a security code review
- **Flask App Generation**: Example of generating a Flask application
- **Information Extraction**: Example of extracting structured information from text
- **Security Vulnerability Summary**: Example of summarizing security vulnerabilities
- **Story Concept Marketing**: Example of generating marketing content for a story concept

## Running the Examples

To run any of these examples, make sure you have set your Google API key as an environment variable:

```bash
export GOOGLE_API_KEY=your_api_key_here
```

Then run the example:

```bash
python examples/guardrails/easy_guardrails.py
```

## Creating Your Own Examples

Feel free to modify these examples or create your own to explore the capabilities of the TBH Secure Agents framework. The examples are designed to be educational and to demonstrate best practices for secure multi-agent systems.
