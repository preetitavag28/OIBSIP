from email_sender import send_email

print("📧 Starting email test...")

success, message = send_email(
    "tavagpreeti@gmail.com",
    "OASIS Voice Assistant Test",
    "This is a test email sent using the OASIS Infobyte Voice Assistant."
)

print("Result:", message)