# import firebase_admin
# from firebase_admin import credentials, messaging

# cred = credentials.Certificate("./app/utils/firebase_notifications/serviceAccountKey.json")

# firebase_admin.initialize_app(cred, name='legalzhub')

# def send_push_notification(token, title, body):
#     try:
#         if not firebase_admin._apps.get('legalzhub'):
#             raise ValueError("Firebase app 'legalzhub' is not initialized.")
    
#         app = firebase_admin.get_app('legalzhub')
    
#         message = messaging.Message(
#             notification=messaging.Notification(
#             title=title,
#             body=body,
#             ),
#             token=token,
#         )

#         response = messaging.send(message, app=app)
#         print('Successfully sent message:', response)
#     except firebase_admin.exceptions.FirebaseError as e:
#         print(f'Error sending message: {e}')
#     except ValueError as e:
#         print(f'ValueError: {e}')
#     except Exception as e:
#         print(f'An unexpected error occurred: {e}')