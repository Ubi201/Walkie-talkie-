from gtts import gTTS
import os
import time

# Text to be converted to audio
text = "This is a test walkie-talkie message."

# Create gTTS object
tts = gTTS(text=text, lang='en')

# Save the audio file
audio_file = "walkie_talkie.mp3"
tts.save(audio_file)

# Play the audio file using playsound
os.system(f"playsound {audio_file}")