#!/bin/bash
# Lead Gear SEO Strategist Installer - Complete Fixed Version
# Version: 2.1.1

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
INSTALL_DIR="$HOME/.leadgear-seo"
REPO_URL="https://raw.githubusercontent.com/SMBeepay/leadgear-seo-strategist/main"

print_header() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║        Lead Gear SEO Strategist Installer v2.1               ║"
    echo "║        Enhanced with DataForSEO & ClickUp Export             ║"
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
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is required but not installed."
        exit 1
    fi
    
    if ! command -v curl &> /dev/null; then
        print_error "curl is required but not installed."
        exit 1
    fi
    
    print_status "✅ All requirements met"
}

create_install_dir() {
    print_status "Creating installation directory..."
    mkdir -p "$INSTALL_DIR"
    print_status "✅ Created $INSTALL_DIR"
}

download_files() {
    print_status "Downloading SEO Strategist files..."
    
    if curl -fsSL "$REPO_URL/seo_strategist.py" -o "$INSTALL_DIR/seo_strategist.py" 2>/dev/null; then
        print_status "✅ Downloaded main SEO strategist script"
    else
        print_error "Failed to download main script from GitHub"
        exit 1
    fi
    
    chmod +x "$INSTALL_DIR/seo_strategist.py"
    print_status "✅ Downloaded and configured scripts"
}

setup_credentials() {
    print_status "Setting up DataForSEO credentials..."
    
    if [ -n "$DATAFORSEO_USERNAME" ] && [ -n "$DATAFORSEO_PASSWORD" ]; then
        print_status "✅ DataForSEO credentials found in environment"
        return 0
    fi
    
    SHELL_RC=""
    if [[ "$SHELL" == *"zsh"* ]]; then
        SHELL_RC="$HOME/.zshrc"
    elif [[ "$SHELL" == *"bash"* ]]; then
        SHELL_RC="$HOME/.bashrc"
    else
        SHELL_RC="$HOME/.profile"
    fi
    
    echo ""
    echo -e "${BLUE}DataForSEO API Setup (Optional)${NC}"
    echo "For real SEO audit data, add DataForSEO API credentials."
    echo "Sign up at: https://app.dataforseo.com/register"
    echo ""
    echo "Add credentials now or skip for demo mode."
    echo ""
    
    read -p "Add DataForSEO credentials now? (y/N): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "DataForSEO Username: " dfso_username
        if [ -n "$dfso_username" ]; then
            read -s -p "DataForSEO Password: " dfso_password
            echo ""
            
            echo "" >> "$SHELL_RC"
            echo "# DataForSEO API Credentials" >> "$SHELL_RC"
            echo "export DATAFORSEO_USERNAME=\"$dfso_username\"" >> "$SHELL_RC"
            echo "export DATAFORSEO_PASSWORD=\"$dfso_password\"" >> "$SHELL_RC"
            
            print_status "✅ API credentials saved"
        fi
    else
        print_status "Skipping API setup - using demo mode"
    fi
}

