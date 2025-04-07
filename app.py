from flask import Flask, render_template, request, send_from_directory
import os
from speech import generate_speech

app = Flask(__name__)

# Directory to store generated audio files
AUDIO_DIR = os.path.join(app.root_path, 'static', 'audio')

# Ensure the audio directory exists
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from form
        text = request.form.get('text')
        voice_gender = request.form.get('voice_gender')
        slow = 'slow' in request.form
        volume = request.form.get('volume')

        # Validate text input
        if not text or len(text.strip()) == 0:
            return render_template('index.html', error="Text input cannot be empty.")

        # Generate speech file
        filename = os.path.join(AUDIO_DIR, "output.mp3")
        generate_speech(text, voice_gender=voice_gender, slow=slow, filename=filename)

        return render_template('index.html', audio_file="audio/output.mp3", text=text)

    return render_template('index.html', audio_file=None)

@app.route('/audio/<filename>')
def send_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
