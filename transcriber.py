import os
from google.cloud import speech
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)

def transcribe_google(gcs_uri: str, transcript_path: str) -> str:
    try:
        client = speech.SpeechClient()

        audio = speech.RecognitionAudio(uri=gcs_uri)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="lt-LT",
            enable_automatic_punctuation=True,
            audio_channel_count=1,
            speech_contexts=[
                speech.SpeechContext(
                    phrases=[
                        "krepšinis",
                        "Vokietija",
                        "JAV",
                        "3 prieš 3",
                        "5:11",
                        "Dainius Novickas",
                    ],
                ),
            ],
        )

        operation = client.long_running_recognize(config=config, audio=audio)
        response = operation.result(timeout=600)

        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript + " "

        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript)

        return transcript
    except Exception as e:
        return f"Error while calling Google Speech-to-Text API: {str(e)}"