setup_shell_integration() {
    print_status "Setting up shell integration..."
    
    SHELL_RC=""
    if [[ "$SHELL" == *"zsh"* ]]; then
        SHELL_RC="$HOME/.zshrc"
    elif [[ "$SHELL" == *"bash"* ]]; then
        SHELL_RC="$HOME/.bashrc"
    else
        SHELL_RC="$HOME/.profile"
    fi
    
    if [ -f "$SHELL_RC" ]; then
        cp "$SHELL_RC" "$SHELL_RC.backup.$(date +%Y%m%d_%H%M%S)"
        print_status "✅ Backed up existing $SHELL_RC"
    fi
    
    cat >> "$SHELL_RC" << 'EOF'

# Lead Gear SEO Strategist Sub-Agent
export PATH="$HOME/.leadgear-seo:$PATH"

# Main SEO planning command
alias seo-plan='python3 $HOME/.leadgear-seo/seo_strategist.py'

# Quick commands for each tier
seo-starter() {
    if [ -z "$1" ]; then
        echo "Usage: seo-starter <url>"
        return 1
    fi
    python3 $HOME/.leadgear-seo/seo_strategist.py "$1" --tier starter
}

seo-business() {
    if [ -z "$1" ]; then
        echo "Usage: seo-business <url>"
        return 1
    fi
    python3 $HOME/.leadgear-seo/seo_strategist.py "$1" --tier business
}

seo-pro() {
    if [ -z "$1" ]; then
        echo "Usage: seo-pro <url>"
        return 1
    fi
    python3 $HOME/.leadgear-seo/seo_strategist.py "$1" --tier pro
}

# Audit with ClickUp export
seo-audit() {
    if [ -z "$1" ]; then
        echo "Usage: seo-audit <url>"
        return 1
    fi
    python3 $HOME/.leadgear-seo/seo_strategist.py "$1" --clickup-csv
}

# Status check
seo-status() {
    echo "Lead Gear SEO Strategist Status:"
    if [ -f "$HOME/.leadgear-seo/seo_strategist.py" ]; then
        echo "✅ SEO Strategist installed"
    else
        echo "❌ SEO Strategist not found"
    fi
    
    if [ -n "$DATAFORSEO_USERNAME" ]; then
        echo "✅ DataForSEO API configured: $DATAFORSEO_USERNAME"
    else
        echo "⚠️  Using demo mode (no API credentials)"
    fi
}
EOF
    
    print_status "✅ Added shell integration"
}

create_uninstaller() {
    cat > "$INSTALL_DIR/uninstall.sh" << 'EOF'
#!/bin/bash
echo "🗑️  Uninstalling Lead Gear SEO Strategist..."
rm -rf "$HOME/.leadgear-seo"
echo "⚠️  Manually remove Lead Gear SEO section from shell config"
echo "✅ Uninstallation complete"
EOF
    chmod +x "$INSTALL_DIR/uninstall.sh"
    print_status "✅ Created uninstaller"
}

test_installation() {
    print_status "Testing installation..."
    
    if python3 "$INSTALL_DIR/seo_strategist.py" --help &>/dev/null; then
        print_status "✅ Installation test passed"
    else
        print_warning "Installation test failed - may need shell reload"
    fi
}

print_success() {
    echo -e "${GREEN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🎉 Installation Complete!                 ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    echo -e "${BLUE}📖 Available Commands:${NC}"
    echo "   seo-plan <url>               - Full SEO planning tool"
    echo "   seo-starter <url>            - Starter tier plan"
    echo "   seo-business <url>           - Business tier plan"
    echo "   seo-pro <url>                - Pro tier plan"
    echo "   seo-audit <url>              - Audit + ClickUp CSV export"
    echo "   seo-status                   - Check status"
    echo ""
    echo -e "${BLUE}🚀 Quick Start:${NC}"
    echo "   # Reload shell:"
    if [[ "$SHELL" == *"zsh"* ]]; then
        echo "   source ~/.zshrc"
    elif [[ "$SHELL" == *"bash"* ]]; then
        echo "   source ~/.bashrc"
    else
        echo "   source ~/.profile"
    fi
    echo ""
    echo "   # Test it:"
    echo "   seo-business https://client.com"
    echo ""
    echo -e "${BLUE}🔑 Features:${NC}"
    echo "   ✅ Tier specification with warnings"
    echo "   ✅ 30% reduced hour estimates"
    echo "   ✅ Proper recurring task frequencies"
    echo "   ✅ ClickUp CSV export"
    echo "   ✅ Real audit data (with API) or demo mode"
    echo ""
    echo -e "${YELLOW}🗑️  Uninstall:${NC} ~/.leadgear-seo/uninstall.sh"
}

# Main installation
main() {
    print_header
    check_requirements
    create_install_dir
    download_files
    setup_credentials
    setup_shell_integration
    create_uninstaller
    test_installation
    print_success
}

main "$@"
