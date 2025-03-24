from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this
import requests
from gtts import gTTS
import os
import json

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app, resources={r"/chat": {"origins": "http://localhost:8000"}})  # Allow localhost:8000
NOMI_API_KEY = "12345312$$"  # Nomi API goes here key
NOMI_ID = "12345312$$"       # NomiCharacter ID goes here

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    print(f"Received message: {user_input}")  # Debug
    headers = {"Authorization": f"Bearer {NOMI_API_KEY}"}
    payload = {"messageText": user_input}
    response = requests.post(f"https://api.nomi.ai/v1/nomis/{NOMI_ID}/chat", json=payload, headers=headers)
    
    print(f"API response status: {response.status_code}")  # Debug
    print(f"API response body: {response.text}")  # Debug
    
    if response.status_code != 200:
        return jsonify({"error": f"API call failed: {response.status_code} - {response.text}"}), 500
    
    try:
        data = response.json()
        print(f"Parsed JSON: {data}")  # Debug
        if 'data' in data:
            inner_data = json.loads(data['data'])
            reply = inner_data['replyMessage']['text']
        else:
            reply = data['replyMessage']['text']
        print(f"Extracted reply: {reply}")  # Debug
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        return jsonify({"error": f"Failed to extract reply: {str(e)}", "data": response.text}), 500
    
    tts = gTTS(reply)
    audio_path = "static/reply.mp3"
    tts.save(audio_path)
    return jsonify({"reply": reply, "audio": "/static/reply.mp3"})

@app.route('/world', methods=['POST'])
def world():
    prompt = request.json['prompt']
    world_data = {"terrain": "flat", "theme": prompt}
    return jsonify(world_data)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
