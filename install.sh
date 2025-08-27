#!/bin/bash
# Lead Gear SEO Strategist Installer - Fixed Version
# Version: 2.1.0

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

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
    
    # Download main script
    if curl -fsSL "$REPO_URL/seo_strategist.py" -o "$INSTALL_DIR/seo_strategist.py" 2>/dev/null; then
        print_status "✅ Downloaded main SEO strategist script"
    else
        print_error "Failed to download main script from GitHub"
        print_status "Please ensure seo_strategist.py is uploaded to your repository"
        exit 1
    fi
    
    # Make executable
    chmod +x "$INSTALL_DIR/seo_strategist.py"
    
    print_status "✅ Downloaded and configured scripts"
}

setup_credentials() {
    print_status "Setting up DataForSEO credentials..."
    
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
    echo -e "${BLUE}DataForSEO API Setup (Optional)${NC}"
    echo "For real SEO audit data, you can add DataForSEO API credentials."
    echo "Sign up at: https://app.dataforseo.com/register"
    echo ""
    echo "You can add credentials now or skip and add them later."
    echo "Without credentials, the tool will use realistic demo data."
    echo ""
    
    read -p "Do you have DataForSEO credentials to add now? (y/N): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "DataForSEO Username: " dfso_username
        if [ -n "$dfso_username" ]; then
            read -s -p "DataForSEO Password: " dfso_password
            echo ""
            
            # Add to shell profile
            echo "" >> "$SHELL_RC"
            echo "# DataForSEO API Credentials for Lead Gear SEO Strategist" >> "$SHELL_RC"
            echo "export DATAFORSEO_USERNAME=\"$dfso_username\"" >> "$SHELL_RC"
            echo "export DATAFORSEO_PASSWORD=\"$dfso_password\"" >> "$SHELL_RC"
            
            print_status "✅ API credentials saved to $SHELL_RC"
            print_warning "Run 'source $SHELL_RC' or restart terminal to activate"
        fi
    else
        print_status "Skipping API setup - will use demo mode"
        echo ""
        echo "To add credentials later, run:"
        echo "  export DATAFORSEO_USERNAME=\"your_username\""
        echo "  export DATAFORSEO_PASSWORD=\"your_password\""
        echo "  echo 'export DATAFORSEO_USERNAME=\"your_username\"' >> $SHELL_RC"
        echo "  echo 'export DATAFORSEO_PASSWORD=\"your_password\"' >> $SHELL_RC"
    fi
}

setup_shell_integration() {
    print_status "Setting up shell integration..."
    
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
    
    # Add aliases and functions
    cat >> "$SHELL_RC" << EOF

# Lead Gear SEO Strategist Sub-Agent
export PATH="\$HOME/.leadgear-seo:\$PATH"

# Main SEO planning command
alias seo-plan='python3 \$HOME/.leadgear-seo/seo_strategist.py'

# Quick commands for each tier
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

# Audit with ClickUp export
seo-audit() {
    if [ -z "\$1" ]; then
        echo "Usage: seo-audit <url>"
        echo "Runs full audit and exports ClickUp CSV"
        return 1
    fi
    python3 \$HOME/.leadgear-seo/seo_strategist.py "\$1" --clickup-csv
}

# Status check
seo-status() {
    echo "Lead Gear SEO Strategist Status:"
    if [ -f "\$HOME/.leadgear-seo/seo_strategist.py" ]; then
        echo "✅ SEO Strategist installed"
    else
        echo "❌ SEO Strategist not found"
    fi
    
    if [ -n "\$DATAFORSEO_USERNAME" ]; then
        echo "✅ DataForSEO API credentials configured"
        echo "Username: \$DATAFORSEO_USERNAME"
    else
        echo "⚠️  DataForSEO API credentials not found"
        echo "Using demo mode for audits"
    fi
}

EOF
    
    print_status "✅ Added shell integration to $SHELL_RC"
}

create_uninstaller() {
    cat > "$INSTALL_DIR/uninstall.sh" << 'EOF'
#!/bin/bash
# Lead Gear SEO Strategist Uninstaller

echo "🗑️  Uninstalling Lead Gear SEO Strategist..."

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
    chmod +x "$INSTALL_DIR/uninstaller.sh"
    print_status "✅ Created uninstaller"
}

test_installation() {
    print_status "Testing installation..."
    
    # Test if script can run
    if python3 "$INSTALL_DIR/seo_strategist.py" --help &>/dev/null; then
        print_status "✅ Installation test passed"
    else
        print_warning "Installation may need manual shell reload"
    fi
}

print_success() {
    echo -e "${GREEN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🎉 Installation Complete!                 ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    echo -e "${BLUE}📖 Available Commands:${NC}"
    echo "   seo-plan <url> [options]     - Full SEO planning tool"
    echo "   seo-starter <url>            - Generate Starter tier plan"
    echo "   seo-business <url>           - Generate Business tier plan"
    echo "   seo-pro <url>                - Generate Pro tier plan"
    echo "   seo-audit <url>              - Full audit + ClickUp CSV export"
    echo "   seo-status                   - Check installation & API status"
    echo ""
    echo -e "${BLUE}🚀 Quick Start:${NC}"
    echo "   # Reload your shell first:"
    if [[ "$SHELL" == *"zsh"* ]]; then
        echo "   source ~/.zshrc"
    elif [[ "$SHELL" == *"bash"* ]]; then
        echo "   source ~/.bashrc"
    else
        echo "   source ~/.profile"
    fi
