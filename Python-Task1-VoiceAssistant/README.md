# OASIS Infobyte Voice Assistant

## Project Overview

This project is a Python-based voice assistant developed as part of the OASIS Infobyte Python Programming Internship.

The assistant listens to spoken commands, converts speech to text, performs useful actions, and responds using text-to-speech.

## Features

### Beginner Tier

* Voice input using SpeechRecognition
* Greeting response for "Hello"
* Current time
* Current date
* Web search using the user's spoken topic
* Error handling when speech is not understood
* Text-to-speech responses using pyttsx3

### Advanced Tier

* Weather information using OpenWeatherMap API
* Email sending using SMTP
* Timed voice reminders
* Custom commands using a JSON configuration file
* Secure API and email credentials using environment variables

## Technologies Used

* Python 3.14
* SpeechRecognition
* SoundDevice
* NumPy
* pyttsx3
* Requests
* python-dotenv
* OpenWeatherMap API
* SMTP
* JSON
* Threading

## Project Structure

```text
Python-Task1-VoiceAssistant/
│
├── assistant.py
├── weather.py
├── email_sender.py
├── test_weather.py
├── test_email.py
├── test_microphone.py
├── test_speech.py
├── test_speaker.py
├── commands.json
├── .env
├── .gitignore
└── README.md
```

## How to Run

### 1. Create and activate the virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install --no-cache-dir SpeechRecognition pyttsx3 requests python-dotenv sounddevice numpy
```

### 3. Configure environment variables

Create a `.env` file:

```text
WEATHER_API_KEY=your_weather_api_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
```

Never upload the `.env` file to GitHub.

### 4. Run the assistant

```powershell
python assistant.py
```

## Example Voice Commands

```text
Hello

What is the time?

What is the date?

Search Python programming

What is the weather in Belagavi?

Set a reminder for 10 seconds to drink water

Open YouTube

Send an email

Goodbye
```

## Privacy Considerations

The application processes microphone audio only when the user activates the listening function.

Speech is converted to text using the speech recognition service.

The application uses an external weather API when the user requests weather information.

Email credentials and API keys are stored in environment variables and are not hard-coded in the source code.

The `.env` file should not be shared publicly or committed to GitHub.

## Error Handling

The assistant handles:

* Unrecognized speech
* Speech recognition service errors
* Microphone errors
* Invalid weather API keys
* Invalid city names
* Weather network timeouts
* Missing email credentials
* Email authentication failures
* Invalid custom command configuration

## Internship Task

**Organization:** OASIS Infobyte

**Track:** Python Programming

**Task:** Task 1 - Voice Assistant

**Developer:** Preeti Tavag
