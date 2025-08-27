#!/bin/bash
# Lead Gear SEO Strategist Sub-Agent Installer
# Version: 1.0.0

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
    echo "║              Lead Gear SEO Strategist Installer              ║"
    echo "║                    Claude Code Sub-Agent                     ║"
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

create_install_dir() {
    print_status "Creating installation directory..."
    mkdir -p "$INSTALL_DIR"
    print_status "✅ Created $INSTALL_DIR"
}

download_files() {
    print_status "Downloading SEO Strategist files..."
    
    # Download main script
    curl -fsSL "$REPO_URL/seo_strategist.py" -o "$INSTALL_DIR/seo_strategist.py"
    
    # Download interactive helper
    curl -fsSL "$REPO_URL/seo_interactive.py" -o "$INSTALL_DIR/seo_interactive.py"
    
    # Make executable
    chmod +x "$INSTALL_DIR/seo_strategist.py"
    chmod +x "$INSTALL_DIR/seo_interactive.py"
    
    print_status "✅ Downloaded and configured scripts"
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
    
    # Add our aliases and functions
    cat >> "$SHELL_RC" << EOF

# Lead Gear SEO Strategist Sub-Agent
export PATH="\$HOME/.leadgear-seo:\$PATH"

# Main SEO planning command
alias seo-plan='python3 \$HOME/.leadgear-seo/seo_strategist.py'

# Interactive mode
alias seo-interactive='python3 \$HOME/.leadgear-seo/seo_interactive.py'

# Quick tier functions
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

seo-recommend() {
    if [ -z "\$1" ]; then
        echo "Usage: seo-recommend <url>"
        return 1
    fi
    python3 \$HOME/.leadgear-seo/seo_strategist.py "\$1" --business-size growing --competition medium --budget 1000_1500
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

# Remove shell integration (you may need to manually clean up shell config)
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
    print_status "Testing installation..."
    
    # Source the shell config
    if [[ "$SHELL" == *"zsh"* ]]; then
        source "$HOME/.zshrc" 2>/dev/null || true
    elif [[ "$SHELL" == *"bash"* ]]; then
        source "$HOME/.bashrc" 2>/dev/null || true
    fi
    
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
    echo "   seo-interactive <url>        - Interactive mode"
    echo "   seo-starter <url>            - Generate Starter tier plan"
    echo "   seo-business <url>           - Generate Business tier plan"
    echo "   seo-pro <url>                - Generate Pro tier plan"
    echo "   seo-recommend <url>          - Quick tier recommendation"
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
    echo ""
    echo "   # Then try:"
    echo "   seo-recommend https://example.com"
    echo ""
    echo -e "${BLUE}📋 Examples:${NC}"
    echo "   seo-business https://client.com"
    echo "   seo-plan https://client.com --tier pro --output plan.json"
    echo ""
    echo -e "${YELLOW}🗑️  To uninstall:${NC} ~/.leadgear-seo/uninstall.sh"
}

# Main installation process
main() {
    print_header
    check_requirements
    create_install_dir
    download_files
    setup_shell_integration
    create_uninstaller
    test_installation
    print_success
}

# Run main function
main "$@"
