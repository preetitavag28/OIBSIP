import threading
import time
import pyttsx3

engine = pyttsx3.init()


def speak(text):
    print(f"\n🔔 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def set_reminder(seconds, message):
    def reminder():

        time.sleep(seconds)

        speak(f"Reminder: {message}")

    reminder_thread = threading.Thread(
        target=reminder,
        daemon=True
    )

    reminder_thread.start()