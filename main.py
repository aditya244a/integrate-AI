from voice_command.voice_recognition import voice_control
from monitor.monitor import monitor_system
from gpt_integration.gpt_handler import query_chatgpt
from voice_command.text_to_speech import speak

if __name__ == "__main__":
    while True:
        command = voice_control()
        if command:
            if "analyze" in command:
                speak("Analyzing your request.")
                response = query_chatgpt(command)
                speak(f"Here is the result: {response}")
            else:
                speak(f"Executing command: {command}")
                # Route to monitor or perform tasks as needed
                monitor_system()
