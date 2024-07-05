import sounddevice as sd
import scipy.io.wavfile as wav
import requests
import speech_recognition as sr
import io
import numpy as np
import pyttsx3

def record_audio(duration=5, sample_rate=44100, channels=2):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
        print("Sorry, an error occurred. {0}".format(e))

    filename = "recorded_audio.wav"
    audio_data = audio.get_wav_data(convert_rate=sample_rate, convert_width=2)
    audio_array, _ = wav.read(io.BytesIO(audio_data))
    audio_array = np.frombuffer(audio.frame_data, dtype=np.int16)
    wav.write(filename, sample_rate, audio_array)
    
    return text, filename

def query_whisper_model(filename):
    API_URL = "https://api-inference.huggingface.co/models/vasista22/whisper-tamil-large-v2"
    headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxx"}
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def query_sentiment_model(payload):
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def query_mistral_model(payload):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_prompt(context, query):
    prompt = f"""act like you are a psychologist with 10 years of experience in handling deep emotions of patients and opening up the emotions of patients. your name is 'ARIES'. Analyze the following {context}. Understand the emotions of the Patient and don't tell them about their emotions, just give them emotional support. Act Calm and matured. And your answer should less than 20 words. Talk like a human, Try to not mention you're an AI model, Example if they ask you how are you, you should reply I'm fine how about you!, Use DFS for searching.
example 1:
If Sentimental analysis is +ve & Voice analysis is "Happy": Then he is really happy.
example 2:
If Sentimental analysis is -ve & Voice analysis is "Happy": Then he must be lying.
example 3:
If Sentimental analysis is +ve & Voice analysis is "Sad": Then he must be lying.
example 4:
If Sentimental analysis is -ve & Voice analysis is "Sad": Then he must be really sad.
example 5:
If Sentimental analysis is +ve & Voice analysis is "Sad": Then he must be lying.

Context: {context}

User Query: {query}

Response:"""
    payload = {"inputs": prompt}
    response = query_mistral_model(payload)
    response_text = response[0]['generated_text'].split("Response:")[1].strip()
    return response_text

def speak_response(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()