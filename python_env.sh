#!/bin/bash

# Detect the user's distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        echo "$ID"
    else
        echo -e "\nCannot determine your Linux distribution.\n"
        exit 1
    fi
}

# Check if Python is installed
python_check() {
    if python3 --version > /dev/null 2>&1; then
        echo "Python is installed in your system"
        return 0
    else
        echo "Python is not installed"
        return 1
    fi
}

# Check if Pip is installed
pip_check() {
    if pip3 --version > /dev/null 2>&1; then
        echo -e "\nPip is installed in your system\n"
        return 0
    else
        echo "Pip is not installed"
        return 1
    fi
}

# Install Python and Pip based on the detected distribution
python_pip_install() {
    if ! python_check; then
        case $(detect_distro) in
            ubuntu|debian)
                sudo apt update > /dev/null 2>&1
                sudo apt install python3 python3-pip -y > /dev/null 2>&1
            ;;
            centos|rhel)
                sudo yum install -y python3 python3-pip > /dev/null 2>&1
            ;;
            fedora)
                sudo dnf install -y python3 python3-pip > /dev/null 2>&1
            ;;
            *)
                echo -e "\nYour distribution is not supported by this script.\n"
                exit 1
            ;;
        esac
    fi

    if ! pip_check; then
        case $(detect_distro) in
            ubuntu|debian)
                sudo apt install python3-pip -y > /dev/null 2>&1
            ;;
            centos|rhel)
                sudo yum install -y python3-pip > /dev/null 2>&1
            ;;
            fedora)
                sudo dnf install python3-pip -y > /dev/null 2>&1
            ;;
            *)
                echo -e "\nYour distribution is not supported by this script.\n"
                exit 1
            ;;
        esac
    fi
}

# Install required Python modules
modules_install() {
    local MODULES=(
        psutil
        argparse
        logging
        shutil
        os
        matplotlib
        time
        datetime
        re
        subprocess
    )

    # Install Python modules using pip3
    echo "Installing Python modules..."
    for MODULE in "${MODULES[@]}"; do
        if pip3 show "$MODULE" > /dev/null 2>&1; then
            echo "$MODULE is already installed"
        else
            pip3 install "$MODULE"
        fi
    done

    echo "All required packages and modules have been installed."
}

# Main script logic
echo "Start preparing the Python environment..."
python_pip_install
modules_install
