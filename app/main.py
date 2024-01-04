from fastapi import FastAPI
from app.routes import filter, report, settings
from app.models.database.client import db_client_user
from app.routes.mentor import mentor_auth, mentor_home, mentor_properties,  mentor_register, mentor_account, mentor_account_experiance, mentor_payments, mentor_appointment, mentor_settings
from app.routes.client import client_account, archive, client_appointment, client_auth, client_home, discount, mentor_list, mentors_details
from app.routes.notifications import client_notifications
from app.routes.notifications import mentor_notifications
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
    return {"message": " -#- Welcome To HelpEra API's With CICD- 11#- "}


#Mentors
app.include_router(mentor_auth.router)
app.include_router(mentor_home.router)
app.include_router(mentor_account.router)
app.include_router(mentor_account_experiance.router)
app.include_router(mentor_settings.router)
app.include_router(mentor_register.router)
app.include_router(mentor_properties.router)
app.include_router(mentor_payments.router)
app.include_router(mentor_appointment.router)
app.include_router(mentor_notifications.router)

#Clients
app.include_router(client_auth.router)
app.include_router(client_home.router)
app.include_router(mentor_list.router)
app.include_router(discount.router)
app.include_router(archive.router)
app.include_router(client_account.router)
app.include_router(mentors_details.router)
app.include_router(client_appointment.router)
app.include_router(client_notifications.router)

#Shared
app.include_router(filter.router)
app.include_router(settings.router)
app.include_router(report.router)

# TODO: Handle Send SMS For Verifications
# TODO: Handle Send Push Notifications
    # addNewNotification(UserType.Mentor, user.id, "notification" , "new Login", db)
# TODO: Currencys 
# TODO: UTC and Timing
# TODO: handle payment after success call
# TODO: handle mentor user need to verify
# TODO: handle mentor user rating hours / 1/2 1/4 3/4
# TODO: handle record call
# TODO: generate apikey for each login

# TODO: crod to delete duplicated contact in leads
# TODO: add  points for each mentor/client was used his referal code

# TODO: mentor must see rating and reviews for mentors and respond

# TODO: client login should have one methods delete debug