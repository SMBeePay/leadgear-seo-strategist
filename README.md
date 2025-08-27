# Lead Gear SEO Strategist Sub-Agent

A Claude Code sub-agent that generates comprehensive 12-month SEO plans based on Lead Gear's service tiers.

## Quick Install

```bash
# One-command install
curl -fsSL https://raw.githubusercontent.com/SMBeePay/leadgear-seo-strategist/main/install.sh | bash
```

## Manual Install

```bash
# Clone the repository
git clone https://github.com/SMBeePay/leadgear-seo-strategist.git
cd leadgear-seo-strategist

# Run the installer
./install.sh
```

## Usage

After installation, use from anywhere in Claude Code:

```bash
# Quick analysis with tier recommendation
seo-plan https://clientwebsite.com --business-size growing --competition medium

# Generate specific tier plans
seo-plan https://client.com --tier business
seo-plan https://client.com --tier pro --output custom_plan.json

# Interactive mode
seo-interactive https://newclient.com
```

## Features

- **Smart Tier Recommendations**: Automatically suggests Starter ($899), Business ($1,399), or Pro ($1,999) tiers
- **12-Month Planning**: Detailed monthly breakdowns following Lead Gear's 5-phase process
- **Hour Allocation**: Precise hour distribution across SEO activities
- **Automation Opportunities**: Identifies tasks that can be automated for efficiency
- **Export Options**: Generate JSON plans for client presentations

## Service Tiers

| Tier | Monthly Investment | Hours/Month | Best For |
|------|-------------------|-------------|----------|
| **Starter** | $899/month | 20 hours | Small businesses, local services, SEO foundation |
| **Business** | $1,399/month | 35 hours | Growing businesses, competitive markets |
| **Pro** | $1,999/month | 50 hours | Established businesses, hands-off growth |

## Lead Gear Process Integration

Follows the proven 5-phase methodology:

1. **Setup & Onboarding** (Week 1)
2. **Plan** - Research, Evaluate & Develop (Weeks 2-6)
3. **Build** - Execute The Plan (Weeks 7-12)
4. **Measure** - Gather Data & Share Success (Months 3-4)
5. **Learn** - Review, Refine & Repeat (Month 4+)

## Requirements

- Python 3.6+
- macOS, Linux, or Windows with WSL
- Claude Code terminal access

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details.
