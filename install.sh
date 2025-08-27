#!/bin/bash
# Enhanced Lead Gear SEO Strategist Installer with DataForSEO Integration
# Version: 2.0.0

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
INSTALL_DIR="$HOME/.leadgear-seo"
BIN_NAME="seo-plan"
REPO_URL="https://raw.githubusercontent.com/SMBeepay/leadgear-seo-strategist/main"

print_header() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║        Enhanced Lead Gear SEO Strategist Installer           ║"
    echo "║             With DataForSEO Integration v2.0                 ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

check_requirements() {
    print_status "Checking requirements..."
    
    # Check Python 3
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is required but not installed."
        exit 1
    fi
    
    # Check curl
    if ! command -v curl &> /dev/null; then
        print_error "curl is required but not installed."
        exit 1
    fi
    
    print_status "✅ All requirements met"
}

setup_api_credentials() {
    print_status "Setting up DataForSEO API credentials..."
    
    # Check if credentials already exist
    if [ -n "$DATAFORSEO_USERNAME" ] && [ -n "$DATAFORSEO_PASSWORD" ]; then
        print_status "✅ DataForSEO credentials found in environment"
        return 0
    fi
    
    # Detect shell
    SHELL_RC=""
    if [[ "$SHELL" == *"zsh"* ]]; then
        SHELL_RC="$HOME/.zshrc"
    elif [[ "$SHELL" == *"bash"* ]]; then
        SHELL_RC="$HOME/.bashrc"
    else
        SHELL_RC="$HOME/.profile"
    fi
    
    echo ""
    echo -e "${BLUE}DataForSEO API Setup${NC}"
    echo "To get real SEO audit data, you need DataForSEO API credentials."
    echo "1. Sign up at: https://app.dataforseo.com/register"
    echo "2. Get your API username and password"
    echo "3. Enter them below (or press Enter to skip and use demo mode)"
    echo ""
    
    read -p "DataForSEO Username (or Enter to skip): " dfso_username
    if [ -n "$dfso_username" ]; then
        read -s -p "DataForSEO Password: " dfso_password
        echo ""
        
        # Add to shell profile
        echo "" >> "$SHELL_RC"
        echo "# DataForSEO API Credentials for Lead Gear SEO Strategist" >> "$SHELL_RC"
        echo "export DATAFORSEO_USERNAME=\"$dfso_username\"" >> "$SHELL_RC"
        echo "export DATAFORSEO_PASSWORD=\"$dfso_password\"" >> "$SHELL_RC"
        
        print_status "✅ API credentials saved to $SHELL_RC"
        print_warning "You'll need to run 'source $SHELL_RC' or restart your terminal"
    else
        print_warning "Skipping API setup - will run in demo mode"
        echo "You can add credentials later by setting environment variables:"
        echo "  export DATAFORSEO_USERNAME=\"your_username\""
        echo "  export DATAFORSEO_PASSWORD=\"your_password\""
    fi
}

create_install_dir() {
    print_status "Creating installation directory..."
    mkdir -p "$INSTALL_DIR"
    print_status "✅ Created $INSTALL_DIR"
}

download_files() {
    print_status "Downloading Enhanced SEO Strategist files..."
    
    # Download enhanced main script
    if curl -fsSL "$REPO_URL/enhanced_seo_strategist.py" -o "$INSTALL_DIR/seo_strategist.py"; then
        print_status "✅ Downloaded enhanced SEO strategist"
    else
        print_error "Failed to download enhanced SEO strategist"
        exit 1
    fi
    
    # Download interactive helper (if exists)
    if curl -fsSL "$REPO_URL/seo_interactive.py" -o "$INSTALL_DIR/seo_interactive.py" 2>/dev/null; then
        print_status "✅ Downloaded interactive helper"
        chmod +x "$INSTALL_DIR/seo_interactive.py"
    else
        print_warning "Interactive helper not found (optional)"
    fi
    
    # Make executable
    chmod +x "$INSTALL_DIR/seo_strategist.py"
    
    print_status "✅ Downloaded and configured scripts"
}

