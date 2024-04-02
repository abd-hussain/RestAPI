import firebase_admin
from firebase_admin import credentials, messaging

# cred = credentials.Certificate("./app/utils/firebase_notifications/serviceAccountKey.json")

# firebase_admin.initialize_app(cred, name='legalzhub')

def send_push_notification(token, title, body):
    app = firebase_admin.get_app('legalzhub')
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message, app=app)
    print('Successfully sent message:', response)