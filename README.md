# Lead Gear SEO Strategist Sub-Agent

A Claude Code sub-agent that generates comprehensive, data-driven 12-month SEO plans based on real audit results and Lead Gear's proven methodology.

## Features

- **Real SEO Audits**: Integration with DataForSEO API for actual website analysis
- **Smart Tier Recommendations**: Automatically suggests Starter, Business, or Pro tiers based on audit complexity
- **Specific Actionable Tasks**: Generate concrete tasks like "Add title tags to 12 pages" instead of generic recommendations
- **Dynamic Hour Allocation**: Calculate actual hours needed based on issues found
- **ClickUp CSV Export**: Export all tasks to ClickUp-importable format for team management
- **Recurring Task Management**: Proper frequency planning (monthly/quarterly/bi-annually) by tier
- **Tier Override**: Specify tier manually with smart resource allocation warnings

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/SMBeepay/leadgear-seo-strategist/main/install.sh | bash
```

## Service Tiers

| Tier | Investment | Hours/Month | Recurring Tasks | Best For |
|------|-----------|-------------|-----------------|----------|
| **Starter** | $899/month | 20 hours | Quarterly monitoring, bi-annual reviews | Small businesses, local services, SEO foundation |
| **Business** | $1,399/month | 35 hours | Monthly optimization, quarterly strategy | Growing businesses, competitive markets |
| **Pro** | $1,999/month | 50 hours | Monthly everything, advanced features | Established businesses, hands-off growth |

## Usage Examples

### Basic Audit with Tier Recommendation
```bash
seo-plan https://client.com
```

### Force Specific Tier
```bash
seo-plan https://client.com --tier pro
# Shows: "Note: Specified tier may be over-resourced for this website's needs"
```

### Full Audit with ClickUp Export
```bash
seo-audit https://client.com
# Generates both JSON plan and ClickUp-importable CSV
```

### Quick Tier-Specific Plans
```bash
seo-starter https://client.com
seo-business https://client.com  
seo-pro https://client.com
```

### Advanced Options
```bash
seo-plan https://client.com \
  --tier business \
  --clickup-csv \
  --output custom_plan.json \
  --dataforseo-username your_username \
  --dataforseo-password your_password
```

## Real vs Demo Mode

### With DataForSEO API (Recommended)
- **Real audit data**: Actual missing title tags, 404 errors, page speed issues
- **Specific tasks**: "Fix 3 broken pages causing 404 errors"
- **Accurate estimates**: Hours based on actual issues found
- **Smart recommendations**: Tier suggestions based on complexity

### Demo Mode (No API Required)
- **Realistic sample data**: Based on typical website issues
- **Generic tasks**: Standard SEO improvement recommendations
- **Estimated hours**: Average time allocations
- **Default recommendations**: Business tier for most sites

## DataForSEO Setup

1. **Sign up**: https://app.dataforseo.com/register
2. **Get credentials**: Username and password from dashboard
3. **Add to environment**:
```bash
export DATAFORSEO_USERNAME="your_username"
export DATAFORSEO_PASSWORD="your_password"
echo 'export DATAFORSEO_USERNAME="your_username"' >> ~/.zshrc
echo 'export DATAFORSEO_PASSWORD="your_password"' >> ~/.zshrc
```

## Output Files

### JSON Plan Export
- Complete 12-month SEO strategy
- Specific tasks with hour estimates
- Monthly breakdown by focus area
- Automation opportunities
- Priority roadmap

### ClickUp CSV Export
- **Task Organization**: Critical, Important, Medium, Strategic lists
- **Proper Hierarchy**: Main tasks with subtasks for large projects
- **Time Estimates**: Converted to minutes (ClickUp format)
- **Due Dates**: Realistic timelines based on priority
- **Recurring Tasks**: Multiple instances for ongoing work
- **Tags**: SEO type, priority, tier classification

## Lead Gear Process Integration

Follows the proven 5-phase methodology:

### Phase 1: Setup & Onboarding (Week 1)
- Client kickoff and tool setup
- Initial audit configuration

### Phase 2: Plan - Research & Develop (Weeks 2-6)  
- Comprehensive audit execution
- Competitor and keyword research
- Strategy development

### Phase 3: Build - Execute The Plan (Weeks 7-12)
- Critical issue resolution
- Technical and on-page optimization
- Content and local SEO implementation

### Phase 4: Measure - Data & Success (Months 3-4)
- Performance monitoring
- Results analysis and reporting
- Strategy refinement

### Phase 5: Learn - Review & Repeat (Month 4+)
- Continuous optimization
- Tier-appropriate recurring tasks
- Strategic pivots and scaling

## Recurring Task Frequencies by Tier

### Starter Tier
- **Technical monitoring**: Quarterly (2.8h)
- **Performance reporting**: Quarterly (2.1h)
- **Keyword review**: Bi-annually (1.4h)

### Business Tier  
- **Technical monitoring**: Monthly (3.5h)
- **Performance reporting**: Monthly (2.8h)
- **Keyword optimization**: Monthly (2.1h)
- **Content strategy**: Quarterly (2.8h)

### Pro Tier
- **Technical optimization**: Monthly (4.2h)
- **Performance reporting**: Monthly (3.5h)
- **Ranking movement analysis**: Monthly (3.5h)
- **CRO monitoring**: Monthly (2.8h)
- **Content strategy**: Monthly (4.2h)
- **Competitive analysis**: Quarterly (3.5h)

## Example Output

```bash
$ seo-business https://allbaysolar.com

Analyzing website: https://allbaysolar.com
Running comprehensive SEO audit for allbaysolar.com...

Audit Results:
  Total Issues Found: 18
  Critical Issues: 3
  Important Issues: 8
  Pages Analyzed: 47
  Estimated Fix Hours: 12.3

Audit recommended: BUSINESS
Using audit-recommended tier: BUSINESS

DATA-DRIVEN PLAN SUMMARY
Client: https://allbaysolar.com/
Tier: Business
Investment: $1,399/month
Base Hours: 35
Actual Hours Needed: 38.2

IMMEDIATE PRIORITY TASKS:
  1. Add keyword-optimized H1 tags to 2 pages (0.3h)
  2. Add unique, optimized title tags to 3 pages (0.5h)
  3. Optimize page speed for 8 slow-loading pages (2.8h)

RECURRING TASKS BY TIER:
  • Technical SEO monitoring and fixes: 3.5h monthly
  • Performance reporting and strategic updates: 2.8h monthly
  • Keyword ranking monitoring and content optimization: 2.1h monthly
  • Content strategy review and planning: 2.8h quarterly

Enhanced SEO plan exported to: allbaysolar.com_audit_based_seo_plan_20250827.json
ClickUp CSV exported to: allbaysolar.com_seo_tasks_clickup_20250827.csv
```

## Commands Reference

| Command | Description |
|---------|-------------|
| `seo-plan <url>` | Full audit and plan generation |
| `seo-starter <url>` | Starter tier plan |
| `seo-business <url>` | Business tier plan |
| `seo-pro <url>` | Pro tier p
