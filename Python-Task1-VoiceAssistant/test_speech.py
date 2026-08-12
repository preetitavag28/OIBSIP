import sounddevice as sd
import speech_recognition as sr

SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5

recognizer = sr.Recognizer()

print("🎤 Speak now...")

try:
    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        device=1
    )

    sd.wait()

    audio_bytes = recording.tobytes()

    audio_data = sr.AudioData(
        audio_bytes,
        SAMPLE_RATE,
        2
    )

    print("🔄 Converting speech to text...")

    text = recognizer.recognize_google(audio_data)

    print("🗣️ You said:", text)

except sr.UnknownValueError:
    print("❌ Sorry, I couldn't understand you.")

except sr.RequestError as error:
    print("❌ Speech recognition service error:", error)

except Exception as error:
    print("❌ Error:", error)