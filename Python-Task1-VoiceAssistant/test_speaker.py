import pyttsx3

engine = pyttsx3.init()

engine.say(
    "Hello. I am your OASIS Infobyte voice assistant. "
    "My voice system is working correctly."
)

engine.runAndWait()