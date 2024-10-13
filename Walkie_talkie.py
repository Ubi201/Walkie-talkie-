from gtts import gTTS
import os
import subprocess

# Text to be converted to audio
text = "Dari 29 minta 34 beri maklumat taiping over."

# Create gTTS object
tts = gTTS(text=text, lang='en')

# Save the audio file
audio_file = "walkie_talkie.mp3"
tts.save(audio_file)

# Play the audio file using mpg123
subprocess.run(["mpg123", audio_file])