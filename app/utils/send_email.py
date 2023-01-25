import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = os.environ.get("email_sender")
email_password = os.environ.get("email_password")
body = """
Test Email """


def send_email_async(subject: str, email_to: str):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_to
    em['Subject'] = "Test"
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_to, em.as_string())





