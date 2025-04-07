from gtts import gTTS
import os

def generate_speech(text, voice_gender='male', slow=False, filename='output.mp3'):
    """
    Generates speech from the given text and saves it to the specified filename.

    Parameters:
    - text: The text to be converted to speech.
    - voice_gender: The gender of the voice ('male' or 'female').
    - slow: Whether the speech should be slow or normal.
    - filename: The name of the file where the audio will be saved.
    """
    # Check for empty text
    if not text or len(text.strip()) == 0:
        raise ValueError("Text input cannot be empty")

    # Select voice language/accents for differentiation (though gTTS does not provide true male/female differentiation)
    lang = 'en'
    if voice_gender == 'female':
        lang = 'en'  # Here you could choose another variant (like en-us) for an accent, but not gender

    # Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=slow)

    # Save the audio file
    tts.save(filename)

    # Return the filename for testing purposes
    return filename
