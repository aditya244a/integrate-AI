import logging

logging.basicConfig(
    filename='system_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_system_data(data):
    logging.info(f"Mouse: {data['mouse_position']}, Text: {data['selected_text']}")

def log_ai_action(action):
    logging.info(f"AI Action: {action}")
