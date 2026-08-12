from weather import get_weather

city = input("Enter city name: ")

result = get_weather(city)

print("\n🌦️ Weather Result:")
print(result)