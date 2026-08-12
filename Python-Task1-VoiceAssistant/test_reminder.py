from reminder import set_reminder
import time

print("⏰ Setting reminder for 10 seconds...")

set_reminder(
    10,
    "Your reminder is ready."
)

print("Reminder is running in the background.")

time.sleep(15)

print("Test completed.")