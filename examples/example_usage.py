#!/usr/bin/env python3
"""
Example usage of the TBH Secure Agents package.

This script demonstrates how to use the TBH Secure Agents package to create
a simple multi-agent system with security controls.

To run this script:
1. Install the package: pip install tbh-secure-agents
2. Set your Google API key: export GOOGLE_API_KEY="your_api_key_here"
3. Run the script: python example_usage.py
"""

import os
from tbh_secure_agents import Expert, Operation, Squad

# Set your Google API key
# You can also set this as an environment variable before running the script
os.environ["GOOGLE_API_KEY"] = "AIzaSyAwkWbBba6t9O15Ok0bsxFmBRoFfhokmVA"

def main():
    print("\n" + "="*80)
    print("TBH SECURE AGENTS - EXAMPLE USAGE".center(80))
    print("="*80 + "\n")
    
    print("Creating experts with security profiles...\n")
    
    # Create experts with specific security profiles
    research_expert = Expert(
        specialty="Technology Researcher",
        objective="Research and analyze technology trends",
        background="Expert in technology research with focus on enterprise solutions",
        security_profile="medium_security"
    )
    
    analysis_expert = Expert(
        specialty="Business Analyst",
        objective="Analyze business implications of technology trends",
        background="Specialized in business impact analysis",
        security_profile="medium_security"
    )
    
    print("Defining operations with clear instructions...\n")
    
    # Define operations for the experts
    research_operation = Operation(
        instructions="""
        Research the latest trends in cloud computing for small businesses.
        Focus on:
        1. Popular cloud services
        2. Cost considerations
        3. Implementation challenges
        """,
        output_format="A detailed research summary with key findings",
        expert=research_expert
    )
    
    analysis_operation = Operation(
        instructions="""
        Based on the research findings, analyze how small businesses can
        implement cloud solutions effectively.
        """,
        output_format="An analysis report with recommendations",
        expert=analysis_expert
    )
    
    print("Creating a squad with the experts and operations...\n")
    
    # Create a squad with the experts and operations
    business_squad = Squad(
        experts=[research_expert, analysis_expert],
        operations=[research_operation, analysis_operation],
        process="sequential"  # Operations run in sequence
    )
    
    print("Deploying the squad...\n")
    
    # Deploy the squad and get the final result
    try:
        result = business_squad.deploy()
        
        print("\n" + "="*80)
        print("FINAL REPORT".center(80))
        print("="*80 + "\n")
        print(result)
        print("\n" + "="*80)
        
    except Exception as e:
        print(f"Error during squad deployment: {e}")

if __name__ == "__main__":
    main()
