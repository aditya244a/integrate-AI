from gpt_integration.gpt_handler import query_chatgpt
from voice_command.text_to_speech import speak

def monitor_system():
    """
    Continuously monitors the system, including mouse position, selected text, etc.
    Routes complex tasks to ChatGPT for advanced processing.
    """
    while True:
        # Example system activity (placeholder data)
        task = "Write a Python script for a REST API"

        # Determine if the task is complex (route to ChatGPT)
        if "Write a Python script" in task:  # Example condition
            speak("This is a complex task. Let me ask ChatGPT.")
            response = query_chatgpt(task)
            speak(f"ChatGPT suggests: {response}")
        else:
            speak(f"Performing task: {task}")

        # Pause before checking again
        time.sleep(1)
