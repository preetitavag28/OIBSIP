import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

if api_key:
    print("✅ OpenWeather API key loaded successfully!")
    print("🔐 API key is hidden for security.")
else:
    print("❌ API key was not found.")