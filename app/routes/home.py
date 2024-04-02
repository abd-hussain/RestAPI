from fastapi import Request, Depends ,APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_banner import DB_Banners, UsersType
from app.models.database.posts.db_posts import DB_Post

from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/home",
    tags=["Home"]
)

@router.get("/")
async def get_home(userType: str, request: Request, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language
    
    if userType == "attorney":
        targeted = UsersType.attorney
    elif userType == "customer":
        targeted = UsersType.customer
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")
    
    main_banners = db.query(DB_Banners.image, DB_Banners.action_type
        ).filter_by(language=language, published=True, targeted=targeted
                                ).all()
    
    posts = db.query(DB_Post).all()
        
    return generalResponse(message="Home returned successfully", data={"banners": main_banners,
                                                                       "posts": posts })


# //TODO Handle Return Post Pagination, repost post, add comment to the post, delete comment from post, delete post, edit post, add post