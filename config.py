"""
Configuration settings for the LED control application.
"""

# GPIO Configuration
LED_PIN = 18  # GPIO pin connected to the LED
GPIO_MODE = 'BCM'  # BCM or BOARD

# Flask Configuration
DEBUG = True
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5000

# Security Configuration
BASIC_AUTH_USERNAME = 'admin'
BASIC_AUTH_PASSWORD = 'raspberry'  # Change this in production!
BASIC_AUTH_FORCE = True  # Require authentication for all routes

# NGROK Configuration
NGROK_AUTH_TOKEN = ''  # Add your NGROK auth token here if you have one