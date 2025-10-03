from typing import List, Dict, Optional

class InterviewerAgent:
    """Agent that conducts interviews to gather website requirements."""
    
    def __init__(self):
        self.questions = [
            {
                'id': 'purpose',
                'question': 'What is the primary purpose of your website?',
                'examples': ['E-commerce', 'Portfolio', 'Blog', 'Business landing page', 'SaaS product', 'Other']
            },
            {
                'id': 'target_audience',
                'question': 'Who is your target audience?',
                'examples': ['General public', 'Professionals', 'Students', 'Specific industry', 'Age group']
            },
            {
                'id': 'key_features',
                'question': 'What are the key features you need?',
                'examples': ['User authentication', 'Payment processing', 'Content management', 'Search functionality', 'Social media integration', 'Analytics']
            },
            {
                'id': 'design_preferences',
                'question': 'What design style do you prefer?',
                'examples': ['Modern/Minimalist', 'Bold/Colorful', 'Corporate/Professional', 'Creative/Artistic', 'Dark mode', 'Light mode']
            },
            {
                'id': 'content_type',
                'question': 'What type of content will you be displaying?',
                'examples': ['Text articles', 'Images/Gallery', 'Videos', 'Products', 'Services', 'Documentation']
            },
            {
                'id': 'user_interactions',
                'question': 'How should users interact with your site?',
                'examples': ['Browse content', 'Make purchases', 'Submit forms', 'Create accounts', 'Leave comments', 'Book appointments']
            },
            {
                'id': 'mobile_priority',
                'question': 'Is mobile responsiveness a priority?',
                'examples': ['Critical', 'Important', 'Nice to have', 'Desktop-first']
            },
            {
                'id': 'integrations',
                'question': 'Do you need any third-party integrations?',
                'examples': ['Google Analytics', 'Email marketing', 'CRM', 'Payment gateways', 'Social media', 'APIs']
            },
            {
                'id': 'budget_timeline',
                'question': 'What is your budget and timeline?',
                'examples': ['Small budget/Quick launch', 'Medium budget/Standard timeline', 'Large budget/Comprehensive development']
            },
            {
                'id': 'success_metrics',
                'question': 'How will you measure success?',
                'examples': ['User engagement', 'Conversion rates', 'Traffic volume', 'Sales/Revenue', 'User retention', 'Brand awareness']
            }
        ]
        self.responses = {}
        self.current_question_index = 0
    
    def get_next_question(self) -> Optional[Dict]:
        """Get the next question in the interview sequence."""
        if self.current_question_index >= len(self.questions):
            return None
        return self.questions[self.current_question_index]
    
    def record_response(self, question_id: str, response: str) -> None:
        """Record a user's response to a question."""
        self.responses[question_id] = response
        self.current_question_index += 1
    
    def get_progress(self) -> Dict:
        """Get the current progress of the interview."""
        return {
            'completed': self.current_question_index,
            'total': len(self.questions),
            'percentage': (self.current_question_index / len(self.questions)) * 100
        }
    
    def generate_requirements_document(self) -> Dict:
        """Generate a structured requirements document based on responses."""
        if not self.responses:
            return {'error': 'No responses recorded yet'}
        
        requirements = {
            'project_overview': {
                'purpose': self.responses.get('purpose', 'Not specified'),
                'target_audience': self.responses.get('target_audience', 'Not specified'),
                'success_metrics': self.responses.get('success_metrics', 'Not specified')
            },
            'functional_requirements': {
                'key_features': self.responses.get('key_features', 'Not specified'),
                'user_interactions': self.responses.get('user_interactions', 'Not specified'),
                'integrations': self.responses.get('integrations', 'Not specified')
            },
            'design_requirements': {
                'style': self.responses.get('design_preferences', 'Not specified'),
                'mobile_priority': self.responses.get('mobile_priority', 'Not specified'),
                'content_type': self.responses.get('content_type', 'Not specified')
            },
            'project_constraints': {
                'budget_timeline': self.responses.get('budget_timeline', 'Not specified')
            },
            'recommendations': self._generate_recommendations()
        }
        
        return requirements
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on the responses."""
        recommendations = []
        
        # Check for purpose-specific recommendations
        purpose = self.responses.get('purpose', '').lower()
        if 'ecommerce' in purpose or 'e-commerce' in purpose:
            recommendations.append('Consider implementing a robust product catalog with search and filtering')
            recommendations.append('Ensure secure payment gateway integration')
            recommendations.append('Implement shopping cart and checkout flow')
        
        if 'saas' in purpose:
            recommendations.append('Focus on user onboarding and trial flow')
            recommendations.append('Implement subscription management')
            recommendations.append('Add comprehensive analytics dashboard')
        
        # Mobile priority recommendations
        mobile = self.responses.get('mobile_priority', '').lower()
        if 'critical' in mobile or 'important' in mobile:
            recommendations.append('Use mobile-first design approach')
            recommendations.append('Optimize images and assets for mobile performance')
            recommendations.append('Implement touch-friendly UI elements')
        
        # Feature-based recommendations
        features = self.responses.get('key_features', '').lower()
        if 'authentication' in features:
            recommendations.append('Implement secure authentication with password hashing')
            recommendations.append('Consider OAuth/social login options')
        
        if 'payment' in features:
            recommendations.append('Use established payment providers (Stripe, PayPal)')
            recommendations.append('Ensure PCI compliance')
        
        if not recommendations:
            recommendations.append('Start with an MVP approach to validate core features')
            recommendations.append('Focus on user experience and ease of navigation')
            recommendations.append('Implement analytics from day one to track user behavior')
        
        return recommendations
    
    def reset_interview(self) -> None:
        """Reset the interview to start over."""
        self.responses = {}
        self.current_question_index = 0
    
    def get_summary(self) -> str:
        """Get a text summary of all responses."""
        if not self.responses:
            return "No responses recorded yet."
        
        summary = "Interview Summary:\n\n"
        for question in self.questions:
            q_id = question['id']
            if q_id in self.responses:
                summary += f"{question['question']}\n"
                summary += f"Answer: {self.responses[q_id]}\n\n"
        
        return summary
