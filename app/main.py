from fastapi import FastAPI
from app.routes import discount, filter, notifications, report, settings
from app.models.database.client import db_client_user
from app.routes.mentor import mentor_auth, mentor_home, mentor_register, mentor_account, mentor_account_experiance, mentor_payments, mentor_appointment, mentor_settings, working_hours, mentor_hour_rate
from app.routes.client import client_account, archive, client_appointment, client_auth, client_home, mentor_list, mentors_details
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
    return {"message": " -#- Welcome To LegalzHub API's With CICD -#- "}

#Mentors
app.include_router(mentor_auth.router)
app.include_router(mentor_home.router)
app.include_router(mentor_account.router)
app.include_router(mentor_account_experiance.router)
app.include_router(mentor_settings.router)
app.include_router(mentor_register.router)
app.include_router(working_hours.router)
app.include_router(mentor_hour_rate.router)
app.include_router(mentor_payments.router)
app.include_router(mentor_appointment.router)

#Clients
app.include_router(client_auth.router)
app.include_router(client_home.router)
app.include_router(mentor_list.router)
app.include_router(archive.router)
app.include_router(client_account.router)
app.include_router(mentors_details.router)
app.include_router(client_appointment.router)

#Shared
app.include_router(filter.router)
app.include_router(settings.router)
app.include_router(report.router)
app.include_router(notifications.router)
app.include_router(discount.router)

# TODO: Handle Send SMS For Verifications
    #     addNewNotification(user_type=UserType.Mentor,
                        # user_id=current_user.user_id,
                        # currentLanguage=myHeader.language,
                        # db=db,
                        # title_english="Appointment canceled successfully",
                        # title_arabic="تم إلغاء الموعد بنجاح",
                        # content_english="canceling appointment will not cost you any thing and will not added to the payment screen",
                        # content_arabic="إلغاء الموعد لن يكلفك شيئا ولن يضاف إلى شاشة الدفع")


# TODO: handle record call & add Archive
