#!/usr/bin/env python3
"""
Comprehensive Example for TBH Secure Agents

This example demonstrates the key features of the TBH Secure Agents framework:
1. Creating experts with different security profiles
2. Defining operations with clear instructions
3. Using guardrails to dynamically control expert behavior
4. Implementing security controls throughout the process
5. Forming a squad with sequential operations

The example creates a security assessment team that:
1. Analyzes a system for security vulnerabilities
2. Develops mitigation strategies
3. Creates a comprehensive security report

This example is designed to be easy to execute and understand.
"""

import os
import sys
import logging
import json
from datetime import datetime

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the TBH Secure Agents framework
from tbh_secure_agents import Expert, Operation, Squad

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    """
    Main function demonstrating a comprehensive example of TBH Secure Agents.
    """
    print("\n" + "="*80)
    print("TBH SECURE AGENTS - COMPREHENSIVE EXAMPLE".center(80))
    print("="*80 + "\n")

    # Set your API key
    # You can also set this as an environment variable: GOOGLE_API_KEY
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        print("Please set your GOOGLE_API_KEY environment variable.")
        return False

    print("STEP 1: Creating experts with different security profiles...\n")

    # Create a security analyst with high security profile
    security_analyst = Expert(
        specialty="Security Analyst specializing in {system_type} systems",
        objective="Identify and analyze security vulnerabilities in {system_type} environments",
        background="You have extensive experience in security assessment with expertise in {security_domain}.",
        security_profile="high_security",  # High security profile to prevent data leakage
        api_key=api_key
    )

    # Create a security architect with medium security profile
    security_architect = Expert(
        specialty="Security Architect with focus on {architecture_type} architectures",
        objective="Design secure solutions and mitigation strategies for {system_type} systems",
        background="You have deep knowledge of security frameworks and best practices for {industry} organizations.",
        security_profile="medium_security",  # Medium security for design recommendations
        api_key=api_key
    )

    # Create a technical writer with PII protection profile
    technical_writer = Expert(
        specialty="Technical Writer specializing in security documentation",
        objective="Create clear, comprehensive security reports for {audience_type} audiences",
        background="You excel at translating technical security findings into actionable documentation.",
        security_profile="pii_protection",  # PII protection to prevent sensitive data in reports
        api_key=api_key
    )

    print("STEP 2: Defining operations with template variables...\n")

    # Define a vulnerability assessment operation
    vulnerability_assessment = Operation(
        instructions="""
        Conduct a comprehensive security assessment of a {system_type} system in the {industry} sector.
        
        {assessment_scope, select,
          network:Focus on network security aspects including perimeter security, segmentation, and traffic analysis.|
          application:Focus on application security including input validation, authentication, and session management.|
          infrastructure:Focus on infrastructure security including servers, cloud resources, and configuration.|
          comprehensive:Perform a comprehensive assessment covering all security aspects.
        }
        
        Consider the following threat actors:
        {threat_actors}
        
        Security classification: {security_classification}
        
        Your assessment should identify:
        1. Critical vulnerabilities that could be exploited
        2. Security gaps in the current implementation
        3. Compliance issues with {compliance_framework} requirements
        4. Risk levels for each identified vulnerability
        
        Provide a structured assessment with clear categories and severity ratings.
        """,
        output_format="A detailed vulnerability assessment report with findings categorized by severity",
        expert=security_analyst
    )

    # Define a mitigation strategy operation
    mitigation_strategy = Operation(
        instructions="""
        Based on the vulnerability assessment, develop mitigation strategies to address the identified security issues.
        
        {strategy_type, select,
          tactical:Focus on immediate tactical solutions that can be implemented quickly.|
          strategic:Focus on long-term strategic solutions that address root causes.|
          balanced:Provide a balanced approach with both immediate and long-term solutions.
        }
        
        {resource_constraints, select,
          limited:Consider significant resource constraints in your recommendations.|
          moderate:Consider moderate resource availability for security improvements.|
          ample:Assume resources are available for comprehensive security enhancements.
        }
        
        Your mitigation strategies should:
        1. Address all critical and high vulnerabilities identified
        2. Align with {compliance_framework} requirements
        3. Consider the organization's {industry} context
        4. Provide clear implementation guidance
        
        Prioritize recommendations based on:
        - Risk reduction potential
        - Implementation complexity
        - Resource requirements
        - Time to implement
        """,
        output_format="A structured mitigation strategy document with prioritized recommendations",
        expert=security_architect
    )

    # Define a security report operation
    security_report = Operation(
        instructions="""
        Create a comprehensive security report based on the vulnerability assessment and mitigation strategies.
        
        {report_type, select,
          executive:Create an executive summary suitable for senior leadership.|
          technical:Create a detailed technical report for security professionals.|
          compliance:Focus on compliance aspects for regulatory purposes.|
          comprehensive:Create a complete report with both executive and technical sections.
        }
        
        The report should be tailored for {audience_type} audience and include:
        
        1. Executive Summary
        2. Assessment Methodology
        3. Key Findings
        4. Detailed Vulnerabilities
        5. Recommended Mitigations
        6. Implementation Roadmap
        7. Conclusion
        
        {include_appendices, select,
          true:Include technical appendices with detailed evidence and findings.|
          false:Omit technical appendices.
        }
        
        Format the report professionally and ensure it is actionable for the {audience_type} audience.
        """,
        output_format="A professional security report formatted according to industry standards",
        expert=technical_writer
    )

    print("STEP 3: Creating a squad with security controls...\n")

    # Create a squad with the experts and operations
    security_squad = Squad(
        experts=[security_analyst, security_architect, technical_writer],
        operations=[vulnerability_assessment, mitigation_strategy, security_report],
        process="sequential",  # Operations run in sequence
        security_level="high"  # High security level for the squad
    )

    print("STEP 4: Defining guardrail inputs...\n")

    # Define guardrail inputs
    guardrail_inputs = {
        # System and environment parameters
        "system_type": "cloud-based healthcare",
        "architecture_type": "multi-tier",
        "security_domain": "data protection and compliance",
        "industry": "healthcare",
        
        # Assessment parameters
        "assessment_scope": "comprehensive",
        "threat_actors": [
            "Sophisticated cybercriminal groups targeting patient data",
            "Nation-state actors interested in research data",
            "Insider threats from employees with access to sensitive information"
        ],
        "security_classification": "confidential",
        "compliance_framework": "HIPAA",
        
        # Strategy parameters
        "strategy_type": "balanced",
        "resource_constraints": "moderate",
        
        # Report parameters
        "report_type": "comprehensive",
        "audience_type": "mixed technical and management",
        "include_appendices": "true"
    }

    print("Guardrail inputs defined. Here are some key parameters:")
    print(f"  - System type: {guardrail_inputs['system_type']}")
    print(f"  - Industry: {guardrail_inputs['industry']}")
    print(f"  - Assessment scope: {guardrail_inputs['assessment_scope']}")
    print(f"  - Compliance framework: {guardrail_inputs['compliance_framework']}")
    print(f"  - Report type: {guardrail_inputs['report_type']}")

    print("\nSTEP 5: Deploying the squad with guardrails...\n")

    # Deploy the squad with the guardrail inputs
    try:
        result = security_squad.deploy(guardrails=guardrail_inputs)

        print("\n" + "="*80)
        print("FINAL SECURITY REPORT".center(80))
        print("="*80 + "\n")
        print(result)
        print("\n" + "="*80)

        # Save the output to a file
        output_file = os.path.join(os.path.dirname(__file__), "comprehensive_example_output.txt")
        with open(output_file, "w") as f:
            f.write("TBH SECURE AGENTS - COMPREHENSIVE EXAMPLE\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("Guardrail inputs (selected):\n")
            for key in ["system_type", "industry", "assessment_scope", "compliance_framework", "report_type"]:
                f.write(f"  - {key}: {guardrail_inputs[key]}\n")
            f.write("\nResult:\n\n")
            f.write(result)
        
        print(f"\nOutput saved to {output_file}")
        return True

    except Exception as e:
        print(f"Error during squad deployment: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
