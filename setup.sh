#!/bin/bash

# Update package index
echo "Updating package index..."
sudo apt update

# Install necessary packages
echo "Installing required packages..."
sudo apt install -y curl wget git

# Check for SSL installation
if ! dpkg -l | grep -q "openssl"; then
    echo "Installing OpenSSL..."
    sudo apt install -y openssl
else
    echo "OpenSSL is already installed."
fi

# Any other setup steps can be added here

echo "Setup completed successfully."