from typing import List, Dict, Optional

class MarketingStrategyAgent:
    """Agent that develops comprehensive marketing strategies for websites."""
    
    def __init__(self):
        self.strategy_components = [
            'brand_positioning',
            'target_market_analysis',
            'content_strategy',
            'seo_strategy',
            'social_media_plan',
            'paid_advertising',
            'email_marketing',
            'analytics_tracking'
        ]
        self.website_requirements = {}
        self.strategy = {}
    
    def load_requirements(self, requirements: Dict) -> None:
        """Load website requirements from the interviewer agent."""
        self.website_requirements = requirements
    
    def generate_brand_positioning(self) -> Dict:
        """Generate brand positioning strategy."""
        purpose = self.website_requirements.get('project_overview', {}).get('purpose', '')
        target_audience = self.website_requirements.get('project_overview', {}).get('target_audience', '')
        
        positioning = {
            'unique_value_proposition': self._generate_uvp(purpose),
            'brand_voice': self._determine_brand_voice(target_audience),
            'key_messaging': self._generate_key_messages(purpose, target_audience),
            'competitive_differentiation': [
                'Focus on unique features that competitors lack',
                'Emphasize superior user experience',
                'Highlight customer success stories and testimonials'
            ]
        }
        
        return positioning
    
    def _generate_uvp(self, purpose: str) -> str:
        """Generate unique value proposition based on purpose."""
        purpose_lower = purpose.lower()
        
        if 'ecommerce' in purpose_lower or 'e-commerce' in purpose_lower:
            return 'Seamless shopping experience with fast checkout and reliable delivery'
        elif 'saas' in purpose_lower:
            return 'Powerful yet intuitive solution that saves time and increases productivity'
        elif 'portfolio' in purpose_lower:
            return 'Showcase your work with stunning visuals and compelling storytelling'
        elif 'blog' in purpose_lower:
            return 'Valuable insights and content that educates and inspires'
        elif 'business' in purpose_lower:
            return 'Professional solutions that drive growth and deliver results'
        else:
            return 'Exceptional quality and user-focused design that exceeds expectations'
    
    def _determine_brand_voice(self, audience: str) -> Dict:
        """Determine appropriate brand voice for target audience."""
        audience_lower = audience.lower()
        
        if 'professional' in audience_lower or 'corporate' in audience_lower:
            return {
                'tone': 'Professional and authoritative',
                'style': 'Clear, concise, and informative',
                'personality': 'Expert, trustworthy, solution-oriented'
            }
        elif 'student' in audience_lower or 'young' in audience_lower:
            return {
                'tone': 'Friendly and approachable',
                'style': 'Conversational and engaging',
                'personality': 'Energetic, helpful, innovative'
            }
        else:
            return {
                'tone': 'Balanced and authentic',
                'style': 'Clear and relatable',
                'personality': 'Trustworthy, helpful, professional'
            }
    
    def _generate_key_messages(self, purpose: str, audience: str) -> List[str]:
        """Generate key marketing messages."""
        messages = [
            f'Designed specifically for {audience}',
            'User-friendly and intuitive interface',
            'Reliable and secure platform'
        ]
        
        purpose_lower = purpose.lower()
        if 'ecommerce' in purpose_lower:
            messages.append('Fast and secure transactions')
            messages.append('Wide selection and competitive prices')
        elif 'saas' in purpose_lower:
            messages.append('Scalable solution that grows with you')
            messages.append('Comprehensive features at competitive pricing')
        
        return messages
    
    def generate_content_strategy(self) -> Dict:
        """Generate content marketing strategy."""
        content_type = self.website_requirements.get('design_requirements', {}).get('content_type', '')
        
        strategy = {
            'content_pillars': self._identify_content_pillars(content_type),
            'content_calendar': {
                'frequency': 'Post 2-3 times per week initially',
                'best_times': 'Peak engagement hours based on audience timezone',
                'content_mix': '70% educational, 20% promotional, 10% entertaining'
            },
            'content_formats': self._recommend_content_formats(content_type),
            'distribution_channels': [
                'Website blog',
                'Social media platforms',
                'Email newsletters',
                'Guest posting opportunities'
            ],
            'engagement_tactics': [
                'Encourage user-generated content',
                'Respond promptly to comments',
                'Run contests and giveaways',
                'Create interactive content (polls, quizzes)'
            ]
        }
        
        return strategy
    
    def _identify_content_pillars(self, content_type: str) -> List[str]:
        """Identify main content themes."""
        content_lower = content_type.lower()
        
        if 'product' in content_lower:
            return ['Product features', 'Use cases', 'Customer success', 'Industry trends']
        elif 'service' in content_lower:
            return ['Service offerings', 'Case studies', 'Expert insights', 'How-to guides']
        elif 'article' in content_lower or 'blog' in content_lower:
            return ['Educational content', 'Industry news', 'Best practices', 'Thought leadership']
        else:
            return ['Value proposition', 'Customer benefits', 'Social proof', 'Educational resources']
    
    def _recommend_content_formats(self, content_type: str) -> List[str]:
        """Recommend content formats based on content type."""
        formats = ['Blog posts', 'Infographics', 'Videos']
        
        content_lower = content_type.lower()
        if 'video' in content_lower:
            formats.extend(['Tutorial videos', 'Product demos', 'Live streams'])
        if 'image' in content_lower:
            formats.extend(['Photo galleries', 'Before/after comparisons', 'Visual case studies'])
        if 'text' in content_lower or 'article' in content_lower:
            formats.extend(['Long-form articles', 'White papers', 'E-books'])
        
        return formats
    
    def generate_seo_strategy(self) -> Dict:
        """Generate SEO strategy."""
        return {
            'on_page_seo': {
                'keyword_research': [
                    'Identify primary and secondary keywords',
                    'Analyze search volume and competition',
                    'Focus on long-tail keywords for quick wins'
                ],
                'technical_optimization': [
                    'Optimize page load speed',
                    'Implement schema markup',
                    'Create XML sitemap',
                    'Optimize meta titles and descriptions',
                    'Use header tags properly (H1, H2, H3)'
                ],
                'content_optimization': [
                    'Write compelling, keyword-rich content',
                    'Optimize images with alt tags',
                    'Create internal linking structure',
                    'Ensure mobile responsiveness'
                ]
            },
            'off_page_seo': {
                'link_building': [
                    'Guest posting on relevant websites',
                    'Build relationships with industry influencers',
                    'Create shareable content to earn backlinks',
                    'Submit to relevant directories'
                ],
                'local_seo': [
                    'Create Google Business Profile',
                    'Ensure NAP consistency across listings',
                    'Encourage customer reviews'
                ]
            },
            'monitoring': [
                'Track keyword rankings',
                'Monitor organic traffic',
                'Analyze backlink profile',
                'Review Core Web Vitals'
            ]
        }
    
    def generate_social_media_plan(self) -> Dict:
        """Generate social media marketing plan."""
        target_audience = self.website_requirements.get('project_overview', {}).get('target_audience', '')
        
        return {
            'platform_selection': self._recommend_platforms(target_audience),
            'content_strategy': {
                'posting_frequency': {
                    'LinkedIn': '1 post per day',
                    'Twitter/X': '3-5 tweets per day',
                    'Instagram': '1-2 posts per day',
                    'Facebook': '1 post per day'
                },
                'content_types': [
                    'Educational posts (tips, how-tos)',
                    'Behind-the-scenes content',
                    'User testimonials and success stories',
                    'Product/service updates',
                    'Industry news and trends'
                ]
            },
            'engagement_tactics': [
                'Respond to comments within 2 hours',
                'Join relevant conversations and hashtags',
                'Collaborate with micro-influencers',
                'Run social media contests',
                'Use stories and reels for authentic connection'
            ],
            'paid_social_strategy': {
                'budget_allocation': 'Start with $500-1000/month',
                'ad_types': ['Awareness campaigns', 'Lead generation', 'Retargeting'],
                'targeting': 'Use detailed demographic and interest targeting'
            }
        }
    
    def _recommend_platforms(self, audience: str) -> Dict[str, str]:
        """Recommend social media platforms based on audience."""
        audience_lower = audience.lower()
        
        platforms = {}
        
        if 'professional' in audience_lower or 'business' in audience_lower:
            platforms['LinkedIn'] = 'Primary - Best for B2B and professional networking'
            platforms['Twitter/X'] = 'Secondary - Great for thought leadership'
        
        if 'young' in audience_lower or 'student' in audience_lower:
            platforms['Instagram'] = 'Primary - Visual content performs well'
            platforms['TikTok'] = 'Primary - Short-form video content'
            platforms['Twitter/X'] = 'Secondary - Real-time engagement'
        
        if 'general' in audience_lower:
            platforms['Facebook'] = 'Primary - Broad reach'
            platforms['Instagram'] = 'Primary - Visual storytelling'
            platforms['LinkedIn'] = 'Secondary - Professional content'
        
        if not platforms:
            platforms = {
                'Facebook': 'Broad audience reach',
                'Instagram': 'Visual content and engagement',
                'LinkedIn': 'Professional networking'
            }
        
        return platforms
    
    def generate_email_marketing_strategy(self) -> Dict:
        """Generate email marketing strategy."""
        return {
            'list_building': {
                'tactics': [
                    'Lead magnets (ebooks, checklists, templates)',
                    'Website popup forms (exit-intent)',
                    'Content upgrades for blog posts',
                    'Webinar registrations',
                    'Contest entries'
                ],
                'segmentation': [
                    'New subscribers',
                    'Engaged users',
                    'Past customers',
                    'By interest/behavior',
                    'By demographic'
                ]
            },
            'campaign_types': {
                'welcome_series': 'Onboard new subscribers (3-5 emails)',
                'newsletter': 'Weekly or bi-weekly updates',
                'promotional': 'Product launches, sales, special offers',
                'educational': 'Tips, guides, best practices',
                're_engagement': 'Win back inactive subscribers'
            },
            'best_practices': [
                'Personalize subject lines and content',
                'Optimize for mobile devices',
                'A/B test subject lines and CTAs',
                'Send at optimal times (Tuesday-Thursday, 10am-11am)',
                'Maintain consistent sending schedule',
                'Clean list regularly (remove inactive users)'
            ],
            'metrics_to_track': [
                'Open rate (aim for 15-25%)',
                'Click-through rate (aim for 2-5%)',
                'Conversion rate',
                'Unsubscribe rate (keep below 0.5%)',
                'List growth rate'
            ]
        }
    
    def generate_paid_advertising_strategy(self) -> Dict:
        """Generate paid advertising strategy."""
        budget = self.website_requirements.get('project_constraints', {}).get('budget_timeline', '')
        
        return {
            'channel_recommendation': self._recommend_ad_channels(budget),
            'google_ads': {
                'campaign_types': ['Search ads', 'Display ads', 'Shopping ads (if ecommerce)'],
                'targeting': 'Keyword-based targeting with negative keywords',
                'budget': 'Start with $30-50/day, scale based on ROAS',
                'optimization': [
                    'Focus on high-intent keywords',
                    'Use ad extensions',
                    'Create compelling ad copy with strong CTAs',
                    'Optimize landing pages for conversions'
                ]
            },
            'facebook_instagram_ads': {
                'campaign_objectives': ['Traffic', 'Conversions', 'Lead generation'],
                'targeting': 'Detailed demographic, interest, and behavior targeting',
                'budget': '$20-40/day to start',
                'creative': [
                    'Use eye-catching visuals',
                    'Test video vs. image ads',
                    'Create multiple ad variations',
                    'Use carousel ads for products'
                ]
            },
            'retargeting': {
                'strategy': 'Target website visitors who didn\'t convert',
                'platforms': ['Google Display Network', 'Facebook Pixel', 'LinkedIn'],
                'budget': '20-30% of total ad budget',
                'tactics': [
                    'Dynamic product ads',
                    'Special offer campaigns',
                    'Abandoned cart reminders',
                    'Sequential messaging'
                ]
            }
        }
    
    def _recommend_ad_channels(self, budget: str) -> List[str]:
        """Recommend advertising channels based on budget."""
        budget_lower = budget.lower()
        
        if 'small' in budget_lower or 'quick' in budget_lower:
            return ['Google Ads (search only)', 'Facebook/Instagram ads', 'Focus on organic growth']
        elif 'large' in budget_lower:
            return ['Google Ads (all types)', 'Facebook/Instagram ads', 'LinkedIn ads', 'YouTube ads', 'Display network']
        else:
            return ['Google Ads (search + display)', 'Facebook/Instagram ads', 'Retargeting campaigns']
    
    def generate_analytics_plan(self) -> Dict:
        """Generate analytics and tracking strategy."""
        success_metrics = self.website_requirements.get('project_overview', {}).get('success_metrics', '')
        
        return {
            'tools_to_implement': [
                'Google Analytics 4',
                'Google Search Console',
                'Hotjar or similar heatmap tool',
                'Social media analytics',
                'Email marketing analytics'
            ],
            'key_metrics': self._identify_key_metrics(success_metrics),
            'conversion_tracking': {
                'goals_to_set': [
                    'Page views',
                    'Time on site',
                    'Form submissions',
                    'Button clicks',
                    'Purchases (if ecommerce)',
                    'Sign-ups'
                ],
                'event_tracking': [
                    'Video plays',
                    'Downloads',
                    'Outbound link clicks',
                    'Scroll depth',
                    'Search queries'
                ]
            },
            'reporting': {
                'frequency': 'Weekly for key metrics, monthly for comprehensive review',
                'dashboards': [
                    'Traffic overview',
                    'Conversion funnel',
                    'Campaign performance',
                    'User behavior flow',
                    'ROI by channel'
                ],
                'actions': [
                    'Review data weekly',
                    'Identify trends and patterns',
                    'Adjust strategies based on performance',
                    'Test hypotheses with A/B tests'
                ]
            }
        }
    
    def _identify_key_metrics(self, success_metrics: str) -> List[str]:
        """Identify key metrics to track based on success criteria."""
        metrics_lower = success_metrics.lower()
        key_metrics = []
        
        if 'traffic' in metrics_lower:
            key_metrics.extend(['Sessions', 'Users', 'Page views', 'Traffic sources'])
        if 'engagement' in metrics_lower:
            key_metrics.extend(['Bounce rate', 'Pages per session', 'Average session duration'])
        if 'conversion' in metrics_lower or 'sales' in metrics_lower:
            key_metrics.extend(['Conversion rate', 'Revenue', 'Average order value', 'Cart abandonment rate'])
        if 'retention' in metrics_lower:
            key_metrics.extend(['Return visitor rate', 'Customer lifetime value', 'Churn rate'])
        if 'brand' in metrics_lower or 'awareness' in metrics_lower:
            key_metrics.extend(['Social media reach', 'Brand mentions', 'Share of voice'])
        
        if not key_metrics:
            key_metrics = ['Sessions', 'Conversion rate', 'Bounce rate', 'Traffic sources']
        
        return key_metrics
    
    def generate_complete_strategy(self) -> Dict:
        """Generate the complete marketing strategy."""
        if not self.website_requirements:
            return {'error': 'No website requirements loaded. Please load requirements first.'}
        
        complete_strategy = {
            'executive_summary': self._generate_executive_summary(),
            'brand_positioning': self.generate_brand_positioning(),
            'content_strategy': self.generate_content_strategy(),
            'seo_strategy': self.generate_seo_strategy(),
            'social_media_plan': self.generate_social_media_plan(),
            'email_marketing': self.generate_email_marketing_strategy(),
            'paid_advertising': self.generate_paid_advertising_strategy(),
            'analytics_tracking': self.generate_analytics_plan(),
            'implementation_timeline': self._generate_timeline(),
            'budget_breakdown': self._generate_budget_breakdown()
        }
        
        self.strategy = complete_strategy
        return complete_strategy
    
    def _generate_executive_summary(self) -> str:
        """Generate executive summary of the marketing strategy."""
        purpose = self.website_requirements.get('project_overview', {}).get('purpose', 'the website')
        audience = self.website_requirements.get('project_overview', {}).get('target_audience', 'target users')
        
        summary = f"""
This comprehensive marketing strategy is designed to successfully launch and promote {purpose}, 
targeting {audience}. The strategy encompasses multiple channels including content marketing, 
SEO, social media, email marketing, and paid advertising to maximize reach and engagement.

The approach is data-driven, focusing on measurable results and continuous optimization. 
We'll start with foundational elements (website optimization, content creation, SEO) and 
progressively expand into paid channels as we validate our approach and scale what works.

Key success factors include consistent brand messaging, audience-focused content, 
multi-channel presence, and rigorous tracking of all marketing activities.
        """.strip()
        
        return summary
    
    def _generate_timeline(self) -> Dict:
        """Generate implementation timeline."""
        return {
            'phase_1_foundation': {
                'duration': 'Weeks 1-4',
                'activities': [
                    'Set up analytics and tracking',
                    'Optimize website for SEO',
                    'Create initial content batch',
                    'Set up social media profiles',
                    'Configure email marketing platform'
                ]
            },
            'phase_2_launch': {
                'duration': 'Weeks 5-8',
                'activities': [
                    'Launch website',
                    'Begin content publishing schedule',
                    'Start social media posting',
                    'Launch initial email campaigns',
                    'Begin small-scale paid advertising tests'
                ]
            },
            'phase_3_optimize': {
                'duration': 'Weeks 9-12',
                'activities': [
                    'Analyze performance data',
                    'Optimize underperforming channels',
                    'Scale successful campaigns',
                    'Expand content production',
                    'Build link building relationships'
                ]
            },
            'phase_4_scale': {
                'duration': 'Month 4+',
                'activities': [
                    'Increase ad budgets on winning campaigns',
                    'Launch advanced campaigns (retargeting, etc.)',
                    'Explore new channels and tactics',
                    'Develop strategic partnerships',
                    'Continuous testing and optimization'
                ]
            }
        }
    
    def _generate_budget_breakdown(self) -> Dict:
        """Generate recommended budget breakdown."""
        budget = self.website_requirements.get('project_constraints', {}).get('budget_timeline', '')
        
        if 'small' in budget.lower():
            return {
                'total_monthly': '$1,000 - $2,000',
                'breakdown': {
                    'content_creation': '$300 (30%)',
                    'paid_advertising': '$400 (40%)',
                    'tools_software': '$200 (20%)',
                    'email_marketing': '$100 (10%)'
                }
            }
        elif 'large' in budget.lower():
            return {
                'total_monthly': '$10,000+',
                'breakdown': {
                    'content_creation': '$2,000 (20%)',
                    'paid_advertising': '$5,000 (50%)',
                    'tools_software': '$1,000 (10%)',
                    'email_marketing': '$500 (5%)',
                    'influencer_partnerships': '$1,000 (10%)',
                    'design_creative': '$500 (5%)'
                }
            }
        else:
            return {
                'total_monthly': '$3,000 - $5,000',
                'breakdown': {
                    'content_creation': '$800 (20%)',
                    'paid_advertising': '$2,000 (50%)',
                    'tools_software': '$400 (10%)',
                    'email_marketing': '$300 (7.5%)',
                    'design_creative': '$500 (12.5%)'
                }
            }
    
    def export_strategy_document(self) -> str:
        """Export strategy as formatted text document."""
        if not self.strategy:
            return "No strategy generated yet. Please generate strategy first."
        
        doc = "=" * 80 + "\n"
        doc += "COMPREHENSIVE MARKETING STRATEGY\n"
        doc += "=" * 80 + "\n\n"
        
        for section, content in self.strategy.items():
            doc += f"\n{section.upper().replace('_', ' ')}\n"
            doc += "-" * 80 + "\n"
            doc += self._format_section(content)
            doc += "\n"
        
        return doc
    
    def _format_section(self, content, indent=0) -> str:
        """Recursively format section content."""
        formatted = ""
        indent_str = "  " * indent
        
        if isinstance(content, dict):
            for key, value in content.items():
                formatted += f"{indent_str}{key.replace('_', ' ').title()}:\n"
                formatted += self._format_section(value, indent + 1)
        elif isinstance(content, list):
            for item in content:
                formatted += f"{indent_str}• {item}\n"
        else:
            formatted += f"{indent_str}{content}\n"
        
        return formatted
