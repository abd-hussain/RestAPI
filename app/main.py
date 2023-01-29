from fastapi import FastAPI
from app.routes import filter, report, settings, notifications, loyality, tips, discount, appointment, event, client_account, mentor_account, mentor_list, messages
from app.models.database.client import db_client_user
from app.routes.mentor import mentor_auth, mentor_home
from app.routes.client import client_auth, client_home
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

app.include_router(client_auth.router)
app.include_router(mentor_auth.router)
app.include_router(client_home.router)
app.include_router(mentor_home.router)

app.include_router(client_account.router)
app.include_router(mentor_account.router)
app.include_router(mentor_list.router)
app.include_router(appointment.router)
app.include_router(event.router)

app.include_router(filter.router)
app.include_router(settings.router)
app.include_router(report.router)
app.include_router(notifications.router)
app.include_router(loyality.router)

app.include_router(tips.router)
app.include_router(discount.router)

app.include_router(messages.router)


# TODO: Handle Send SMS For Verifications
# TODO: Handle Send Push Notifications

