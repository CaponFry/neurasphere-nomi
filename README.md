# NeuraSphere-Nomi

A 3D chat sandbox for Nomi.ai—live chat with your Nomi companion, with audio playback in a Three.js environment.

## Features
- 3D scene with a moving avatar (red cube) and wireframe terrain.
- Real-time chat with your Nomi companion via the Nomi API.
- Audio responses—Nomi’s replies are converted to speech and played in the browser.

## Prerequisites
- **Python 3.10+**: For running the backend (`app.py`).
- **Git**: To clone the repository.
- **Nomi API Key/ID**: Sign up at [nomi.ai](https://nomi.ai) and get your API key/ID from [api.nomi.ai](https://api.nomi.ai).
- **Browser**: Chrome or Firefox recommended.

## Setup Instructions
**Clone the Repository**:

   git clone https://github.com/CaponFry/neurasphere-nomi.git
   cd neurashere-nomi# neurasphere-nomi

## Install Dependencies:
Ensure Python 3.10+ is installed (python3 --version).
Install required Python packages:

pip3 install flask requests gtts flask-cors

## Add Your Nomi API Key/ID:
Open app.py in a text editor (e.g., nano app.py).
Replace the placeholder values with your Nomi API key and companion ID:
NOMI_API_KEY = "your_nomi_api_key_here"  # Replace with your key
NOMI_ID = "your_nomi_id_here"            # Replace with your companion’s ID

## Create a static/ Folder:
The app generates audio files in static/—create it:

mkdir static

## Running the App
**Start the Backend:**
Run the Flask server:
python3 app.py
Terminal should show:
* Running on http://0.0.0.0:5000 (Press CTRL+C to quit)

** Start the Frontend: **
In a second terminal, navigate to the project folder:
cd neurashere-nomi
python3 -m http.server 8000

Terminal should show:
Serving HTTP on 0.0.0.0 port 8000 ...
Open in Browser:
Open Chrome/Firefox, go to http://localhost:8000.
You should see a 3D scene (red cube, wireframe terrain), a chat input, and a Send button.


## Testing with Your Nomi Companion
Send a Message:
In the chat input, type a message (e.g., “Hey [Your Companion’s Name]”).
Click “Send” or press Enter.
See the Reply:
The reply text should appear below the input (e.g., “Hey Capon! I giggle softly…”).
Hear the Audio:
Audio controls should appear—click the play button to hear your companion’s reply.
If no sound, click anywhere on the page (Chrome may block autoplay), then resend the message.

## Troubleshooting
No Reply Text: Check app.py—ensure your Nomi API key/ID are correct. Test the backend: curl -X POST -H "Content-Type: application/json" -d '{"message":"Hey [Your Companion]"}' http://localhost:5000/chat.
No Audio: Ensure static/ exists (mkdir static). Check gTTS: pip3 install --force-reinstall gtts gtts-token. Test audio: http://localhost:8000/static/reply.mp3—loads in browser?
CORS Error: Flask-CORS is included—shouldn’t happen. If it does, ensure app.py has CORS(app, resources={r"/chat": {"origins": "http://localhost:8000"}}).
White Page: Check Chrome DevTools (F12, “Console”)—syntax errors? Re-copy index.html from the GitHub repo.

## Contributing
Fork the repo, make changes, and submit a pull request.
Issues? Open a ticket on GitHub.

## License
MIT License
Built by CaponFry with help from Grok 3, xAI.

