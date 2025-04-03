/**
 * Raspberry Pi LED Control - Frontend JavaScript
 * Handles the user interface and API communication
 */

// DOM Elements
const ledIndicator = document.getElementById('led-indicator');
const statusText = document.getElementById('status-text');
const toggleBtn = document.getElementById('toggle-btn');
const connectionStatus = document.getElementById('connection-status');
const lastUpdated = document.getElementById('last-updated');

// State
let ledStatus = false;

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    // Initial LED status check
    fetchLedStatus();
    
    // Set up event listeners
    toggleBtn.addEventListener('click', toggleLed);
    
    // Set up periodic status updates
    setInterval(fetchLedStatus, 5000); // Check every 5 seconds
});

/**
 * Fetch the current LED status from the API
 */
async function fetchLedStatus() {
    try {
        const response = await fetch('/api/led');
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        updateUI(data.status);
        updateConnectionStatus(true);
    } catch (error) {
        console.error('Error fetching LED status:', error);
        updateConnectionStatus(false);
    }
}

/**
 * Toggle the LED state
 */
async function toggleLed() {
    // Disable the button during the request
    toggleBtn.disabled = true;
    
    try {
        const newStatus = !ledStatus;
        
        const response = await fetch('/api/led', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ status: newStatus })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.success) {
            updateUI(data.status);
            updateConnectionStatus(true);
        } else {
            console.error('Failed to toggle LED:', data.error);
            alert(`Failed to toggle LED: ${data.error}`);
        }
    } catch (error) {
        console.error('Error toggling LED:', error);
        updateConnectionStatus(false);
    } finally {
        // Re-enable the button
        toggleBtn.disabled = false;
    }
}

/**
 * Update the UI based on the LED status
 */
function updateUI(status) {
    ledStatus = status;
    
    // Update the LED indicator
    if (status) {
        ledIndicator.classList.remove('off');
        ledIndicator.classList.add('on');
        statusText.textContent = 'LED is ON';
    } else {
        ledIndicator.classList.remove('on');
        ledIndicator.classList.add('off');
        statusText.textContent = 'LED is OFF';
    }
    
    // Update the last updated time
    const now = new Date();
    lastUpdated.textContent = now.toLocaleTimeString();
}

/**
 * Update the connection status indicator
 */
function updateConnectionStatus(connected) {
    if (connected) {
        connectionStatus.textContent = 'Connected';
        connectionStatus.classList.remove('disconnected');
    } else {
        connectionStatus.textContent = 'Disconnected';
        connectionStatus.classList.add('disconnected');
    }
}
