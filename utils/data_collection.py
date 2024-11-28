import pyautogui
import pyperclip

def collect_system_data():
    mouse_position = pyautogui.position()
    selected_text = pyperclip.paste()
    return {
        'mouse_position': mouse_position,
        'selected_text': selected_text
    }
