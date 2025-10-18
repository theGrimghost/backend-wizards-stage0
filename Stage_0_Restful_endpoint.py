from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
CAT_FACT_API = "https://catfact.ninja/fact"
API_TIMEOUT = 5  # seconds

@app.route('/me', methods=['GET'])
def get_profile():
    """
    Returns user profile with a dynamic cat fact
    """
    try:
        # Fetch cat fact from external API
        response = requests.get(CAT_FACT_API, timeout=API_TIMEOUT)
        response.raise_for_status()
        cat_fact = response.json().get('fact', 'No cat fact available')
    except requests.exceptions.Timeout:
        cat_fact = "Cat fact unavailable at the moment - but cats are awesome anyway! 🐱"
    except requests.exceptions.RequestException as e:
        cat_fact = "Cat fact service is taking a catnap right now. Try again later! 😺"
    
    # Get current UTC timestamp in ISO 8601 format
    timestamp = datetime.utcnow().isoformat() + 'Z'
    
    # Build response
    response_data = {
        "status": "success",
        "user": {
            "email": "lionspride105@gmail.com",
            "name": "Prince Olamide Babalola",
            "stack": "Python/Flask"
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }
    
    return jsonify(response_data), 200

@app.route('/', methods=['GET'])
def home():
    """
    Home route for basic info
    """
    return jsonify({
        "message": "Welcome to the Profile API",
        "endpoint": "/me",
        "method": "GET"
    }), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    """
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)