import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi import FastAPI, BackgroundTasks

conf = ConnectionConfig(
    MAIL_USERNAME="abd.alhaj.hussain",
    MAIL_PASSWORD="lzwoirqlsaixbqha",
    MAIL_FROM="abd.alhaj.hussain@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="test",
    USE_CREDENTIALS=True,
    MAIL_SSL_TLS=False,
    MAIL_STARTTLS=False,
    TEMPLATE_FOLDER='./app/utils/templates/email'
)
    
def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body="s",
        subtype='html',
    )
    fm = FastMail(conf)
    background_tasks.add_task(
       fm.send_message, message, template_name='email.html')