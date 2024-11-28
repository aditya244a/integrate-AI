import openai
from api.api_keys import get_api_key

# Initialize OpenAI API Key
openai.api_key = get_api_key("openai")

def query_chatgpt(prompt):
    """
    Sends a prompt to ChatGPT and returns the response.
    """
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Replace with the GPT model you're using
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error communicating with ChatGPT: {str(e)}"
