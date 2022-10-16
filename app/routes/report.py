from app.models.respond import general
from fastapi import status, Depends, APIRouter
from app.models.schemas.report import Report

router = APIRouter(
    tags=["Report"]
)

# @router.post("/issue", status_code=status.HTTP_201_CREATED)
# def create_issue(payload: Report,db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
#     obj = db_models.Issues_Reported_items(**payload.dict())
#     db.add(obj)
#     db.commit()
#     return response.generalResponse(message= "successfully created issue", data= None)

# @router.post("/suggestion", status_code=status.HTTP_201_CREATED)
# def create_suggestion(payload: Report,db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
#     obj = db_models.Suggestion_Reported_items(**payload.dict())
#     db.add(obj)
#     db.commit()
#     return response.generalResponse(message= "successfully created suggestion", data= None)