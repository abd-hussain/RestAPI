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

@router.get("/banners")
async def get_banner_home(userType: str, request: Request, db: Session = Depends(get_db)):
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
        
    return generalResponse(message="Home Banners returned successfully", data=main_banners)


@router.get("/posts")
async def get_posts_home(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language

    posts = db.query(DB_Post).order_by(DB_Post.created_at).all()
    
    return generalResponse(message="Home Posts returned successfully", data=posts[skip : skip + limit])


# //TODO Handle repost post, add comment to the post, delete comment from post, delete post, edit post, add post