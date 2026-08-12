import os
import json
import time
import threading
import webbrowser
import datetime
import smtplib
import ssl
import urllib.parse

import requests
import speech_recognition as sr
import sounddevice as sd
from dotenv import load_dotenv
import pyttsx3


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# ============================================================
# TEXT TO SPEECH
# ============================================================

engine = pyttsx3.init()
engine.setProperty("rate", 165)


def speak(text):
    """Speak and display assistant response."""

    print(f"Assistant: {text}")

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as error:
        print(f"Text-to-speech error: {error}")


# ============================================================
# CUSTOM COMMANDS
# ============================================================

def load_custom_commands():
    """Load commands from commands.json."""

    file_path = "commands.json"

    if not os.path.exists(file_path):
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return {}


custom_commands = load_custom_commands()


# ============================================================
# MICROPHONE
# ============================================================

SAMPLE_RATE = 16000
RECORD_SECONDS = 5


def listen():
    """
    Record audio using sounddevice and convert it to text
    using SpeechRecognition's Google recognizer.
    """

    recognizer = sr.Recognizer()

    print("\n🎤 Listening...")

    try:

        audio_data = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        print("🔄 Converting speech to text...")

        audio = sr.AudioData(
            audio_data.tobytes(),
            SAMPLE_RATE,
            2
        )

        command = recognizer.recognize_google(audio)

        command = command.lower().strip()

        print(f"You: {command}")

        return command

    except sr.UnknownValueError:

        speak("Sorry, I couldn't understand you. Please repeat.")
        return ""

    except sr.RequestError:

        speak("Speech recognition service is unavailable.")
        return ""

    except Exception as error:

        print(f"Microphone error: {error}")
        speak("There was a microphone error. Please try again.")
        return ""


# ============================================================
# WEATHER
# ============================================================

def get_weather(city):
    """Get current weather using OpenWeatherMap."""

    if not WEATHER_API_KEY:

        return "The weather API key is missing."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code == 401:
            return "The weather API key is invalid."

        if response.status_code == 404:
            return f"I couldn't find the city {city}."

        if response.status_code != 200:
            return "Unable to get weather information right now."

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9 / 5) + 32

        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        result = (
            f"The weather in {city} is {condition}. "
            f"The temperature is {temperature_c:.1f} degrees Celsius "
            f"or {temperature_f:.1f} degrees Fahrenheit. "
            f"Humidity is {humidity} percent. "
            f"Wind speed is {wind_speed} meters per second."
        )

        return result

    except requests.exceptions.Timeout:

        return "The weather request timed out."

    except requests.exceptions.RequestException:

        return "There was a network error while getting the weather."

    except Exception as error:

        print(f"Weather error: {error}")
        return "Unable to retrieve weather information."


def weather_command(command):
    """Handle weather requests."""

    city = ""

    phrases = [
        "what is the weather in ",
        "what's the weather in ",
        "weather in ",
        "weather for ",
        "tell me the weather in "
    ]

    for phrase in phrases:

        if phrase in command:

            city = command.split(phrase, 1)[1].strip()
            break

    if not city:

        speak("Please tell me the city name.")

        city = input("Enter city name: ").strip()

    if city:

        result = get_weather(city)
        speak(result)


# ============================================================
# WEB SEARCH
# ============================================================

def search_web(command):
    """Open a Google search."""

    search_phrases = [
        "search ",
        "search for ",
        "google "
    ]

    query = ""

    for phrase in search_phrases:

        if command.startswith(phrase):

            query = command[len(phrase):].strip()
            break

    if query:

        speak(f"Searching the web for {query}.")

        encoded_query = urllib.parse.quote_plus(query)

        url = f"https://www.google.com/search?q={encoded_query}"

        webbrowser.open(url)

    else:

        speak("Please tell me what you want me to search for.")


# ============================================================
# REMINDER
# ============================================================

def reminder_alert(message):
    """Speak reminder message."""

    speak(f"Reminder: {message}")


def set_reminder(command):
    """
    Set a reminder.

    Example:
    set reminder for 10 seconds to drink water
    """

    words = command.split()

    seconds = None

    for index, word in enumerate(words):

        try:

            if word.isdigit():

                number = int(word)

                if index + 1 < len(words):

                    unit = words[index + 1]

                    if "second" in unit:
                        seconds = number

                    elif "minute" in unit:
                        seconds = number * 60

                    elif "hour" in unit:
                        seconds = number * 3600

                break

        except ValueError:
            pass

    if seconds is None:

        speak(
            "Please say the reminder duration, "
            "for example, set a reminder for 10 seconds."
        )

        return

    message = "your reminder"

    if " to " in command:

        message = command.split(" to ", 1)[1].strip()

    speak(f"Reminder set for {seconds} seconds.")

    timer = threading.Timer(
        seconds,
        reminder_alert,
        args=[message]
    )

    timer.daemon = True
    timer.start()


