#!/usr/bin/env python3
"""
Modified Main Example for TBH Secure Agents

This example demonstrates how to use the TBH Secure Agents package to create a secure
multi-agent system that performs a complex task with multiple experts working together.

This version uses a less sensitive topic to avoid triggering security checks.

API Key: Using the provided API key for demonstration purposes only.
"""

import os
import sys
from tbh_secure_agents import Expert, Operation, Squad

# Set the API key for Google Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyAwkWbBba6t9O15Ok0bsxFmBRoFfhokmVA"

def main():
    print("\n" + "="*80)
    print("TBH SECURE AGENTS - MODIFIED MAIN EXAMPLE".center(80))
    print("="*80 + "\n")
    
    print("Creating secure experts with specialized security profiles...\n")
    
    # Create experts with specific security profiles
    research_expert = Expert(
        specialty="Technology Researcher",
        objective="Research and analyze technology trends and best practices",
        background="Expert in technology research with focus on enterprise solutions",
        security_profile="medium_security"
    )
    
    analysis_expert = Expert(
        specialty="Business Analyst",
        objective="Analyze business implications of technology trends",
        background="Specialized in business impact analysis and recommendations",
        security_profile="medium_security"
    )
    
    report_writer = Expert(
        specialty="Technical Writer",
        objective="Create comprehensive reports from technical findings",
        background="Experienced in creating clear, actionable documentation",
        security_profile="medium_security"
    )
    
    print("Defining secure operations with clear instructions and output formats...\n")
    
    # Define operations for the experts
    research_operation = Operation(
        instructions="""
        Research the latest trends in cloud computing for small businesses.
        Focus on:
        1. Popular cloud services for small businesses
        2. Cost considerations
        3. Implementation challenges
        4. Benefits and ROI
        
        Provide factual information without speculation.
        """,
        output_format="A detailed research summary with key findings organized by category",
        expert=research_expert
    )
    
    analysis_operation = Operation(
        instructions="""
        Based on the research findings, analyze how small businesses can best 
        implement cloud solutions.
        
        Consider:
        1. Resource requirements
        2. Training needs
        3. Implementation timeline
        4. Expected benefits
        
        Provide a structured analysis with clear recommendations.
        """,
        output_format="An analysis report with practical recommendations",
        expert=analysis_expert
    )
    
    report_operation = Operation(
        instructions="""
        Create a comprehensive report on cloud computing for small businesses
        based on the research and analysis.
        
        The report should include:
        1. Executive Summary
        2. Cloud Technology Overview
        3. Implementation Considerations
        4. Recommended Approach
        5. Expected Benefits
        
        Format the report in a professional manner suitable for business owners.
        """,
        output_format="A complete business report with all sections properly formatted",
        expert=report_writer
    )
    
    print("Assembling secure squad with multiple experts and sequential operations...\n")
    
    # Create a squad with the experts and operations
    business_squad = Squad(
        experts=[research_expert, analysis_expert, report_writer],
        operations=[research_operation, analysis_operation, report_operation],
        process="sequential"  # Operations run in sequence, passing results as context
    )
    
    print("Deploying squad with security controls and monitoring...\n")
    
    # Deploy the squad and get the final result
    try:
        result = business_squad.deploy()
        
        print("\n" + "="*80)
        print("FINAL BUSINESS REPORT".center(80))
        print("="*80 + "\n")
        print(result)
        print("\n" + "="*80)
        
        return True
    except Exception as e:
        print(f"Error during squad deployment: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
