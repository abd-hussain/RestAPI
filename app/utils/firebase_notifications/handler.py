import firebase_admin
from firebase_admin import credentials, messaging

credMentor = credentials.Certificate("./app/utils/firebase_notifications/serviceMentorAccountKey.json")
credClient = credentials.Certificate("./app/utils/firebase_notifications/serviceClientAccountKey.json")

firebase_admin.initialize_app(credClient, name='client')
firebase_admin.initialize_app(credMentor, name='mentor')


def send_push_notification_mentor(token, title, body):
    app = firebase_admin.get_app('mentor')
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message, app=app)
    print('Successfully sent message:', response)
    
def send_push_notification_client(token, title, body):
    app = firebase_admin.get_app('client')
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message, app=app)
    print('Successfully sent message:', response)