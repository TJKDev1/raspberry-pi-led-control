# Raspberry Pi LED Control

A web application to control an LED connected to a Raspberry Pi through a simple web interface. This project allows you to toggle an LED on and off remotely using a web browser.

## Hardware Requirements

- Raspberry Pi 4
- Breadboard
- LED
- Resistor (220-330 ohms)
- Jumper wires

## Circuit Setup

1. Connect a GPIO pin (default: GPIO 18) to a resistor on the breadboard
2. Connect the resistor to the LED's anode (longer leg)
3. Connect the LED's cathode (shorter leg) to a ground (GND) pin on the Raspberry Pi

## Software Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Clone this repository or download the files to your Raspberry Pi

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) Configure the application by editing `config.py`:
   - Change the GPIO pin if needed
   - Set your NGROK auth token if you have one
   - Change the authentication credentials (recommended for security)

### Running the Application

1. Start the application:
   ```
   python app.py
   ```

2. Access the web interface:
   - Locally: http://localhost:5000 or http://[raspberry_pi_ip]:5000
   - Remotely (if using NGROK): Check the console output for the NGROK URL

3. Log in with the credentials specified in `config.py` (default: admin/raspberry)

## Using NGROK for Remote Access

This application supports NGROK for exposing your local server to the internet. To use NGROK:

1. Sign up for an NGROK account at https://ngrok.com/
2. Get your auth token from the NGROK dashboard
3. Add your auth token to the `NGROK_AUTH_TOKEN` variable in `config.py`
4. Run the application as normal

The NGROK URL will be displayed in the console when the application starts.

## Security Considerations

- Change the default username and password in `config.py`
- Consider using HTTPS for secure communication
- Be cautious about exposing your Raspberry Pi to the internet

## Troubleshooting

- If you encounter permission issues with GPIO, try running the application with sudo:
  ```
  sudo python app.py
  ```
- Make sure the LED is connected to the correct GPIO pin as specified in `config.py`
- Check the console output for any error messages

## License

This project is open source and available under the MIT License.