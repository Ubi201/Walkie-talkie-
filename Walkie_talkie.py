import pyttsx3
import random
import time

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Set voice properties
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Sample police/military-style messages
phrases = [
    "Unit Bravo, what's your status? Over.",
    "Alpha team moving to checkpoint Charlie.",
    "Requesting backup at sector seven, over.",
    "We have a visual on the target.",
    "All units, proceed with caution. Code Red!",
    "Command, do you copy? We are under fire!",
    "Suspect in custody, returning to base.",
    "Tango down! Area secure.",
    "Deploying drones for aerial recon.",
    "Enemy spotted, requesting air support."
]

# Function to simulate radio chatter
def radio_chatter():
    while True:
        message = random.choice(phrases)  # Pick a random message
        print(f"[Radio] {message}")  # Display on screen
        engine.say(message)  # Convert text to speech
        engine.runAndWait()  # Play the message
        time.sleep(random.randint(3, 7))  # Random delay between messages

if __name__ == "__main__":
    print("Simulating Walkie-Talkie AI chatter. Press Ctrl+C to stop.")
    try:
        radio_chatter()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")