import os
import requests
import openai
from dotenv import load_dotenv
from utils import get_voice_id, numberOf, userPrompt, systemPrompt  # Import from utils

# Load environment variables
load_dotenv()

# Initialize API keys
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate API keys
if not ELEVENLABS_API_KEY:
    raise ValueError("Missing ELEVENLABS_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY")

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

def generate_script() -> str:
    try:
        # Generate a script using GPT-3
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": systemPrompt()},
                {"role": "user", "content": userPrompt()}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating script: {e}")
        return ""

def text_to_speech_file(text: str, output_dir: str, index: int) -> str:
    voice_id = get_voice_id()  # Use the get_voice_id function here
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Use index to create a unique file name
    file_name = f"voiceOver_{index + 1}.mp3"
    file_path = os.path.join(output_dir, file_name)

    # Send request to Eleven Labs
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for bad HTTP status codes
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Voiceover saved at {file_path}")
        return file_path
    except requests.exceptions.RequestException as e:
        print(f"Error during text-to-speech conversion: {e}")
        return None

# Call numberOf to get the integer value
num_iterations = numberOf()  # Ensure this function returns a valid integer

# Loop to generate scripts and convert them to speech
for i in range(num_iterations):
    print(f"Generating script {i + 1} of {num_iterations}")
    script = generate_script()
    if script:  # Proceed only if script is generated successfully
        text_to_speech_file(script, "/workspaces/generativeVoiceOver/lib", i)