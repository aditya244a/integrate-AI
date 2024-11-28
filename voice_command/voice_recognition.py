import speech_recognition as sr
from voice_command.text_to_speech import speak

WAKE_WORD = "jago mangal"
SLEEP_WORD = "sojao mangal"

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  # Debugging message
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Heard: {command}")  # Debugging message
            return command
        except sr.UnknownValueError:
            print("Could not understand audio.")  # Debugging message
            return ""
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")  # Debugging message
            return ""

def voice_control():
    active = False
    print("Voice control started. Waiting for wake word.")  # Debugging message
    while True:
        command = recognize_voice()
        if WAKE_WORD in command:
            print("AI Activated!")  # Debugging message
            speak("AI activated.")
            active = True
        elif SLEEP_WORD in command:
            print("AI Deactivated!")  # Debugging message
            speak("AI deactivated.")
            active = False
        elif active and command:
            print(f"Processing command: {command}")  # Debugging message
            speak(f"Processing command: {command}")
            return command
