"""
Main Flask application for LED control.
This module sets up the Flask web server and defines the API endpoints.
"""

import atexit
import logging
from flask import Flask, jsonify, render_template, request
from flask_basicauth import BasicAuth
from pyngrok import ngrok
from gpio_controller import gpio_controller
from config import (
    DEBUG, HOST, PORT, 
    BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD, BASIC_AUTH_FORCE,
    NGROK_AUTH_TOKEN
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configure basic authentication
app.config['BASIC_AUTH_USERNAME'] = BASIC_AUTH_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = BASIC_AUTH_PASSWORD
app.config['BASIC_AUTH_FORCE'] = BASIC_AUTH_FORCE
basic_auth = BasicAuth(app)

# Register cleanup function to run on exit
atexit.register(gpio_controller.cleanup)

@app.route('/')
def index():
    """
    Render the main page.
    """
    return render_template('index.html')

@app.route('/api/led', methods=['GET'])
def get_led_status():
    """
    Get the current status of the LED.
    Returns:
        JSON: {"status": true/false}
    """
    status = gpio_controller.get_status()
    return jsonify({"status": status})

@app.route('/api/led', methods=['POST'])
def set_led_status():
    """
    Set the LED status based on the request.
    Expects JSON: {"status": true/false}
    Returns:
        JSON: {"status": true/false, "success": true/false}
    """
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"success": False, "error": "Invalid JSON"}), 400
            
        if 'status' not in data:
            return jsonify({"success": False, "error": "Missing 'status' field"}), 400
            
        status = data['status']
        if status:
            gpio_controller.turn_on()
            logger.info("LED turned ON")
        else:
            gpio_controller.turn_off()
            logger.info("LED turned OFF")
            
        return jsonify({"success": True, "status": status})
    except Exception as e:
        logger.error(f"Error setting LED status: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

def start_ngrok():
    """
    Start ngrok if configured.
    """
    if NGROK_AUTH_TOKEN:
        # Set auth token
        ngrok.set_auth_token(NGROK_AUTH_TOKEN)
        
    # Open a tunnel on the specified port
    public_url = ngrok.connect(PORT).public_url
    logger.info(f"NGROK tunnel established at: {public_url}")
    app.config["BASE_URL"] = public_url

if __name__ == '__main__':
    # Start ngrok if we're running directly
    if not DEBUG:
        start_ngrok()
    
    # Run the Flask app
    app.run(host=HOST, port=PORT, debug=DEBUG)
    
    # When the app exits, clean up ngrok
    ngrok.kill()