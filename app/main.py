from fastapi import FastAPI
from app.routes import filter, report, auth, settings, account
from app.models.database import db_user
from app.utils.public_api import origins
from app.utils.database.database import engine
from fastapi.middleware.cors import CORSMiddleware

db_user.Base.metadata.create_all(bind=engine)

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

app.include_router(auth.router)
app.include_router(filter.router)
app.include_router(settings.router)
app.include_router(report.router)
app.include_router(account.router)

