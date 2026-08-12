import sounddevice as sd
import wave

SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5
OUTPUT_FILE = "test_recording.wav"

print("🎤 Microphone test")
print("Get ready...")

try:
    print("Speak now! Recording for 5 seconds...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        device=1
    )

    sd.wait()

    with wave.open(OUTPUT_FILE, "wb") as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(recording.tobytes())

    print(f"✅ Recording saved as: {OUTPUT_FILE}")

except Exception as error:
    print("❌ Microphone error:", error)