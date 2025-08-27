#!/usr/bin/env python3
"""
Lead Gear SEO Strategist Sub-Agent
An expert SEO strategist that analyzes websites and creates 12-month SEO plans
based on Lead Gear's service tiers (Starter, Business, Pro).
"""

import json
import sys
import argparse
from typing import Dict, List, Any
from datetime import datetime, timedelta
import requests
from urllib.parse import urlparse

# Service Tier Configurations
SERVICE_TIERS = {
    "starter": {
        "name": "Starter",
        "monthly_investment": "$899/month",
        "best_for": "Small businesses, local services, getting SEO foundation",
        "monthly_hours": 20,  # Estimated based on scope
        "features": {
            "technical_seo_fixes": "Basic implementation",
            "technical_seo_monitoring": False,
            "website_auditing": "Every Quarter",
            "advanced_schema": False,
            "ai_optimizations": False,
            "content_ai": False,
            "seo_ai_models": False,
            "content_strategy": False,
            "content_creation": False,
            "content_implementation": "Client handles",
            "onpage_optimization": "Top 5 pages",
            "existing_content_opt": "Basic optimization",
            "realtime_adjustments": False,
            "local_seo": "Up to 2 locations",
            "gbp_management": "One location",
            "nap_audit": "Basic audit",
            "link_building_strategy": "Basic NAP/Link strategy",
            "active_link_building": False,
            "ux_optimization": False,
            "cro": False,
            "ab_testing": False,
            "reporting": "Standard reporting",
            "performance_tracking": "Basic metrics",
            "strategy_calls": "Annual strategy call"
        }
    },
    "business": {
        "name": "Business",
        "monthly_investment": "$1,399/month",
        "best_for": "Growing businesses ready to scale, competitive markets",
        "monthly_hours": 35,  # Estimated based on scope
        "features": {
            "technical_seo_fixes": "Full implementation",
            "technical_seo_monitoring": "Ongoing watch for changes",
            "website_auditing": "Monthly",
            "advanced_schema": "Basic structured data optimization",
            "ai_optimizations": "Full one-time implementation",
            "content_ai": False,
            "seo_ai_models": False,
            "content_strategy": "Comprehensive strategy",
            "content_creation": "Strategy only",
            "content_implementation": "Client handles",
            "onpage_optimization": "Top 10 pages",
            "existing_content_opt": "Advanced optimization",
            "realtime_adjustments": False,
            "local_seo": "Up to 5 locations",
            "gbp_management": "Up to 2 locations",
            "nap_audit": "Advanced optimization",
            "link_building_strategy": "Advanced off-page strategy",
            "active_link_building": "One-time link acquisition",
            "ux_optimization": "User experience improvements",
            "cro": False,
            "ab_testing": False,
            "reporting": "Advanced reporting",
            "performance_tracking": "Comprehensive analytics",
            "strategy_calls": "Quarterly strategy call"
        }
    },
    "pro": {
        "name": "Pro",
        "monthly_investment": "$1,999/month",
        "best_for": "Established businesses wanting hands-off growth",
        "monthly_hours": 50,  # Estimated based on scope
        "features": {
            "technical_seo_fixes": "Advanced implementation",
            "technical_seo_monitoring": "Ongoing watch for changes",
            "website_auditing": "Monthly",
            "advanced_schema": "Advanced structured data optimization",
            "ai_optimizations": "Ongoing implementation",
            "content_ai": "Full Audit and Content Strategy",
            "seo_ai_models": "Advanced features and best practices",
            "content_strategy": "Comprehensive strategy",
            "content_creation": "3 new pages/month",
            "content_implementation": "Full done-for-you",
            "onpage_optimization": "All pages",
            "existing_content_opt": "Advanced optimization",
            "realtime_adjustments": "Based on ranking movement",
            "local_seo": "Up to 5 locations",
            "gbp_management": "Up to 5 profiles",
            "nap_audit": "Ongoing optimization",
            "link_building_strategy": "Advanced off-page strategy",
            "active_link_building": "Quarterly link acquisition",
            "ux_optimization": "User experience improvements",
            "cro": "CRO on key conversion pages",
            "ab_testing": "A/B Testing",
            "reporting": "Advanced reporting",
            "performance_tracking": "Comprehensive analytics",
            "strategy_calls": "Monthly strategy call"
        }
    }
}

