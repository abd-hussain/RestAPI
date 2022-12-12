from fastapi import Request, Depends, status ,APIRouter, Form
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_tips import DB_TipsQuestions, DB_TipsUsersAnswer
from app.models.respond.general import generalResponse
from app.models.schemas.answers import AnswersModel
from app.utils.oauth2 import get_current_user
from sqlalchemy import func

router = APIRouter(
    prefix="/tips",
    tags=["Tips"]
)

@router.get("/")
async def get_tips(tip_id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    query = db.query(DB_TipsQuestions.id, DB_TipsQuestions.question_english.label("question"), 
                     DB_TipsQuestions.answer1_english.label("answer1"),
                     DB_TipsQuestions.answer1_points,
                     DB_TipsQuestions.answer2_english.label("answer2"),
                     DB_TipsQuestions.answer2_points,
                     DB_TipsQuestions.answer3_english.label("answer3"),
                     DB_TipsQuestions.answer3_points,
                     DB_TipsQuestions.answer4_english.label("answer4"),
                     DB_TipsQuestions.answer4_points).filter(DB_TipsQuestions.tips_id == tip_id).all()
    if (myHeader.language == "ar"):
        query = db.query(DB_TipsQuestions.id, DB_TipsQuestions.question_arabic.label("question"), 
                     DB_TipsQuestions.answer1_arabic.label("answer1"),
                     DB_TipsQuestions.answer1_points,
                     DB_TipsQuestions.answer2_arabic.label("answer2"),
                     DB_TipsQuestions.answer2_points,
                     DB_TipsQuestions.answer3_arabic.label("answer3"),
                     DB_TipsQuestions.answer3_points,
                     DB_TipsQuestions.answer4_arabic.label("answer4"),
                     DB_TipsQuestions.answer4_points).filter(DB_TipsQuestions.tips_id == tip_id).all()
    return generalResponse(message="tips questions return successfully", data=query)


@router.post("/")
async def postQuestionAnswers(payload: AnswersModel, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    numberOfPoints = 0
    
    for item in payload.list:
       numberOfPoints = numberOfPoints + item.point
       item.client_owner_id = get_current_user.user_id
       obj = DB_TipsUsersAnswer(**item.dict())
       db.add(obj) 
       db.commit()
       db.refresh(obj)

    
        
    print(numberOfPoints)
    

    return generalResponse(message="tips Answers send successfully", data=None)
