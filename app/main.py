from fastapi import FastAPI
from app.routes import filter, report, settings , posts
from app.models.database.client import db_client_user
from app.routes.client import client_auth, client_account
from app.routes.mentor import mentor_auth, mentor_account
from app.utils.public_api import origins
from app.utils.database import engine
from fastapi.middleware.cors import CORSMiddleware

db_client_user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": " -#- Welcome To My API -#- "}

app.include_router(client_auth.router)
app.include_router(mentor_auth.router)
app.include_router(client_account.router)
app.include_router(mentor_account.router)

app.include_router(posts.router)
app.include_router(filter.router)
app.include_router(settings.router)
app.include_router(report.router)


# TODO: Handle Send SMS For Verifications
# TODO: Handle Send Push Notifications
# TODO: Handle Upload Image
# TODO: Handle Return Images

