API_KEYS = {
    "openai": "enter your gpt api"
}

def get_api_key(service_name):
    return API_KEYS.get(service_name)
