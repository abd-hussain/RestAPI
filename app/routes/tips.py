from fastapi import Request, Depends, status ,APIRouter
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_tips import DB_TipsQuestions, DB_TipsUsersAnswer, DB_TipsResult
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
async def postQuestionAnswers(tip_id :int, payload: AnswersModel, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    query = db.query(DB_TipsUsersAnswer)
    
    numberOfPoints = 0
    
    for item in payload.list:
        numberOfPoints = numberOfPoints + item.point
        item.client_owner_id = get_current_user.user_id
        filtered = query.filter(DB_TipsUsersAnswer.question_id == item.question_id and DB_TipsUsersAnswer.client_owner_id == item.client_owner_id)
        
        if filtered.first() == None:
            print("|++++ not exsist")
            obj = DB_TipsUsersAnswer(**item.dict())
            db.add(obj) 
            db.commit()
        else:
            print("|++++ exsist")
            filtered.update(item.dict(), synchronize_session=False)
            db.commit()
      
    result_query = db.query(DB_TipsResult.id, DB_TipsResult.tips_id, DB_TipsResult.point, 
                            DB_TipsResult.title_english.label("title"), DB_TipsResult.desc_english.label("desc"))
    if (myHeader.language == "ar"):
        result_query = db.query(DB_TipsResult.id, DB_TipsResult.tips_id, DB_TipsResult.point, 
                            DB_TipsResult.title_arabic.label("title"), DB_TipsResult.desc_arabic.label("desc"))
        
    if numberOfPoints >= 100:
        result_query = result_query.filter(DB_TipsResult.tips_id == tip_id).filter(DB_TipsResult.point == "very high").first()
    elif numberOfPoints >= 75 and numberOfPoints < 100:
        result_query = result_query.filter(DB_TipsResult.tips_id == tip_id).filter(DB_TipsResult.point == "high").first()
    elif numberOfPoints >= 50 and numberOfPoints < 75:
        result_query = result_query.filter(DB_TipsResult.tips_id == tip_id).filter(DB_TipsResult.point == "mid").first()
    elif numberOfPoints < 50:
        result_query = result_query.filter(DB_TipsResult.tips_id == tip_id).filter(DB_TipsResult.point == "low").first()
        
    return generalResponse(message="tips Answers result", data=result_query)
