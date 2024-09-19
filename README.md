# Voice Over Generator using ChatGPT & Eleven Labs

This project is a Python script that utilizes ChatGPT and the Eleven Labs API to generate voiceovers for characters. The script allows users to define custom text prompts to create voiceover scripts with ChatGPT, which are then converted into audio files using Eleven Labs’ voice synthesis.

## Features
- Uses ChatGPT to generate voiceover text.
- Utilizes Eleven Labs API to convert text into natural-sounding voiceovers.
- Customizable voice, prompts, and the number of voiceovers through [Utils.py.](utils.py)

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>

2.	**Install required dependencies**:
    Ensure you have Python installed on your machine. Then, open your terminal and run the following command to install the necessary packages:

    ```bash
    pip install openai elevenlabs

3.	**Set up your API keys**:
    You will need to set up API keys for both Eleven Labs and OpenAI:

    - **Eleven Labs API**: Obtain an API key from [Eleven Labs](https://www.elevenlabs.io).
    - **OpenAI API**: Obtain an API key from [OpenAI](https://openai.com).

    Place these keys in the respective sections of the script or set them as environment variables.

4.	**Modify Utils.py (optional)**:
    You can customize the following parameters in [utils.py](utils.py) with your own values.

## How to Use

1.	After modifying the Utils.py, run the generateVoiceOver.py script:
    ```bash 
    python generateVoiceOver.py

2.	The script will generate a text narrative using ChatGPT, then convert it into a voiceover using Eleven Labs.

3.	The resulting audio files will be saved to the /workspaces/gifTok/lib/assets/voiceOver directory.

## Customization

You can change the following by editing the Utils.py file:

- Voice ID: Change the voice ID to use different voices available from Eleven Labs.
- System Prompt: Modify the system prompt for ChatGPT to suit your specific needs.
- User Prompt: Adjust the user prompt for different types of voiceover content.
- Number of Voiceovers: Set how many different voiceovers you’d like to generate in one run.

### Contribution

Feel free to fork the project and submit pull requests if you have improvements or new features you’d like to add.

[License](/workspaces/generativeVoiceOver/LICENSE)

This project is licensed under the MIT License.
