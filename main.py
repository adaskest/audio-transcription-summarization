from dotenv import load_dotenv
from fileUpload import upload_to_gcs
from transcriber import transcribe_google
from summarizer import summarize
import os

load_dotenv()

AUDIO_FILE = os.getenv("AUDIO_FILE")
BUCKET_NAME = os.getenv("BUCKET_NAME")
GCS_PATH = os.getenv("GCS_PATH")
TRANSCRIPT_PATH = os.getenv("TRANSCRIPT_PATH")
SUMMARY_PATH = os.getenv("SUMMARY_PATH")


if __name__ == "__main__":
    print("Started file upload to GCS...")
    gcs_uri = upload_to_gcs(BUCKET_NAME, AUDIO_FILE, GCS_PATH)

    print("Started audio file transcription...")
    transcript = transcribe_google(gcs_uri, TRANSCRIPT_PATH)
    print("\n Transcription:\n", transcript)

    print("Started transcription summarization...")
    summary = summarize(transcript, summary_path=SUMMARY_PATH)
    print("\nSummary:\n", summary)
