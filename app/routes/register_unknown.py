from fastapi import Request, Depends ,APIRouter, status
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from app.models.schemas.unknown_account import RegisterUnknownAccountModel
from app.utils.database import get_db
from app.utils.generate import generateAPIKey
from app.utils.validation import validateLanguageHeader
from app.models.database.db_unknown_user import DB_Unknown_Users
from app.utils.validate_field import validateField


router = APIRouter(
    prefix="/register",
    tags=["Users"]
)

@router.post("/unknown", status_code=status.HTTP_201_CREATED)
async def register_new_user(request: Request, 
                            os_type: str,
                            os_version: str,
                            device_name: str,
                            app_version: str,
                       db: Session = Depends(get_db)):
    
    myHeader = validateLanguageHeader(request)
    
    lastId = db.query(DB_Unknown_Users).order_by(DB_Unknown_Users.id.desc()).first().id + 1

    payload = RegisterUnknownAccountModel(id=lastId,
                                          language = myHeader.language,
                                          api_key = generateAPIKey(lastId),
                                          os_type = validateField(os_type),
                                          os_version = validateField(os_version),
                                          device_name = validateField(device_name),
                                          app_version = validateField(app_version),
                                          )

    obj = DB_Unknown_Users(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return generalResponse(message= "successfully created Account", data = {"api_key": payload.api_key})
