#!/bin/bash
# Run script for Raspberry Pi LED Control application

# Display banner
echo "====================================="
echo "Raspberry Pi LED Control"
echo "====================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip is not installed."
    echo "Please install pip and try again."
    exit 1
fi

# Check if requirements are installed
if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt not found."
    echo "Please make sure you're in the correct directory."
    exit 1
fi

# Ask if user wants to install dependencies
echo "Would you like to install/update dependencies? (y/n)"
read -r install_deps

if [ "$install_deps" = "y" ] || [ "$install_deps" = "Y" ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    echo "Dependencies installed."
fi

# Ask if user wants to test the LED connection
echo "Would you like to test the LED connection? (y/n)"
read -r test_led

if [ "$test_led" = "y" ] || [ "$test_led" = "Y" ]; then
    echo "Running LED test..."
    python3 test_led.py
    echo "LED test complete."
fi

# Ask if user wants to set up NGROK
echo "Would you like to set up NGROK for remote access? (y/n)"
read -r setup_ngrok

if [ "$setup_ngrok" = "y" ] || [ "$setup_ngrok" = "Y" ]; then
    echo "Setting up NGROK..."
    python3 setup_ngrok.py
    echo "NGROK setup complete."
fi

# Run the application
echo "Starting the LED control application..."
echo "Press Ctrl+C to stop the application."
python3 app.py

# Exit
exit 0