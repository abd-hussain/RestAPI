from fastapi import FastAPI, Response
from app.routes import report, register_unknown
from app.routes.quran import quran_copy

from app.utils.public_api import origins
from app.utils.database import get_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
# import strawberry
# from strawberry.asgi import GraphQL

# graphQL_schema = strawberry.Schema(query=PostQuery)


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/application", StaticFiles(directory="application"), name="application")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": " -#- Welcome To Islam Mob API's With CICD -#- "}

@app.get("/favicon.ico")
async def favicon():
    return Response(content="", media_type="web/favicon.ico")


app.include_router(register_unknown.router)
app.include_router(report.router)
#Quran
app.include_router(quran_copy.router)


#Admin
# app.include_router(admin_auth.router)


# #Attorney
# app.include_router(attorney_account_experiance.router)
# app.include_router(attorney_account.router)
# app.include_router(attorney_appointment.router)
# app.include_router(attorney_hour_rate.router)
# app.include_router(attorney_payments.router)
# app.include_router(attorney_register.router)
# app.include_router(attorney_settings.router)
# app.include_router(working_hours.router)

# #Customer
# app.include_router(attorney_list.router)
# app.include_router(attorneys_details.router)
# app.include_router(customer_account.router)
# app.include_router(customer_appointment.router)
# app.include_router(customer_register.router)

# app.include_router(filter.router)
# app.include_router(settings.router)

# app.include_router(notifications.router)
# app.include_router(discount.router)
# app.include_router(auth.router)
# app.include_router(home.router)
# app.include_router(posts.router)
# app.include_router(post_comments.router)


@app.on_event("startup")
async def startup():
    app.state.db = next(get_db())
    
@app.on_event("shutdown")
async def shutdown():
    app.state.db.close()

# graphql_app = GraphQL(graphQL_schema, debug=True)

# app.add_route("/graphql", graphql_app)
# app.add_websocket_route("/graphql", graphql_app)