setup_shell_integration() {
    print_status "Setting up enhanced shell integration..."
    
    # Detect shell
    SHELL_RC=""
    if [[ "$SHELL" == *"zsh"* ]]; then
        SHELL_RC="$HOME/.zshrc"
    elif [[ "$SHELL" == *"bash"* ]]; then
        SHELL_RC="$HOME/.bashrc"
    else
        SHELL_RC="$HOME/.profile"
    fi
    
    # Backup existing shell config
    if [ -f "$SHELL_RC" ]; then
        cp "$SHELL_RC" "$SHELL_RC.backup.$(date +%Y%m%d_%H%M%S)"
        print_status "✅ Backed up existing $SHELL_RC"
    fi
    
    # Add enhanced aliases and functions
    cat >> "$SHELL_RC" << EOF

# Enhanced Lead Gear SEO Strategist Sub-Agent with DataForSEO
export PATH="\$HOME/.leadgear-seo:\$PATH"

# Main enhanced SEO planning command
alias seo-plan='python3 \$HOME/.leadgear-seo/seo_strategist.py'

# Interactive mode (if available)
if [ -f "\$HOME/.leadgear-seo/seo_interactive.py" ]; then
    alias seo-interactive='python3 \$HOME/.leadgear-seo/seo_interactive.py'
fi

# Quick audit and tier recommendation
seo-audit() {
    if [ -z "\$1" ]; then
        echo "Usage: seo-audit <url>"
        echo "Performs comprehensive audit and recommends tier"
        return 1
    fi
    python3 \$HOME/.leadgear-seo/seo_strategist.py "\$1"
}

# Generate plans for specific tiers with audit data
seo-starter() {
    if [ -z "\$1" ]; then
        echo "Usage: seo-starter <url>"
        return 1
    fi
    python3 \$HOME/.leadgear-seo/seo_strategist.py "\$1" --tier starter
}

seo-business() {
    if [ -z "\$1" ]; then
        echo "Usage: seo-business <url>"
        return 1
    fi
    python3 \$HOME/.leadgear-seo/seo_strategist.py "\$1" --tier business
}

seo-pro() {
    if [ -z "\$1" ]; then
        echo "Usage: seo-pro <url>"
        return 1
    fi
    python3 \$HOME/.leadgear-seo/seo_strategist.py "\$1" --tier pro
}

# Demo mode (without API calls)
seo-demo() {
    if [ -z "\$1" ]; then
        echo "Usage: seo-demo <url>"
        echo "Runs SEO analysis in demo mode (no API calls)"
        return 1
    fi
    python3 \$HOME/.leadgear-seo/seo_strategist.py "\$1" --demo-mode
}

# API status check
seo-status() {
    echo "Lead Gear SEO Strategist Status:"
    if [ -n "\$DATAFORSEO_USERNAME" ]; then
        echo "✅ DataForSEO API credentials configured"
        echo "Username: \$DATAFORSEO_USERNAME"
    else
        echo "⚠️  No DataForSEO API credentials found"
        echo "Set DATAFORSEO_USERNAME and DATAFORSEO_PASSWORD environment variables"
        echo "Or run in demo mode with --demo-mode flag"
    fi
    
    if [ -f "\$HOME/.leadgear-seo/seo_strategist.py" ]; then
        echo "✅ Enhanced SEO Strategist installed"
    else
        echo "❌ SEO Strategist not found"
    fi
}

EOF
    
    print_status "✅ Added enhanced shell integration to $SHELL_RC"
}

