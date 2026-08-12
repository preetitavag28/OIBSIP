import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_email(recipient, subject, message):
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")


    if not sender_email or not sender_password:
        return False, "Email credentials are missing."

    try:
        email = EmailMessage()

        email["From"] = sender_email
        email["To"] = recipient
        email["Subject"] = subject

        email.set_content(message)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(email)

        return True, "Email sent successfully."

    except smtplib.SMTPAuthenticationError:
        return False, "Email authentication failed. Check your email credentials."

    except Exception as error:
        return False, f"Unable to send email: {error}"