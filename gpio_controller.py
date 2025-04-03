"""
GPIO controller module for LED control.
This module handles all interactions with the Raspberry Pi GPIO pins.
"""

import RPi.GPIO as GPIO
from config import LED_PIN, GPIO_MODE

class GPIOController:
    """
    Class to control GPIO pins for LED operation.
    """
    def __init__(self):
        """
        Initialize the GPIO controller.
        Sets up the GPIO mode and configures the LED pin as output.
        """
        # Set GPIO mode (BCM or BOARD)
        if GPIO_MODE == 'BCM':
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)
            
        # Suppress warnings if the channel is already in use
        GPIO.setwarnings(False)
        
        # Set up the LED pin as an output
        GPIO.setup(LED_PIN, GPIO.OUT)
        
        # Initialize LED state as off
        self.turn_off()
        
    def turn_on(self):
        """
        Turn the LED on.
        Returns:
            bool: True if successful
        """
        GPIO.output(LED_PIN, GPIO.HIGH)
        return True
        
    def turn_off(self):
        """
        Turn the LED off.
        Returns:
            bool: True if successful
        """
        GPIO.output(LED_PIN, GPIO.LOW)
        return True
        
    def get_status(self):
        """
        Get the current status of the LED.
        Returns:
            bool: True if LED is on, False if off
        """
        return GPIO.input(LED_PIN) == GPIO.HIGH
        
    def cleanup(self):
        """
        Clean up GPIO resources.
        Should be called when the application exits.
        """
        GPIO.cleanup()

# Create a singleton instance
gpio_controller = GPIOController()