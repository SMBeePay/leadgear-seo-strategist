#!/usr/bin/env python3
"""
Lead Gear SEO Strategist - Interactive Mode
Interactive questionnaire for generating SEO plans
"""

import sys
import os
import subprocess
from typing import Dict, Any

def print_header():
    """Print the interactive mode header"""
    print("🎯" + "=" * 60)
    print("       Lead Gear SEO Strategist - Interactive Mode")
    print("=" * 62)
    print()

def get_url():
    """Get and validate the website URL"""
    while True:
        url = input("🌐 Enter the website URL: ").strip()
        if url:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            return url
        print("❌ Please enter a valid URL")

def get_business_size():
    """Get business size information"""
    print("\n📊 What's the business size?")
    print("1) Small local business")
    print("2) Growing business")
    print("3) Established enterprise")
    
    while True:
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            return "small_local"
        elif choice == "2":
            return "growing"
        elif choice == "3":
            return "established"
        print("❌ Please select 1, 2, or 3")

def get_competition_level():
    """Get competition level information"""
    print("\n🏆 What's the competition level in their industry?")
    print("1) Low competition (local/niche market)")
    print("2) Medium competition (regional/moderate)")
    print("3) High competition (national/highly competitive)")
    
    while True:
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            return "low"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "high"
        print("❌ Please select 1, 2, or 3")

def get_budget_range():
    """Get budget range information"""
    print("\n💰 What's their monthly SEO budget range?")
    print("1) Under $1,000")
    print("2) $1,000 - $1,500")
    print("3) Over $1,500")
    
    while True:
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            return "under_1000"
        elif choice == "2":
            return "1000_1500"
        elif choice == "3":
            return "over_1500"
        print("❌ Please select 1, 2, or 3")

def get_goals():
    """Get business goals information"""
    print("\n🎯 What are their primary SEO goals?")
    print("1) Build SEO foundation (just getting started)")
    print("2) Steady, sustainable growth")
    print("3) Aggressive growth and market domination")
    
    while True:
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            return "foundation"
        elif choice == "2":
            return "growth"
        elif choice == "3":
            return "aggressive_growth"
        print("❌ Please select 1, 2, or 3")

def get_output_preference():
    """Get output file preference"""
    print("\n📄 Would you like to save the plan to a specific file?")
    filename = input("Enter filename (or press Enter for auto-generated): ").strip()
    return filename if filename else None

def confirm_details(url: str, business_size: str, competition: str, budget: str, goals: str, output: str = None):
    """Confirm the collected details"""
    print("\n" + "="*50)
    print("📋 PLAN SUMMARY")
    print("="*50)
    print(f"Website: {url}")
    print(f"Business Size: {business_size.replace('_', ' ').title()}")
    print(f"Competition: {competition.title()}")
    print(f"Budget Range: ${budget.replace('_', ' - $').replace('under ', 'Under $').replace('over ', 'Over $')}")
    print(f"Goals: {goals.replace('_', ' ').title()}")
    if output:
        print(f"Output File: {output}")
    print("="*50)
    
    while True:
        confirm = input("\n✅ Generate SEO plan with these settings? (y/n): ").strip().lower()
        if confirm in ['y', 'yes']:
            return True
        elif confirm in ['n', 'no']:
            return False
        print("❌ Please enter 'y' or 'n'")

def run_seo_planner(url: str, business_size: str, competition: str, budget: str, goals: str, output: str = None):
    """Run the main SEO planner with collected parameters"""
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    seo_script = os.path.join(script_dir, 'seo_strategist.py')
    
    # Build command
    cmd = [
        'python3', seo_script, url,
        '--business-size', business_size,
        '--competition', competition,
        '--budget', budget,
        '--goals', goals
    ]
    
    if output:
        cmd.extend(['--output', output])
    
    print("\n🚀 Generating SEO plan...")
    print("Command:", ' '.join(cmd))
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Warnings:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating plan: {e}")
        if e.stdout:
            print("Output:", e.stdout)
        if e.stderr:
            print("Error:", e.stderr)
        return False
    except FileNotFoundError:
        print(f"❌ Could not find seo_strategist.py at {seo_script}")
        print("Make sure the SEO Strategist is properly installed.")
        return False
    
    return True

def main():
    """Main interactive flow"""
    print_header()
    
    # Collect information
    url = get_url()
    business_size = get_business_size()
    competition = get_competition_level()
    budget = get_budget_range()
    goals = get_goals()
    output = get_output_preference()
    
    # Confirm details
    if not confirm_details(url, business_size, competition, budget, goals, output):
        print("\n❌ Plan generation cancelled.")
        return
    
    # Generate the plan
    success = run_seo_planner(url, business_size, competition, budget, goals, output)
    
    if success:
        print("\n🎉 SEO plan generation complete!")
        print("\n📖 Next steps:")
        print("1. Review the generated plan file")
        print("2. Present to client for approval")
        print("3. Begin implementation using Lead Gear's 5-phase process")
    else:
        print("\n❌ Plan generation failed. Please try again or use manual mode:")
        print(f"seo-plan {url} --business-size {business_size} --competition {competition} --budget {budget} --goals {goals}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If URL is provided as argument, use it
        url = sys.argv[1]
        print_header()
        print(f"🌐 Website: {url}")
        
        business_size = get_business_size()
        competition = get_competition_level()
        budget = get_budget_range()
        goals = get_goals()
        output = get_output_preference()
        
        if confirm_details(url, business_size, competition, budget, goals, output):
            run_seo_planner(url, business_size, competition, budget, goals, output)
        else:
            print("\n❌ Plan generation cancelled.")
    else:
        main()
