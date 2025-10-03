"""
Test file demonstrating the Interviewer and Marketing Strategy agents working together.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.agents.interviewer import InterviewerAgent
from app.agents.marketing import MarketingStrategyAgent
import json


def test_interviewer_workflow():
    """Test the interviewer agent workflow."""
    print("=" * 80)
    print("TESTING INTERVIEWER AGENT")
    print("=" * 80)
    
    interviewer = InterviewerAgent()
    
    # Simulate answering interview questions
    sample_responses = {
        'purpose': 'E-commerce website for selling handmade crafts',
        'target_audience': 'Creative hobbyists and gift shoppers aged 25-45',
        'key_features': 'User authentication, payment processing, product catalog, search functionality',
        'design_preferences': 'Modern/Minimalist with warm, inviting colors',
        'content_type': 'Product images, descriptions, customer reviews',
        'user_interactions': 'Browse products, add to cart, make purchases, leave reviews',
        'mobile_priority': 'Critical - most users shop on mobile',
        'integrations': 'Google Analytics, Stripe payment gateway, email marketing',
        'budget_timeline': 'Medium budget, 3-month development timeline',
        'success_metrics': 'Conversion rates, sales revenue, customer retention'
    }
    
    # Display questions and record responses
    for question_data in interviewer.questions:
        q_id = question_data['id']
        print(f"\nQuestion: {question_data['question']}")
        print(f"Examples: {', '.join(question_data['examples'])}")
        
        response = sample_responses.get(q_id, 'Not specified')
        print(f"Response: {response}")
        interviewer.record_response(q_id, response)
        
        progress = interviewer.get_progress()
        print(f"Progress: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")
    
    # Generate requirements document
    print("\n" + "=" * 80)
    print("GENERATED REQUIREMENTS DOCUMENT")
    print("=" * 80)
    requirements = interviewer.generate_requirements_document()
    print(json.dumps(requirements, indent=2))
    
    # Get summary
    print("\n" + "=" * 80)
    print("INTERVIEW SUMMARY")
    print("=" * 80)
    print(interviewer.get_summary())
    
    return requirements


def test_marketing_strategy_workflow(requirements):
    """Test the marketing strategy agent workflow."""
    print("\n" + "=" * 80)
    print("TESTING MARKETING STRATEGY AGENT")
    print("=" * 80)
    
    marketing = MarketingStrategyAgent()
    
    # Load requirements from interviewer
    marketing.load_requirements(requirements)
    
    # Generate individual strategy components
    print("\n--- Brand Positioning ---")
    brand_positioning = marketing.generate_brand_positioning()
    print(json.dumps(brand_positioning, indent=2))
    
    print("\n--- Content Strategy ---")
    content_strategy = marketing.generate_content_strategy()
    print(json.dumps(content_strategy, indent=2))
    
    print("\n--- SEO Strategy ---")
    seo_strategy = marketing.generate_seo_strategy()
    print(json.dumps(seo_strategy, indent=2))
    
    print("\n--- Social Media Plan ---")
    social_media = marketing.generate_social_media_plan()
    print(json.dumps(social_media, indent=2))
    
    print("\n--- Email Marketing Strategy ---")
    email_marketing = marketing.generate_email_marketing_strategy()
    print(json.dumps(email_marketing, indent=2))
    
    print("\n--- Paid Advertising Strategy ---")
    paid_ads = marketing.generate_paid_advertising_strategy()
    print(json.dumps(paid_ads, indent=2))
    
    print("\n--- Analytics Plan ---")
    analytics = marketing.generate_analytics_plan()
    print(json.dumps(analytics, indent=2))
    
    # Generate complete strategy
    print("\n" + "=" * 80)
    print("COMPLETE MARKETING STRATEGY")
    print("=" * 80)
    complete_strategy = marketing.generate_complete_strategy()
    
    # Export as document
    print("\n" + "=" * 80)
    print("EXPORTED STRATEGY DOCUMENT")
    print("=" * 80)
    strategy_doc = marketing.export_strategy_document()
    print(strategy_doc)
    
    return complete_strategy


def test_integrated_workflow():
    """Test the complete workflow from interview to marketing strategy."""
    print("\n" + "=" * 80)
    print("INTEGRATED WORKFLOW TEST: INTERVIEW → MARKETING STRATEGY")
    print("=" * 80)
    
    # Step 1: Conduct interview
    print("\n### STEP 1: Conducting Requirements Interview ###")
    requirements = test_interviewer_workflow()
    
    # Step 2: Generate marketing strategy
    print("\n### STEP 2: Generating Marketing Strategy ###")
    strategy = test_marketing_strategy_workflow(requirements)
    
    print("\n" + "=" * 80)
    print("WORKFLOW COMPLETE!")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Review the requirements document")
    print("2. Review the complete marketing strategy")
    print("3. Adjust strategies based on feedback")
    print("4. Begin implementation following the timeline")


if __name__ == '__main__':
    # Run the integrated workflow test
    test_integrated_workflow()
    
    print("\n" + "=" * 80)
    print("All tests completed successfully!")
    print("=" * 80)
