"""
NGROK setup helper script for the Raspberry Pi LED Control application.
This script helps users set up NGROK for remote access to the LED control web interface.
"""

import os
import sys
import subprocess
import configparser
from pyngrok import ngrok, conf

def check_ngrok_installed():
    """Check if NGROK is installed."""
    try:
        subprocess.run(["ngrok", "--version"], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def install_ngrok():
    """Provide instructions for installing NGROK."""
    print("NGROK does not appear to be installed.")
    print("\nTo install NGROK:")
    print("1. Visit https://ngrok.com/download")
    print("2. Download the appropriate version for your Raspberry Pi (ARM)")
    print("3. Extract the downloaded file")
    print("4. Move the ngrok executable to a directory in your PATH, e.g.:")
    print("   sudo mv ngrok /usr/local/bin/")
    print("\nAlternatively, you can install NGROK via pip:")
    print("   pip install pyngrok")
    print("   ngrok --version")
    
    choice = input("\nWould you like to attempt installation via pip now? (y/n): ")
    if choice.lower() == 'y':
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pyngrok"], check=True)
            print("NGROK installed successfully via pip!")
            return True
        except subprocess.CalledProcessError:
            print("Failed to install NGROK via pip. Please try the manual installation method.")
            return False
    return False

def get_auth_token():
    """Get the NGROK auth token from the user."""
    print("\nTo use NGROK, you need an auth token.")
    print("If you don't have one, sign up at https://dashboard.ngrok.com/signup")
    print("Then get your auth token from https://dashboard.ngrok.com/get-started/your-authtoken")
    
    token = input("\nEnter your NGROK auth token (or press Enter to skip): ")
    return token.strip()

def update_config_file(token):
    """Update the config.py file with the NGROK auth token."""
    if not token:
        print("No token provided. Skipping config update.")
        return False
        
    try:
        # Read the current config file
        with open('config.py', 'r') as f:
            content = f.read()
            
        # Replace the NGROK_AUTH_TOKEN line
        if "NGROK_AUTH_TOKEN = ''" in content:
            content = content.replace("NGROK_AUTH_TOKEN = ''", f"NGROK_AUTH_TOKEN = '{token}'")
        else:
            # If the format is different, try to find the line and replace it
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'NGROK_AUTH_TOKEN' in line:
                    lines[i] = f"NGROK_AUTH_TOKEN = '{token}'  # Added by setup script"
                    break
            content = '\n'.join(lines)
            
        # Write the updated content back to the file
        with open('config.py', 'w') as f:
            f.write(content)
            
        print("Updated config.py with your NGROK auth token.")
        return True
    except Exception as e:
        print(f"Error updating config file: {str(e)}")
        return False

def test_ngrok_connection():
    """Test the NGROK connection."""
    try:
        print("\nTesting NGROK connection...")
        # Start a temporary NGROK tunnel on port 5000
        public_url = ngrok.connect(5000).public_url
        print(f"NGROK tunnel established successfully at: {public_url}")
        print("Your LED control application will be accessible at this URL when running.")
        
        # Disconnect the tunnel
        ngrok.disconnect(public_url)
        ngrok.kill()
        return True
    except Exception as e:
        print(f"Error testing NGROK connection: {str(e)}")
        return False

def main():
    """Main function."""
    print("=" * 60)
    print("NGROK Setup Helper for Raspberry Pi LED Control")
    print("=" * 60)
    print("This script will help you set up NGROK for remote access to your LED control application.")
    
    # Check if NGROK is installed
    if not check_ngrok_installed():
        if not install_ngrok():
            print("\nPlease install NGROK manually and run this script again.")
            return
    
    # Get the auth token
    token = get_auth_token()
    
    if token:
        # Set the auth token in NGROK
        conf.get_default().auth_token = token
        
        # Update the config file
        update_config_file(token)
        
        # Test the connection
        test_ngrok_connection()
    
    print("\nSetup complete!")
    print("You can now run your LED control application with:")
    print("  python app.py")
    print("\nThe NGROK URL will be displayed in the console when the application starts.")

if __name__ == "__main__":
    main()