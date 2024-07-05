# Psychiatrist Bot

## Overview

The Psychiatrist Bot is an AI-driven application designed to assist users in managing their emotions and mental health. It listens to the user's speech, analyzes the emotions conveyed, and provides supportive responses to guide users through their emotions and relieve mental pressure. The bot aims to act as a friend, offering emotional support and understanding.

## Features

- *Speech Recognition*: Captures user speech and converts it to text.
- *Emotion Analysis*: Uses the Whisper model to analyze the emotions conveyed in the user's speech.
- *Sentiment Analysis*: Employs a sentiment analysis model to understand the sentiment behind the user's words.
- *Emotional Support*: Combines the results of emotion and sentiment analysis to provide appropriate emotional support.
- *Text-to-Speech*: Responds to the user using a natural-sounding voice.

## Technologies Used

- *Python*: The primary programming language used for the application.
- *SpeechRecognition*: Library used to capture and convert speech to text.
- *SpeechTranslation*: Library used to capture and translate tamil speech to english text.
- *Sounddevice*: Library for recording audio.
- *Scipy*: Used for handling audio files.
- *Requests*: Library for making HTTP requests to the models.
- *Pyttsx3*: Library for text-to-speech conversion.
- *Hugging Face Models*: Utilized for emotion and sentiment analysis.

## Installation

1. *Clone the Repository*

    bash
    git clone https://github.com/your-username/psychiatrist-bot.git
    cd psychiatrist-bot
    

2. *Install Dependencies*

    bash
    pip install -r requirements.txt
    

3. *Install PortAudio*

    - *Linux*: sudo apt-get install portaudio19-dev
    - *macOS*: brew install portaudio
    - *Windows*: Download and install from the [PortAudio website](http://www.portaudio.com/download.html).

## Usage

1. *Run the Bot*

    bash
    python psychiatrist_bot.py
    

2. *Interaction*

    - Speak to the bot when prompted.
    - The bot will analyze your speech and provide emotional support based on the analysis.

## Configuration

- *API Tokens*: Make sure to replace the placeholder API tokens in the code with your actual Hugging Face API tokens.

## Contributing

We welcome contributions to improve the Psychiatrist Bot. Please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature-name
3. Make your changes and commit them: git commit -m 'Add some feature'
4. Push to the branch: git push origin feature/your-feature-name
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [Hugging Face](https://huggingface.co/) for providing the models used in this project.

---

Feel free to reach out if you have any questions or need further assistance.