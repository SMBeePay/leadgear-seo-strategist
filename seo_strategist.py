#!/usr/bin/env python3
"""
ClickUp CSV Export Enhancement for SEO Strategist
Adds functionality to export SEO tasks as ClickUp-importable CSV
"""

import csv
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any
from urllib.parse import urlparse

def export_to_clickup_csv(plan: Dict[str, Any], filename: str = None) -> str:
    """Export SEO plan tasks to ClickUp-importable CSV format"""
    
    if not filename:
        domain = urlparse(plan["client_info"]["url"]).netloc.replace("www.", "")
        timestamp = datetime.now().strftime("%Y%m%d")
        filename = f"{domain}_seo_tasks_clickup_{timestamp}.csv"
    
    # ClickUp CSV format columns
    fieldnames = [
        'Name',                    # Task name
        'Description',             # Task description
        'Priority',               # Priority level
        'Status',                 # Task status
        'Assignee',               # Who's assigned
        'Due Date',               # Due date
        'Tags',                   # Task tags
        'List',                   # ClickUp list name
        'Time Estimate',          # Time estimate in minutes
        'Parent Task',            # Parent task for subtasks
        'Folder',                 # Folder organization
        'Space'                   # Space organization
    ]
    
    tasks = []
    current_date = datetime.now()
    client_domain = urlparse(plan["client_info"]["url"]).netloc.replace("www.", "")
    tier = plan["client_info"]["tier"]
    
    # Get audit-based tasks
    audit_tasks = plan.get('audit_based_tasks', {})
    
    # Process immediate fixes (Critical Priority)
    immediate_tasks = audit_tasks.get('immediate_fixes', [])
    for i, task in enumerate(immediate_tasks, 1):
        due_date = (current_date + timedelta(weeks=2)).strftime('%m/%d/%Y')
        
        # Main task
        main_task = {
            'Name': f"CRITICAL: {task['task']}",
            'Description': f"Priority: {task['priority']} | Type: {task['type']} | Pages affected: {task.get('pages_affected', 'N/A')} | Deadline: {task.get('deadline', 'Week 2')}",
            'Priority': 'High',
            'Status': 'to do',
            'Assignee': '',  # Will be filled by user
            'Due Date': due_date,
            'Tags': f"SEO,Critical,{task['type']},{tier}",
            'List': 'SEO Immediate Fixes',
            'Time Estimate': str(int(task['estimated_hours'] * 60)),  # Convert to minutes
            'Parent Task': '',
            'Folder': f'{client_domain} SEO',
            'Space': 'Client Projects'
        }
        tasks.append(main_task)
        
        # Add subtasks if pages affected > 5
        if task.get('pages_affected', 0) > 5:
            pages_per_subtask = max(5, task.get('pages_affected', 0) // 3)
            subtask_count = (task.get('pages_affected', 0) + pages_per_subtask - 1) // pages_per_subtask
            
            for j in range(subtask_count):
                start_page = j * pages_per_subtask + 1
                end_page = min((j + 1) * pages_per_subtask, task.get('pages_affected', 0))
                
                subtask = {
                    'Name': f"Pages {start_page}-{end_page}: {task['task']}",
                    'Description': f"Handle pages {start_page} through {end_page} for: {task['task']}",
                    'Priority': 'High',
                    'Status': 'to do',
                    'Assignee': '',
                    'Due Date': due_date,
                    'Tags': f"SEO,Critical,{task['type']},Subtask",
                    'List': 'SEO Immediate Fixes',
                    'Time Estimate': str(int((task['estimated_hours'] / subtask_count) * 60)),
                    'Parent Task': f"CRITICAL: {task['task']}",
                    'Folder': f'{client_domain} SEO',
                    'Space': 'Client Projects'
                }
                tasks.append(subtask)
    
    # Process short-term tasks (Important Priority)
    short_term_tasks = audit_tasks.get('short_term', [])
    for task in short_term_tasks:
        due_date = (current_date + timedelta(weeks=8)).strftime('%m/%d/%Y')
        
        main_task = {
            'Name': f"IMPORTANT: {task['task']}",
            'Description': f"Priority: {task['priority']} | Type: {task['type']} | Pages affected: {task.get('pages_affected', 'N/A')} | Deadline: {task.get('deadline', 'Month 2')}",
            'Priority': 'Normal',
            'Status': 'to do',
            'Assignee': '',
            'Due Date': due_date,
            'Tags': f"SEO,Important,{task['type']},{tier}",
            'List': 'SEO Short-term',
            'Time Estimate': str(int(task['estimated_hours'] * 60)),
            'Parent Task': '',
            'Folder': f'{client_domain} SEO',
            'Space': 'Client Projects'
        }
        tasks.append(main_task)
    
    # Process medium-term tasks
    medium_term_tasks = audit_tasks.get('medium_term', [])
    for task in medium_term_tasks:
        due_date = (current_date + timedelta(weeks=16)).strftime('%m/%d/%Y')
        
        main_task = {
            'Name': f"MEDIUM: {task['task']}",
            'Description': f"Priority: {task['priority']} | Type: {task['type']} | Pages affected: {task.get('pages_affected', 'N/A')} | Deadline: {task.get('deadline', 'Month 4')}",
            'Priority': 'Low',
            'Status': 'to do',
            'Assignee': '',
            'Due Date': due_date,
            'Tags': f"SEO,Medium,{task['type']},{tier}",
            'List': 'SEO Medium-term',
            'Time Estimate': str(int(task['estimated_hours'] * 60)),
            'Parent Task': '',
            'Folder': f'{client_domain} SEO',
            'Space': 'Client Projects'
        }
        tasks.append(main_task)
    
    # Process long-term strategic tasks
    long_term_tasks = audit_tasks.get('long_term', [])
    for task in long_term_tasks:
        due_date = (current_date + timedelta(weeks=24)).strftime('%m/%d/%Y')
        
        main_task = {
            'Name': f"STRATEGIC: {task['task']}",
            'Description': f"Priority: {task['priority']} | Type: {task['type']} | Deadline: {task.get('deadline', 'Month 6')}",
            'Priority': 'Low',
            'Status': 'to do',
            'Assignee': '',
            'Due Date': due_date,
            'Tags': f"SEO,Strategic,{task['type']},{tier}",
            'List': 'SEO Long-term',
            'Time Estimate': str(int(task['estimated_hours'] * 60)),
            'Parent Task': '',
            'Folder': f'{client_domain} SEO',
            'Space': 'Client Projects'
        }
        tasks.append(main_task)
    
    # Process recurring tasks
    ongoing_tasks = audit_tasks.get('ongoing', [])
    for task in ongoing_tasks:
        if not task.get('recurring'):
            continue
            
        frequency = task.get('frequency', 'monthly')
        
        # Create multiple instances based on frequency
        if frequency == 'monthly':
            instances = 12
            interval = 30  # days
        elif frequency == 'quarterly':
            instances = 4
            interval = 90  # days
        elif frequency == 'bi-annually':
            instances = 2
            interval = 180  # days
        else:
            instances = 1
            interval = 30
        
        for i in range(instances):
            due_date = (current_date + timedelta(days=interval * (i + 1))).strftime('%m/%d/%Y')
            instance_name = f"RECURRING ({frequency.upper()}): {task['task']}"
            
            if instances > 1:
                if frequency == 'monthly':
                    month_name = (current_date + timedelta(days=interval * (i + 1))).strftime('%B %Y')
                    instance_name += f" - {month_name}"
                elif frequency == 'quarterly':
                    quarter = f"Q{i+1} {current_date.year if i < 2 else current_date.year + 1}"
                    instance_name += f" - {quarter}"
                elif frequency == 'bi-annually':
                    half = "H1" if i == 0 else "H2"
                    instance_name += f" - {half} {current_date.year}"
            
            recurring_task = {
                'Name': instance_name,
                'Description': f"Recurring task: {task['task']} | Frequency: {frequency} | Type: {task['type']} | Hours: {task['estimated_hours']}",
                'Priority': 'Normal',
                'Status': 'to do' if i == 0 else 'future',  # First instance active, others future
                'Assignee': '',
                'Due Date': due_date,
                'Tags': f"SEO,Recurring,{frequency},{task['type']},{tier}",
                'List': 'SEO Recurring Tasks',
                'Time Estimate': str(int(task['estimated_hours'] * 60)),
                'Parent Task': '',
                'Folder': f'{client_domain} SEO',
                'Space': 'Client Projects'
            }
            tasks.append(recurring_task)
    
    # Add project overview task
    overview_task = {
        'Name': f"SEO Project Overview - {client_domain}",
        'Description': f"12-month SEO project for {plan['client_info']['url']} | Tier: {tier} | Monthly Hours: {plan['client_info']['actual_monthly_hours']} | Investment: {plan['client_info']['monthly_investment']}",
        'Priority': 'High',
        'Status': 'in progress',
        'Assignee': '',
        'Due Date': (current_date + timedelta(days=365)).strftime('%m/%d/%Y'),
        'Tags': f"SEO,Project,Overview,{tier}",
        'List': 'SEO Projects',
        'Time Estimate': str(int(plan['client_info']['actual_monthly_hours'] * 12 * 60)),  # Total annual hours in minutes
        'Parent Task': '',
        'Folder': f'{client_domain} SEO',
        'Space': 'Client Projects'
    }
    tasks.append(overview_task)
    
    # Write CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)
    
    return filename

# Add this method to the EnhancedSEOStrategist class
def add_clickup_export_method():
    """
    Add this method to your existing EnhancedSEOStrategist class:
    """
    return '''
    def export_clickup_csv(self, plan: Dict[str, Any], filename: str = None) -> str:
        """Export SEO plan to ClickUp CSV format"""
        return export_to_clickup_csv(plan, filename)
    '''

# Usage example for integration:
def integrate_clickup_export():
    """
    To integrate this into your existing SEO strategist, add these lines to the main() function:
    """
    return '''
    # After generating the plan and before the summary display, add:
    
    # Export to ClickUp CSV
    clickup_filename = export_to_clickup_csv(plan)
    print(f"ClickUp tasks exported to: {clickup_filename}")
    
    # Add command line argument:
    parser.add_argument("--clickup-csv", action="store_true", 
                       help="Export tasks to ClickUp-importable CSV")
    
    # In the main logic:
    if args.clickup_csv:
        clickup_filename = export_to_clickup_csv(plan)
        print(f"ClickUp CSV exported to: {clickup_filename}")
    '''

if __name__ == "__main__":
    print("ClickUp CSV Export Enhancement")
    print("Add the export_to_clickup_csv function to your SEO strategist")
    print("Then integrate the export functionality into your main script")    