class SEOStrategist:
    def __init__(self):
        self.current_date = datetime.now()
        
    def analyze_website(self, url: str) -> Dict[str, Any]:
        """
        Analyze website to determine complexity and recommend service tier
        """
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        # Basic website analysis (in real implementation, would use SEO tools)
        analysis = {
            "url": url,
            "domain": domain,
            "analysis_date": self.current_date.isoformat(),
            "estimated_pages": "TBD - Requires crawl",
            "business_type": "TBD - Manual assessment needed",
            "location_count": "TBD - Manual assessment needed",
            "competition_level": "TBD - Keyword research needed",
            "current_seo_status": "TBD - Audit needed",
            "recommended_tier": None
        }
        
        return analysis
    
    def recommend_tier(self, business_size: str, competition: str, budget_range: str, goals: str) -> str:
        """
        Recommend appropriate service tier based on business characteristics
        """
        if budget_range == "under_1000" or business_size == "small_local":
            return "starter"
        elif budget_range == "1000_1500" or (business_size == "growing" and competition == "medium"):
            return "business"
        elif budget_range == "over_1500" or competition == "high" or goals == "aggressive_growth":
            return "pro"
        else:
            return "business"  # Default to middle tier
    
    def generate_12_month_plan(self, url: str, tier: str, business_info: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate comprehensive 12-month SEO plan based on Lead Gear process
        """
        if tier not in SERVICE_TIERS:
            raise ValueError(f"Invalid tier: {tier}. Must be one of: {list(SERVICE_TIERS.keys())}")
        
        tier_config = SERVICE_TIERS[tier]
        
        # Phase definitions based on Lead Gear process
        phases = self._define_phases(tier_config)
        
        # Monthly breakdown
        monthly_plan = self._create_monthly_breakdown(phases, tier_config)
        
        # Hour allocation
        hour_allocation = self._calculate_hour_allocation(tier_config, monthly_plan)
        
        plan = {
            "client_info": {
                "url": url,
                "tier": tier_config["name"],
                "monthly_investment": tier_config["monthly_investment"],
                "monthly_hours": tier_config["monthly_hours"],
                "plan_generated": self.current_date.isoformat()
            },
            "phases": phases,
            "monthly_breakdown": monthly_plan,
            "hour_allocation": hour_allocation,
            "automation_opportunities": self._identify_automation_opportunities(tier_config),
            "kpis": self._define_kpis(tier),
            "deliverables": self._define_deliverables(tier_config)
        }
        
        return plan
    
    def _define_phases(self, tier_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Define the 5 phases of Lead Gear's SEO process
        """
        return {
            "phase_0_setup": {
                "name": "Client Setup & Onboarding",
                "duration": "Week 1",
                "tasks": [
                    "Sales handoff meeting",
                    "Client kickoff meeting prep",
                    "Tool setup (GA, GTM, GSC, GBP)",
                    "Initial site audit setup",
                    "SEO kickoff meeting"
                ]
            },
            "phase_1_plan": {
                "name": "Plan - Research, Evaluate & Develop",
                "duration": "Weeks 2-6",
                "tasks": [
                    "Company & industry research",
                    "Competitor analysis",
                    "Keyword research",
                    "Baseline analytics setup",
                    "Technical SEO audit",
                    "On-page SEO audit",
                    "Off-page SEO audit",
                    "Content audit",
                    "Strategy meeting",
                    "SEO roadmap development"
                ]
            },
            "phase_2_build": {
                "name": "Build - Execute The Plan",
                "duration": "Weeks 7-12",
                "tasks": self._get_build_tasks(tier_config)
            },
            "phase_3_measure": {
                "name": "Measure - Gather Data & Share Success",
                "duration": "Month 3-4",
                "tasks": [
                    "Analytics review",
                    "SEO tools analysis",
                    "Ranking review",
                    "Report building",
                    "Client meeting prep",
                    "Results presentation"
                ]
            },
            "phase_4_learn": {
                "name": "Learn - Review, Refine & Repeat",
                "duration": "Month 4 onwards",
                "tasks": [
                    "Performance evaluation",
                    "Strategy review",
                    "Roadmap updates",
                    "Continuous optimization"
                ]
            }
        }
    
    def _get_build_tasks(self, tier_config: Dict[str, Any]) -> List[str]:
        """
        Get build phase tasks based on tier capabilities
        """
        base_tasks = [
            "Plugin installation & configuration",
            "Sitemap submission",
            "Google Search Console error fixes"
        ]
        
        # Technical tasks
        if tier_config["features"]["technical_seo_fixes"] == "Advanced implementation":
            base_tasks.extend([
                "Advanced technical SEO implementation",
                "Page speed optimization",
                "Advanced redirects setup"
            ])
        elif tier_config["features"]["technical_seo_fixes"] == "Full implementation":
            base_tasks.extend([
                "Full technical SEO implementation",
                "Page speed optimization",
                "Redirects setup"
            ])
        else:
            base_tasks.extend([
                "Basic technical SEO fixes"
            ])
        
        # On-page tasks
        base_tasks.extend([
            f"Title tag optimization ({tier_config['features']['onpage_optimization']})",
            "H1 tag optimization",
            "Meta description optimization",
            "URL optimization",
            "Internal linking optimization"
        ])
        
        # Content tasks
        if tier_config["features"]["content_creation"]:
            base_tasks.append(f"Content creation: {tier_config['features']['content_creation']}")
        
        # Schema markup
        if tier_config["features"]["advanced_schema"]:
            base_tasks.append(f"Schema implementation: {tier_config['features']['advanced_schema']}")
        
        # Local SEO
        if tier_config["features"]["local_seo"]:
            base_tasks.extend([
                f"Local SEO optimization ({tier_config['features']['local_seo']})",
                f"Google Business Profile management ({tier_config['features']['gbp_management']})",
                f"NAP optimization ({tier_config['features']['nap_audit']})"
            ])
        
        # Link building
        if tier_config["features"]["active_link_building"]:
            base_tasks.append(f"Link building: {tier_config['features']['active_link_building']}")
        
        return base_tasks
    
    def _create_monthly_breakdown(self, phases: Dict[str, Any], tier_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create detailed monthly breakdown of activities
        """
        monthly_breakdown = {}
        
        for month in range(1, 13):
            month_key = f"month_{month}"
            
            if month == 1:
                # Setup and planning phase
                monthly_breakdown[month_key] = {
                    "focus": "Onboarding & Initial Planning",
                    "primary_activities": [
                        "Client onboarding",
                        "Initial audits",
                        "Strategy development"
                    ],
                    "hours_allocated": tier_config["monthly_hours"],
                    "expected_deliverables": [
                        "SEO audit reports",
                        "12-month SEO roadmap",
                        "Baseline metrics"
                    ]
                }
            elif month <= 3:
                # Build phase
                monthly_breakdown[month_key] = {
                    "focus": "Implementation & Foundation Building",
                    "primary_activities": [
                        "Technical SEO implementation",
                        "On-page optimization",
                        "Content optimization",
                        "Local SEO setup"
                    ],
                    "hours_allocated": tier_config["monthly_hours"],
                    "expected_deliverables": [
                        "Technical improvements report",
                        "Optimized pages list",
                        "Monthly progress report"
                    ]
                }
            elif month <= 6:
                # Measure and early learn phase
                monthly_breakdown[month_key] = {
                    "focus": "Measurement & Initial Optimization",
                    "primary_activities": [
                        "Performance monitoring",
                        "Initial results analysis",
                        "Strategy refinement",
                        "Continued optimization"
                    ],
                    "hours_allocated": tier_config["monthly_hours"],
                    "expected_deliverables": [
                        "Performance reports",
                        "Optimization recommendations",
                        "Quarterly strategy review"
                    ]
                }
            else:
                # Ongoing optimization phase
                monthly_breakdown[month_key] = {
                    "focus": "Continuous Improvement & Scaling",
                    "primary_activities": self._get_ongoing_activities(tier_config),
                    "hours_allocated": tier_config["monthly_hours"],
                    "expected_deliverables": [
                        "Monthly performance reports",
                        "Ongoing optimizations",
                        "Strategic recommendations"
                    ]
                }
        
        return monthly_breakdown
    
    def _get_ongoing_activities(self, tier_config: Dict[str, Any]) -> List[str]:
        """
        Get ongoing activities based on tier
        """
        activities = [
            "Performance monitoring",
            "Content optimization",
            "Technical maintenance"
        ]
        
        if tier_config["features"]["content_creation"]:
            activities.append("New content creation")
        
        if tier_config["features"]["active_link_building"]:
            activities.append("Link building activities")
        
        if tier_config["features"]["realtime_adjustments"]:
            activities.append("Real-time ranking adjustments")
        
        if tier_config["name"] == "Pro":
            activities.extend([
                "Advanced AI optimizations",
                "CRO testing",
                "Advanced reporting"
            ])
        
        return activities
    
    def _calculate_hour_allocation(self, tier_config: Dict[str, Any], monthly_plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate hour allocation across different SEO activities
        """
        total_monthly_hours = tier_config["monthly_hours"]
        
        # Base allocation percentages (adjust based on tier and phase)
        if tier_config["name"] == "Starter":
            allocation = {
                "technical_seo": 25,      # 25% of hours
                "onpage_optimization": 30, # 30% of hours
                "content_work": 15,        # 15% of hours
                "local_seo": 20,          # 20% of hours
                "reporting": 10           # 10% of hours
            }
        elif tier_config["name"] == "Business":
            allocation = {
                "technical_seo": 20,
                "onpage_optimization": 25,
                "content_work": 25,
                "local_seo": 15,
                "link_building": 10,
                "reporting": 5
            }
        else:  # Pro
            allocation = {
                "technical_seo": 15,
                "onpage_optimization": 20,
                "content_work": 35,
                "local_seo": 10,
                "link_building": 10,
                "cro_testing": 5,
                "reporting": 5
            }
        
        # Convert percentages to actual hours
        hour_breakdown = {}
        for category, percentage in allocation.items():
            hour_breakdown[category] = round((percentage / 100) * total_monthly_hours, 1)
        
        return {
            "monthly_total_hours": total_monthly_hours,
            "category_breakdown": hour_breakdown,
            "annual_hours": total_monthly_hours * 12
        }
    
    def _identify_automation_opportunities(self, tier_config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Identify tasks that can be automated to improve efficiency
        """
        opportunities = [
            {
                "task": "Technical SEO Monitoring",
                "automation_potential": "High",
                "tools": ["Google Search Console API", "Screaming Frog", "SEMrush API"],
                "estimated_time_savings": "5-8 hours/month",
                "implementation_complexity": "Medium"
            },
            {
                "task": "Rank Tracking",
                "automation_potential": "High",
                "tools": ["SEMrush API", "Ahrefs API", "Custom dashboard"],
                "estimated_time_savings": "3-5 hours/month",
                "implementation_complexity": "Low"
            },
            {
                "task": "Reporting",
                "automation_potential": "High",
                "tools": ["Google Analytics API", "Data Studio", "Custom reporting"],
                "estimated_time_savings": "8-12 hours/month",
                "implementation_complexity": "Medium"
            },
            {
                "task": "Content Optimization Analysis",
                "automation_potential": "Medium",
                "tools": ["Content analysis APIs", "AI writing tools", "SEO content tools"],
                "estimated_time_savings": "4-6 hours/month",
                "implementation_complexity": "High"
            },
            {
                "task": "Local Citation Management",
                "automation_potential": "Medium",
                "tools": ["BrightLocal API", "Moz Local", "Citation tracking tools"],
                "estimated_time_savings": "2-4 hours/month",
                "implementation_complexity": "Medium"
            }
        ]
        
        return opportunities
    
    def _define_kpis(self, tier: str) -> Dict[str, List[str]]:
        """
        Define KPIs based on service tier
        """
        base_kpis = [
            "Organic traffic growth",
            "Keyword ranking improvements",
            "Technical SEO score",
            "Page load speed improvements"
        ]
        
        if tier in ["business", "pro"]:
            base_kpis.extend([
                "Content engagement metrics",
                "Local search visibility",
                "Backlink profile growth"
            ])
        
        if tier == "pro":
            base_kpis.extend([
                "Conversion rate improvements",
                "Revenue attribution",
                "AI search readiness score"
            ])
        
        return {
            "primary_kpis": base_kpis,
            "reporting_frequency": SERVICE_TIERS[tier]["features"]["strategy_calls"]
        }
    
    def _define_deliverables(self, tier_config: Dict[str, Any]) -> Dict[str, List[str]]:
        """
        Define deliverables based on tier
        """
        deliverables = {
            "monthly": [
                "Performance report",
                "Ranking updates",
                "Work completed summary"
            ],
            "quarterly": [
                "Comprehensive audit",
                "Strategy review",
                "Roadmap updates"
            ],
            "annual": [
                "Full SEO assessment",
                "Year 2 strategy",
                "ROI analysis"
            ]
        }
        
        if tier_config["name"] in ["Business", "Pro"]:
            deliverables["monthly"].extend([
                "Content recommendations",
                "Technical optimization report"
            ])
        
        if tier_config["name"] == "Pro":
            deliverables["monthly"].extend([
                "New content pieces (3/month)",
                "CRO test results",
                "AI optimization updates"
            ])
        
        return deliverables

    def export_plan_to_json(self, plan: Dict[str, Any], filename: str = None) -> str:
        """
        Export the SEO plan to a JSON file
        """
        if not filename:
            domain = urlparse(plan["client_info"]["url"]).netloc.replace("www.", "")
            filename = f"{domain}_{plan['client_info']['tier'].lower()}_seo_plan.json"
        
        with open(filename, 'w') as f:
            json.dump(plan, f, indent=2, default=str)
        
        return filename

def main():
    parser = argparse.ArgumentParser(description="Lead Gear SEO Strategist Sub-Agent")
    parser.add_argument("url", help="Website URL to analyze")
    parser.add_argument("--tier", choices=["starter", "business", "pro"], 
                       help="Service tier (if not specified, will be recommended)")
    parser.add_argument("--business-size", choices=["small_local", "growing", "established"],
                       help="Business size for tier recommendation")
    parser.add_argument("--competition", choices=["low", "medium", "high"],
                       help="Competition level for tier recommendation")
    parser.add_argument("--budget", choices=["under_1000", "1000_1500", "over_1500"],
                       help="Monthly budget range for tier recommendation")
    parser.add_argument("--goals", choices=["foundation", "growth", "aggressive_growth"],
                       help="Business goals for tier recommendation")
    parser.add_argument("--output", help="Output filename for the plan")
    
    args = parser.parse_args()
    
    strategist = SEOStrategist()
    
    # Analyze website
    print(f"🔍 Analyzing website: {args.url}")
    analysis = strategist.analyze_website(args.url)
    
    # Determine tier
    if args.tier:
        tier = args.tier
        print(f"📊 Using specified tier: {tier.upper()}")
    else:
        tier = strategist.recommend_tier(
            args.business_size or "growing",
            args.competition or "medium", 
            args.budget or "1000_1500",
            args.goals or "growth"
        )
        print(f"💡 Recommended tier: {tier.upper()}")
    
    # Generate 12-month plan
    print(f"📋 Generating 12-month SEO plan...")
    plan = strategist.generate_12_month_plan(args.url, tier)
    
    # Export plan
    filename = strategist.export_plan_to_json(plan, args.output)
    print(f"✅ SEO plan exported to: {filename}")
    
    # Display summary
    print(f"\n🎯 PLAN SUMMARY")
    print(f"Client: {plan['client_info']['url']}")
    print(f"Tier: {plan['client_info']['tier']}")
    print(f"Investment: {plan['client_info']['monthly_investment']}")
    print(f"Monthly Hours: {plan['client_info']['monthly_hours']}")
    print(f"Annual Hours: {plan['hour_allocation']['annual_hours']}")
    
    print(f"\n📈 PRIMARY FOCUS AREAS:")
    for category, hours in plan['hour_allocation']['category_breakdown'].items():
        print(f"  • {category.replace('_', ' ').title()}: {hours} hours/month")
    
    print(f"\n🤖 TOP AUTOMATION OPPORTUNITIES:")
    for opp in plan['automation_opportunities'][:3]:
        print(f"  • {opp['task']}: {opp['estimated_time_savings']} savings")

if __name__ == "__main__":
    main()