create_config_file() {
    print_status "Creating configuration file..."
    
    cat > "$INSTALL_DIR/config.json" << EOF
{
    "version": "2.0.0",
    "dataforseo": {
        "api_url": "https://api.dataforseo.com",
        "demo_mode": false,
        "max_pages_crawl": 100,
        "default_location": "United States",
        "default_language": "English"
    },
    "tiers": {
        "starter": {
            "max_additional_hours": 5,
            "hourly_rate": 45
        },
        "business": {
            "max_additional_hours": 10,
            "hourly_rate": 40
        },
        "pro": {
            "max_additional_hours": 15,
            "hourly_rate": 40
        }
    }
}
EOF
    
    print_status "✅ Created configuration file"
}

create_uninstaller() {
    cat > "$INSTALL_DIR/uninstall.sh" << 'EOF'
#!/bin/bash
# Enhanced Lead Gear SEO Strategist Uninstaller

echo "🗑️  Uninstalling Enhanced Lead Gear SEO Strategist..."

# Remove installation directory
rm -rf "$HOME/.leadgear-seo"

echo "⚠️  Please manually remove the Lead Gear SEO section from your shell config:"
if [[ "$SHELL" == *"zsh"* ]]; then
    echo "   nano ~/.zshrc"
elif [[ "$SHELL" == *"bash"* ]]; then
    echo "   nano ~/.bashrc"
else
    echo "   nano ~/.profile"
fi

echo "✅ Uninstallation complete"
EOF
    chmod +x "$INSTALL_DIR/uninstall.sh"
}

test_installation() {
    print_status "Testing enhanced installation..."
    
    # Test if script can run
    if python3 "$INSTALL_DIR/seo_strategist.py" --help &>/dev/null; then
        print_status "✅ Enhanced installation test passed"
    else
        print_warning "Installation may need manual shell reload"
    fi
}

print_success() {
    echo -e "${GREEN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║               🎉 Enhanced Installation Complete!             ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    echo -e "${BLUE}🚀 Enhanced Commands Available:${NC}"
    echo "   seo-audit <url>              - Full audit + tier recommendation"
    echo "   seo-plan <url> [options]     - Generate comprehensive plan"
    echo "   seo-starter/business/pro <url> - Generate tier-specific plan"
    echo "   seo-demo <url>               - Demo mode (no API required)"
    echo "   seo-status                   - Check API credentials & status"
    echo ""
    echo -e "${BLUE}📖 Quick Start:${NC}"
    echo "   # Reload your shell first:"
    if [[ "$SHELL" == *"zsh"* ]]; then
        echo "   source ~/.zshrc"
    elif [[ "$SHELL" == *"bash"* ]]; then
        echo "   source ~/.bashrc"
    else
        echo "   source ~/.profile"
    fi
    echo ""
    echo "   # Check status:"
    echo "   seo-status"
    echo ""
    echo "   # Run full audit:"
    echo "   seo-audit https://client.com"
    echo ""
    echo -e "${BLUE}🔑 DataForSEO API:${NC}"
    echo "   • With API: Get real audit data and specific tasks"
    echo "   • Demo mode: Uses realistic sample data for testing"
    echo "   • Sign up: https://app.dataforseo.com/register"
    echo ""
    echo -e "${BLUE}📋 What's New in v2.0:${NC}"
    echo "   ✅ Real SEO audit data from DataForSEO"
    echo "   ✅ Specific, actionable tasks (not generic)"
    echo "   ✅ Dynamic hour allocation based on actual issues"
    echo "   ✅ Smart tier recommendations from audit results"
    echo "   ✅ Priority-based task roadmaps"
    echo "   ✅ Automation opportunity identification"
    echo ""
    echo -e "${YELLOW}🗑️  To uninstall:${NC} ~/.leadgear-seo/uninstall.sh"
}

# Main installation process
main() {
    print_header
    check_requirements
    create_install_dir
    setup_api_credentials
    download_files
    setup_shell_integration
    create_config_file
    create_uninstaller
    test_installation
    print_success
}

# Run main function
main "$@"
