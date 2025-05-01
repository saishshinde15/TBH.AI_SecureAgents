#!/usr/bin/env python3
"""
Main Example for TBH Secure Agents

This example demonstrates how to use the TBH Secure Agents package to create a secure
multi-agent system that performs a complex task with multiple experts working together.

The example creates a squad of experts to:
1. Research information about a cybersecurity topic
2. Analyze vulnerabilities in a system
3. Generate a comprehensive security report
"""

import os
import sys
import logging

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the TBH Secure Agents framework
from tbh_secure_agents import Expert, Operation, Squad

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    print("\n" + "="*80)
    print("TBH SECURE AGENTS - MAIN EXAMPLE".center(80))
    print("="*80 + "\n")

    # Set your API key
    # You can also set this as an environment variable: GOOGLE_API_KEY
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        print("Please set your GOOGLE_API_KEY environment variable.")
        return False

    print("Creating secure experts with specialized security profiles...\n")

    # Create experts with specific security profiles
    security_researcher = Expert(
        specialty="Security Researcher",
        objective="Research and analyze cybersecurity threats and vulnerabilities",
        background="Expert in identifying and documenting security issues with 10+ years of experience",
        security_profile="high_security",  # High security profile to prevent data leakage
        api_key=api_key
    )

    vulnerability_analyst = Expert(
        specialty="Vulnerability Analyst",
        objective="Identify and assess security vulnerabilities in systems",
        background="Specialized in penetration testing and vulnerability assessment",
        security_profile="medium_security",
        api_key=api_key
    )

    security_report_writer = Expert(
        specialty="Technical Documentation Specialist",
        objective="Create comprehensive security reports from technical findings",
        background="Experienced in creating clear, actionable security documentation",
        security_profile="high_security",  # High security profile for report generation
        api_key=api_key
    )

    print("Defining secure operations with clear instructions and output formats...\n")

    # Define operations for the experts
    research_operation = Operation(
        instructions="""
        Research the latest trends in ransomware attacks targeting healthcare organizations.
        Focus on:
        1. Recent major incidents (last 2 years)
        2. Common attack vectors
        3. Types of data typically targeted
        4. Estimated financial impact

        Provide factual information without speculation.
        """,
        output_format="A detailed research summary with key findings organized by category",
        expert=security_researcher
    )

    analysis_operation = Operation(
        instructions="""
        Based on the research findings, analyze potential vulnerabilities in a typical
        healthcare organization's IT infrastructure that could be exploited by ransomware.

        Consider:
        1. Network security weaknesses
        2. Employee training gaps
        3. Data backup vulnerabilities
        4. Access control issues

        Provide a structured analysis with clear vulnerability categories.
        """,
        output_format="A vulnerability analysis with severity ratings and potential impact",
        expert=vulnerability_analyst
    )

    report_operation = Operation(
        instructions="""
        Create a comprehensive security report based on the research and vulnerability analysis.
        The report should include:

        1. Executive Summary
        2. Threat Landscape Overview
        3. Vulnerability Assessment
        4. Recommended Security Measures
        5. Implementation Priorities

        Format the report in a professional manner suitable for executive review.
        """,
        output_format="A complete security report with all sections properly formatted",
        expert=security_report_writer
    )

    print("Assembling secure squad with multiple experts and sequential operations...\n")

    # Create a squad with the experts and operations
    security_squad = Squad(
        experts=[security_researcher, vulnerability_analyst, security_report_writer],
        operations=[research_operation, analysis_operation, report_operation],
        process="sequential"  # Operations run in sequence, passing results as context
    )

    print("Deploying squad with security controls and monitoring...\n")

    # Deploy the squad and get the final result
    try:
        result = security_squad.deploy()

        print("\n" + "="*80)
        print("FINAL SECURITY REPORT".center(80))
        print("="*80 + "\n")
        print(result)
        print("\n" + "="*80)

        # Save the output to a file
        output_file = os.path.join(os.path.dirname(__file__), "main_example_output.txt")
        with open(output_file, "w") as f:
            f.write("TBH SECURE AGENTS - MAIN EXAMPLE\n\n")
            f.write("This example demonstrates basic security profiles without guardrails.\n\n")
            f.write("Result:\n\n")
            f.write(result)

        print(f"\nOutput saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error during squad deployment: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
