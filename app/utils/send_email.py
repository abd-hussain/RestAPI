from fastapi import FastAPI, BackgroundTasks, HTTPException
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/email")

def send_email(email_to: str, message : str):
    sender_email = "abd.alhaj.hussain@gmail.com"
    password = "yzhhzkyatoagamqu"
    
    msg = EmailMessage()
    msg['Subject'] = "Forgot Password"
    msg['From'] = sender_email
    msg['To'] = email_to
    msg.set_content(
       f"""\
    Your Password Is : {message}   
    """,
         
    )
    
    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
    
    return "email successfully sent"


