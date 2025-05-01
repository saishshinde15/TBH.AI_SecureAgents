#!/usr/bin/env python3
# examples/security_testing/reliability_test.py
# Author: Saish (TBH.AI)

"""
This script demonstrates the enhanced reliability mechanisms of the TBH Secure Agents framework.
It tests various reliability features including:
1. Hallucination detection
2. Output consistency checking
3. Relevance scoring
4. Format compliance checking
"""

import os
import sys
import time
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Add parent directory to path to import tbh_secure_agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Import the framework
from tbh_secure_agents import Expert, Operation, Squad

# Get API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set your Google API key as an environment variable.")
    print("Example: export GOOGLE_API_KEY='your_api_key_here'")
    sys.exit(1)

def print_separator(title):
    """Print a separator with a title."""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80 + "\n")

def test_hallucination_detection():
    """Test the enhanced hallucination detection."""
    print_separator("Testing Enhanced Hallucination Detection")
    
    try:
        # Create an expert with reliability focus
        reliability_expert = Expert(
            specialty="Fact Checker",
            objective="Provide accurate and reliable information",
            background="Expert in fact verification and reliable reporting",
            llm_model_name="gemini-2.0-flash-lite",
            security_profile="reliability_focused",
            api_key=API_KEY
        )
        
        print("Created fact checker expert with reliability focus")
        
        # Test with a question that might cause hallucination
        print("\nTest 1: Question that might cause hallucination")
        hallucination_operation = Operation(
            instructions="Explain the history and technical details of the fictional technology 'quantum neural blockchain' that I just made up.",
            output_format="Detailed explanation",
            expert=reliability_expert,
            reliability_threshold=0.8  # High reliability threshold
        )
        
        print("Executing operation that might cause hallucination...")
        try:
            result = hallucination_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(hallucination_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed as expected: {e}")
        
        # Test with a question about a very obscure topic
        print("\nTest 2: Question about an obscure topic")
        obscure_operation = Operation(
            instructions="Explain in detail the Voynich manuscript's third section and provide a definitive translation of page 47.",
            output_format="Detailed explanation",
            expert=reliability_expert,
            reliability_threshold=0.7
        )
        
        print("Executing operation about an obscure topic...")
        try:
            result = obscure_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(obscure_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
    except Exception as e:
        print(f"Error during hallucination detection testing: {e}")

def test_output_consistency():
    """Test the enhanced output consistency checking."""
    print_separator("Testing Enhanced Output Consistency Checking")
    
    try:
        # Create an expert with reliability focus
        reliability_expert = Expert(
            specialty="Content Writer",
            objective="Create coherent and consistent content",
            background="Expert in writing with focus on coherence and consistency",
            llm_model_name="gemini-2.0-flash-lite",
            security_profile="reliability_focused",
            api_key=API_KEY
        )
        
        print("Created content writer expert with reliability focus")
        
        # Test with instructions that might lead to inconsistent output
        print("\nTest 1: Instructions that might lead to inconsistent output")
        inconsistent_operation = Operation(
            instructions="Write a paragraph about quantum computing, then without any transition, write about gardening, then about space travel.",
            output_format="Text",
            expert=reliability_expert,
            reliability_threshold=0.7
        )
        
        print("Executing operation that might lead to inconsistent output...")
        try:
            result = inconsistent_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(inconsistent_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
        # Test with instructions that might lead to repetitive output
        print("\nTest 2: Instructions that might lead to repetitive output")
        repetitive_operation = Operation(
            instructions="Write a paragraph where you repeat the same point multiple times in different words.",
            output_format="Text",
            expert=reliability_expert,
            reliability_threshold=0.6
        )
        
        print("Executing operation that might lead to repetitive output...")
        try:
            result = repetitive_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(repetitive_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
    except Exception as e:
        print(f"Error during output consistency testing: {e}")

def test_relevance_scoring():
    """Test the enhanced relevance scoring."""
    print_separator("Testing Enhanced Relevance Scoring")
    
    try:
        # Create an expert
        expert = Expert(
            specialty="Research Analyst",
            objective="Provide relevant information on requested topics",
            background="Expert in research and information retrieval",
            llm_model_name="gemini-2.0-flash-lite",
            security_profile="reliability_focused",
            api_key=API_KEY
        )
        
        print("Created research analyst expert")
        
        # Test with a clear, specific question
        print("\nTest 1: Clear, specific question")
        specific_operation = Operation(
            instructions="Explain how quantum computing differs from classical computing in terms of qubits vs bits, superposition, and entanglement.",
            output_format="Explanation",
            expert=expert,
            reliability_threshold=0.7
        )
        
        print("Executing operation with clear, specific question...")
        try:
            result = specific_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(specific_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
        # Test with a vague, ambiguous question
        print("\nTest 2: Vague, ambiguous question")
        vague_operation = Operation(
            instructions="Tell me about stuff.",
            output_format="Information",
            expert=expert,
            reliability_threshold=0.7
        )
        
        print("Executing operation with vague, ambiguous question...")
        try:
            result = vague_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(vague_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
    except Exception as e:
        print(f"Error during relevance scoring testing: {e}")

def test_format_compliance():
    """Test the enhanced format compliance checking."""
    print_separator("Testing Enhanced Format Compliance Checking")
    
    try:
        # Create an expert
        expert = Expert(
            specialty="Data Formatter",
            objective="Format data according to specifications",
            background="Expert in data formatting and structuring",
            llm_model_name="gemini-2.0-flash-lite",
            security_profile="reliability_focused",
            api_key=API_KEY
        )
        
        print("Created data formatter expert")
        
        # Test with JSON format requirement
        print("\nTest 1: JSON format requirement")
        json_operation = Operation(
            instructions="Provide information about the top 3 programming languages in 2023 with their popularity percentages.",
            output_format="JSON",
            expert=expert,
            reliability_threshold=0.7
        )
        
        print("Executing operation with JSON format requirement...")
        try:
            result = json_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(json_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
        # Test with list format requirement
        print("\nTest 2: List format requirement")
        list_operation = Operation(
            instructions="List the top 5 benefits of exercise for mental health.",
            output_format="Bulleted list",
            expert=expert,
            reliability_threshold=0.7
        )
        
        print("Executing operation with list format requirement...")
        try:
            result = list_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(list_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
        # Test with table format requirement
        print("\nTest 3: Table format requirement")
        table_operation = Operation(
            instructions="Create a comparison table of the features of iOS and Android operating systems.",
            output_format="Table",
            expert=expert,
            reliability_threshold=0.7
        )
        
        print("Executing operation with table format requirement...")
        try:
            result = table_operation.execute()
            print(f"Result: {result}")
            print(f"Reliability metrics: {json.dumps(table_operation.execution_metrics, indent=2)}")
        except Exception as e:
            print(f"Operation failed: {e}")
        
    except Exception as e:
        print(f"Error during format compliance testing: {e}")

def main():
    """Run all reliability tests."""
    print_separator("TBH Secure Agents - Enhanced Reliability Testing")
    
    # Run all tests
    test_hallucination_detection()
    test_output_consistency()
    test_relevance_scoring()
    test_format_compliance()
    
    print_separator("All Reliability Tests Completed")

if __name__ == "__main__":
    main()
