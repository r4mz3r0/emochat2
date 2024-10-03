from flask import Flask, render_template, request, jsonify
import requests, os

app = Flask(__name__)

# Use the Heroku URL of your RASA server in production
RASA_SERVER_URL = os.environ.get("RASA_SERVER_URL", "http://localhost:5005/webhooks/rest/webhook")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    try:
        # Sending the user's message to the RASA server
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to RASA: {e}")
        return jsonify({"error": "Unable to connect to the chatbot"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
