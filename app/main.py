from fastapi import FastAPI
from app.routes import filter, report, settings, notifications, appointment, event, messages
from app.models.database.client import db_client_user
from app.routes.mentor import mentor_auth, mentor_home, mentor_properties, mentor_account, mentor_payments
from app.routes.client import client_account, client_auth, client_home, discount, loyality, mentor_list, mentors_details, tips
from app.utils.public_api import origins
from app.utils.database import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

db_client_user.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": " -#- Welcome To HelpEra API's With CICD-#- "}


#Mentors
app.include_router(mentor_auth.router)
app.include_router(mentor_home.router)
app.include_router(mentor_account.router)
app.include_router(mentor_properties.router)
app.include_router(mentor_payments.router)

#Clients
app.include_router(client_auth.router)
app.include_router(client_home.router)
app.include_router(tips.router)
app.include_router(loyality.router)
app.include_router(mentor_list.router)
app.include_router(discount.router)
app.include_router(client_account.router)
app.include_router(mentors_details.router)

#Shared
app.include_router(filter.router)
app.include_router(messages.router)
app.include_router(settings.router)
app.include_router(report.router)
app.include_router(notifications.router)
app.include_router(event.router)
app.include_router(appointment.router)


# TODO: Handle Send SMS For Verifications
# TODO: Handle Send Push Notifications
# TODO: Handle Send Email On Reset Password

