from utils import record_audio, query_whisper_model, query_sentiment_model, generate_prompt, speak_response

def main():
    while True:
        text, filename = record_audio()
        
        whisper_output = query_whisper_model(filename)
        print("Whisper Output:", whisper_output)

        sentiment_output = query_sentiment_model({"inputs": text})
        print("Sentiment Output:", sentiment_output)

        context = f"Whisper Output: {whisper_output}, Sentiment Output: {sentiment_output}"
        answer = generate_prompt(context, text)
        print("Assistant:", answer)

        speak_response(answer)

if __name__ == "__main__":
    main()