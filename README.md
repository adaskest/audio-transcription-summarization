# Lithuanian Audio Transcriber & Summarizer

This project transcribes Lithuanian-language audio using Google Cloud Speech-to-Text and summarizes the result using OpenAI GPT-4. Audio is uploaded to Google Cloud Storage (GCS), transcribed using the long-running recognizer, and summarized via the OpenAI API. All configuration is stored securely in environment variables.

## Features

- Uploads audio to Google Cloud Storage (GCS)
- Transcribes Lithuanian audio using `long_running_recognize`
- Generates a Lithuanian summary using OpenAI's GPT-4
- Caches results in local files
- Configurable via `.env` file

## Technologies Used

- Python 3.9+
- Google Cloud Speech-to-Text API
- Google Cloud Storage API
- OpenAI API (GPT-4 or GPT-3.5)
- `python-dotenv`

## Setup Instructions

### 1. Clone the repository and create a virtual environment

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Create a .env file

```
OPENAI_API_KEY=your-openai-api-key
GOOGLE_APPLICATION_CREDENTIALS=credentials.json

AUDIO_FILE=audio.wav
BUCKET_NAME=your-gcs-bucket-name
GCS_PATH=uploads/audio.wav
TRANSCRIPT_PATH=responses/transcript.txt
SUMMARY_PATH=responses/summary.txt
```

### 3. Run the Project

```
python main.py
```
