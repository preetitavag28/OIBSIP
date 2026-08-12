# 🎙️ OASIS Infobyte Voice Assistant

A Python-based voice assistant developed as part of the **OASIS Infobyte Python Programming Internship – Task 1**.

The assistant listens to voice commands, converts speech to text, performs useful actions, and responds using text-to-speech.

## ✨ Features

### Beginner Features

* 🎤 Voice input using `SpeechRecognition`
* 🔊 Text-to-speech responses using `pyttsx3`
* 👋 Responds to "Hello"
* 🕐 Tells the current time
* 📅 Tells the current date
* 🌐 Performs web searches using the default browser
* ❌ Handles speech recognition errors gracefully

### Advanced Features

* 🌦️ Real-time weather information using OpenWeatherMap API
* 📧 Send emails using SMTP
* ⏰ Set timed reminders with audible alerts
* 🧠 Basic natural-language command handling
* ⚙️ Custom commands using a JSON configuration file
* 🔐 API credentials stored securely using environment variables

## 🛠️ Technologies Used

* Python 3.14
* SpeechRecognition
* pyttsx3
* Requests
* python-dotenv
* SoundDevice
* OpenWeatherMap API
* SMTP
* JSON
* Webbrowser
* Datetime
* Threading

## 📁 Project Structure

```text
Python-Task1-VoiceAssistant/
│
├── assistant.py
├── weather.py
├── email_sender.py
├── reminder.py
├── commands.json
│
├── test_microphone.py
├── test_speaker.py
├── test_speech.py
├── test_weather.py
├── test_weather_key.py
├── test_email.py
├── test_reminder.py
│
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/preetitavag28/OIBSIP.git
```

### 2. Open the project folder

```bash
cd OIBSIP/Python-Task1-VoiceAssistant
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install SpeechRecognition pyttsx3 requests python-dotenv sounddevice numpy
```

## 🔐 Environment Variables

Create a `.env` file inside the `Python-Task1-VoiceAssistant` folder.

Add your API credentials:

```env
OPENWEATHER_API_KEY=your_openweather_api_key

EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_app_password
```

**Do not upload `.env` to GitHub.**

The `.gitignore` file is configured to prevent sensitive credentials from being committed.

## 🌦️ Weather API

The project uses the **OpenWeatherMap API** to retrieve current weather information.

The weather feature can provide:

* Temperature in Celsius
* Temperature in Fahrenheit
* Humidity
* Weather condition
* Wind speed
* City information

## 📧 Email Feature

The assistant can send an email using SMTP.

For Gmail, an **App Password** should be used instead of your normal Gmail password.

Never store your real password directly in Python source code.

## ⏰ Reminder Feature

The assistant supports timed reminders.

A reminder waits for the specified duration and then provides an audible notification.

## 🎤 Example Voice Commands

You can say:

```text
Hello

What is the time?

What is the date?

Search Python programming

What is the weather in Belagavi?

Set a reminder

Send an email

Goodbye
```

## ▶️ Running the Assistant

Activate the virtual environment and run:

```bash
python assistant.py
```

The assistant will start listening for voice commands.

## 🧪 Testing

Individual components can be tested separately.

### Test microphone

```bash
python test_microphone.py
```

### Test speaker

```bash
python test_speaker.py
```

### Test speech recognition

```bash
python test_speech.py
```

### Test weather

```bash
python test_weather.py
```

### Test email

```bash
python test_email.py
```

### Test reminder

```bash
python test_reminder.py
```

## 🔒 Privacy & Security

This project processes spoken commands through the speech-recognition service used by the application.

API keys and email credentials are stored in environment variables rather than directly in the source code.

The `.env` file should never be committed or shared publicly.

## 🎯 Internship Task

**Program:** OASIS Infobyte Internship

**Track:** Python Programming

**Task:** Task 1 – Voice Assistant

**Developer:** Preeti Tavag

## 📌 Learning Outcomes

Through this project, I practiced:

* Python programming
* Speech recognition
* Text-to-speech systems
* API integration
* Environment variables
* SMTP email integration
* File-based configuration
* Exception handling
* Threading and timers
* Git and GitHub
* Building and testing a Python application

## 🚀 Future Improvements

Possible improvements include:

* More natural language understanding
* Additional voice commands
* More API integrations
* Improved conversation handling
* GUI interface
* Additional smart assistant features

---

⭐ Developed as part of the OASIS Infobyte Python Programming Internship.