# ============================================================
# EMAIL
# ============================================================

def send_email(recipient, subject, message):
    """Send an email using Gmail SMTP."""

    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:

        return "Email credentials are missing."

    try:

        smtp_server = "smtp.gmail.com"
        smtp_port = 465

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            smtp_server,
            smtp_port,
            context=context
        ) as server:

            server.login(
                EMAIL_ADDRESS,
                EMAIL_PASSWORD
            )

            email_message = (
                f"Subject: {subject}\n\n"
                f"{message}"
            )

            server.sendmail(
                EMAIL_ADDRESS,
                recipient,
                email_message
            )

        return "Email sent successfully."

    except smtplib.SMTPAuthenticationError:

        return "Email authentication failed. Please check your email and app password."

    except Exception as error:

        print(f"Email error: {error}")

        return "I couldn't send the email."


def email_command():
    """
    Collect email details using voice input.
    """

    speak("Who should I send the email to?")

    recipient = listen()

    if not recipient:

        return

    # Simple conversion if speech says "at" and "dot"
    recipient = recipient.replace(" at ", "@")
    recipient = recipient.replace(" dot ", ".")

    speak("What should be the subject?")

    subject = listen()

    if not subject:

        return

    speak("What should I say in the email?")

    message = listen()

    if not message:

        return

    speak("Sending the email now.")

    result = send_email(
        recipient,
        subject,
        message
    )

    speak(result)


# ============================================================
# CUSTOM COMMANDS
# ============================================================

def check_custom_commands(command):
    """Check commands.json for user-defined commands."""

    for command_name, url in custom_commands.items():

        if command_name.lower() in command:

            speak(f"Opening {command_name}.")

            webbrowser.open(url)

            return True

    return False


# ============================================================
# DATE
# ============================================================

def tell_date():

    today = datetime.datetime.now()

    date_text = today.strftime(
        "%A, %d %B %Y"
    )

    speak(f"Today is {date_text}.")


# ============================================================
# TIME
# ============================================================

def tell_time():

    current_time = datetime.datetime.now()

    time_text = current_time.strftime(
        "%I:%M %p"
    )

    speak(f"The current time is {time_text}.")


# ============================================================
# MAIN ASSISTANT
# ============================================================

def main():

    print("\n" + "=" * 55)

    print(
        "        OASIS INFOBYTE VOICE ASSISTANT"
    )

    print("=" * 55)

    speak(
        "Hello! I am your OASIS Infobyte voice assistant. "
        "You can say hello, ask for the time or date, "
        "search the web, ask for the weather, "
        "set a reminder, or send an email."
    )

    while True:

        command = listen()

        if not command:
            continue

        # ----------------------------------------------------
        # GOODBYE
        # ----------------------------------------------------

        if any(word in command for word in [
            "goodbye",
            "exit",
            "quit",
            "stop"
        ]):

            speak(
                "Goodbye! Thank you for using the OASIS voice assistant."
            )

            break

        # ----------------------------------------------------
        # HELLO
        # ----------------------------------------------------

        elif (
            "hello" in command
            or "hi assistant" in command
            or "hey assistant" in command
        ):

            speak(
                "Hello! I am ready to help you."
            )

        # ----------------------------------------------------
        # TIME
        # ----------------------------------------------------

        elif "time" in command:

            tell_time()

        # ----------------------------------------------------
        # DATE
        # ----------------------------------------------------

        elif "date" in command or "today" in command:

            tell_date()

        # ----------------------------------------------------
        # WEATHER
        # ----------------------------------------------------

        elif (
            "weather" in command
            or "temperature in" in command
        ):

            weather_command(command)

        # ----------------------------------------------------
        # REMINDER
        # ----------------------------------------------------

        elif (
            "set reminder" in command
            or "set a reminder" in command
            or "remind me" in command
        ):

            set_reminder(command)

        # ----------------------------------------------------
        # EMAIL
        # ----------------------------------------------------

        elif (
            "send email" in command
            or "send an email" in command
            or "email someone" in command
        ):

            email_command()

        # ----------------------------------------------------
        # WEB SEARCH
        # ----------------------------------------------------

        elif (
            command.startswith("search ")
            or command.startswith("search for ")
            or command.startswith("google ")
        ):

            search_web(command)

        # ----------------------------------------------------
        # CUSTOM COMMANDS
        # ----------------------------------------------------

        elif check_custom_commands(command):

            pass

        # ----------------------------------------------------
        # UNKNOWN COMMAND
        # ----------------------------------------------------

        else:

            speak(
                "I don't know that command yet. "
                "You can ask me for the time, date, "
                "weather, a web search, a reminder, "
                "or an email."
            )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()