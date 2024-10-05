# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from app.models.respond.general import generalResponse
# from sqlalchemy.orm import Session
# from fastapi import Request, Depends, APIRouter
# from app.utils.database import get_db
# from app.models.database.db_category import DB_Categories
# from app.models.database.db_suffix import DB_Suffix
# from app.models.database.db_country import DB_Countries
# from app.utils.validation import validateLanguageHeader

# router = APIRouter(
#     prefix="/filter",
#     tags=["Filter"]
# )

# @router.get("/categories")
# async def get_categories(request: Request, db: Session = Depends(get_db)):
#     myHeader = validateLanguageHeader(request)
    
#     category_column = DB_Categories.name_arabic if myHeader.language == "ar" else DB_Categories.name_english
#     categories = db.query(DB_Categories.id, category_column.label("name"), DB_Categories.icon).all()

#     return generalResponse(message="list of categories return successfully", data=categories)

# @router.get("/countries")
# async def get_countries(request: Request, db: Session = Depends(get_db)):
#     myHeader = validateLanguageHeader(request)
    
#     country_name_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english
#     country_currency = DB_Countries.currency_arabic if myHeader.language == "ar" else DB_Countries.currency_english
#     countries = db.query(DB_Countries.id, DB_Countries.flag_image, country_name_column.label("name"), 
#                          country_currency.label("currency"),DB_Countries.dialCode,
#                          DB_Countries.country_code, DB_Countries.currency_code,
#                          DB_Countries.minLength, DB_Countries.maxLength, 
#                          DB_Countries.dollar_equivalent).all()
    
#     return generalResponse(message="list of countries return successfully", data=countries)

# @router.get("/suffix")
# async def get_suffix(request: Request, db: Session = Depends(get_db)):
#     myHeader = validateLanguageHeader(request)
    
#     suffix_name_column = DB_Suffix.name_arabic if myHeader.language == "ar" else DB_Suffix.name_english
#     suffix = db.query(DB_Suffix.id, suffix_name_column.label("name")).all()

#     return generalResponse(message="list of suffix return successfully", data=suffix)

# @router.post("/checkemial")
# async def post_validate_email(email: str, db: Session = Depends(get_db)): 
#     attorney_exists = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.email == email).first() is not None
#     customer_exists = db.query(DB_Customer_Users).filter(DB_Customer_Users.email == email).first() is not None

#     email_exists = attorney_exists or customer_exists

#     return generalResponse(message="checking email is exsisting", data=email_exists)

# @router.post("/checkmobile")
# async def post_validate_mobile(mobile: str, db: Session = Depends(get_db)): 
#     attorney_exists = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.mobile_number == mobile).first() is not None
#     customer_exists = db.query(DB_Customer_Users).filter(DB_Customer_Users.mobile_number == mobile).first() is not None

#     mobile_exists = attorney_exists or customer_exists

#     return generalResponse(message="checking mobile is exsisting", data=mobile_exists)


# @router.post("/referalcode")
# async def post_validate_invitation_code(code: str, db: Session = Depends(get_db)): 
#     attorney_exists = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.invitation_code == code).first() is not None
#     customer_exists = db.query(DB_Customer_Users).filter(DB_Customer_Users.invitation_code == code).first() is not None
    
#     code_exists = attorney_exists or customer_exists

#     return generalResponse(message="checking invitation Code exsisting", data=code_exists)


# @router.post("/currency-converter")
# async def currency_converter(currency: str, db: Session = Depends(get_db)):
    
#     countries = db.query(DB_Countries.currency_code, DB_Countries.dollar_equivalent).all()
    
#     dollar_equivalent = 0.0
    
#     for country in countries:
#         if country.currency_code == currency:
#             dollar_equivalent = country.dollar_equivalent

#     return generalResponse(message="dollar Equivalent", data=dollar_equivalent)