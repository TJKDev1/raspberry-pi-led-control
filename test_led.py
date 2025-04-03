"""
Simple test script to verify the LED connection to the Raspberry Pi.
This script will blink the LED 5 times to confirm that the hardware is set up correctly.
"""

import time
import RPi.GPIO as GPIO
from config import LED_PIN, GPIO_MODE

def setup_gpio():
    """Set up the GPIO pin."""
    # Set GPIO mode (BCM or BOARD)
    if GPIO_MODE == 'BCM':
        GPIO.setmode(GPIO.BCM)
    else:
        GPIO.setmode(GPIO.BOARD)
        
    # Suppress warnings if the channel is already in use
    GPIO.setwarnings(False)
    
    # Set up the LED pin as an output
    GPIO.setup(LED_PIN, GPIO.OUT)
    
    # Ensure LED is off to start
    GPIO.output(LED_PIN, GPIO.LOW)

def blink_led(times=5, delay=0.5):
    """Blink the LED a specified number of times."""
    for _ in range(times):
        # Turn LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(delay)
        
        # Turn LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(delay)

def cleanup():
    """Clean up GPIO resources."""
    GPIO.cleanup()
    print("GPIO cleanup complete")

if __name__ == "__main__":
    try:
        print(f"Testing LED on GPIO pin {LED_PIN}")
        print("The LED should blink 5 times")
        
        # Set up GPIO
        setup_gpio()
        
        # Blink the LED
        blink_led()
        
        print("Test complete! If the LED blinked 5 times, your hardware setup is correct.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Clean up GPIO resources
        cleanup()