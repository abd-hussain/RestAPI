from fastapi import Request, Depends ,APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_banner import DB_Banners, UsersType
from app.models.database.posts.db_posts import DB_Post
from app.models.database.posts.db_posts_comments import DB_Post_Comment 
from app.models.database.customer.db_customer_user import DB_Customer_Users
from app.models.database.posts.db_posts_reports import DB_Post_Report
from app.models.database.db_country import DB_Countries
from sqlalchemy import func
from sqlalchemy import desc
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
async def get_posts_home(request: Request, cat_id: int ,skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language
    if cat_id == 0:
        posts = db.query(DB_Post.id,
                     DB_Post.content,
                     DB_Post.post_img,
                     func.count(DB_Post_Report.id).label("report_count"),
                     DB_Post.customers_owner_id,
                     DB_Post.published,
                     DB_Post.category_id,
                     DB_Post.created_at,
                     DB_Customer_Users.first_name,
                     DB_Customer_Users.last_name,
                     DB_Customer_Users.profile_img,
                     DB_Countries.flag_image,
                     func.count(DB_Post_Comment.id).label("comment_count"),
                     ).join(
                        DB_Customer_Users, DB_Customer_Users.id == DB_Post.customers_owner_id, isouter=True
                    ).join(
                        DB_Countries, DB_Customer_Users.country_id == DB_Countries.id, isouter=True
                    ).outerjoin(
                        DB_Post_Comment, DB_Post_Comment.post_id == DB_Post.id
                    ).outerjoin(
                        DB_Post_Report, DB_Post_Report.post_id == DB_Post.id
                    ).group_by(
                        DB_Post.id,
                        DB_Customer_Users.first_name,
                        DB_Customer_Users.last_name,
                        DB_Customer_Users.profile_img,
                        DB_Countries.flag_image
                    ).filter(DB_Post.published == True
                    ).order_by(desc(DB_Post.created_at)).all()
    else:
        posts = db.query(DB_Post.id,
                     DB_Post.content,
                     DB_Post.post_img,
                     func.count(DB_Post_Report.id).label("report_count"),
                     DB_Post.customers_owner_id,
                     DB_Post.published,
                     DB_Post.category_id,
                     DB_Post.created_at,
                     DB_Customer_Users.first_name,
                     DB_Customer_Users.last_name,
                     DB_Customer_Users.profile_img,
                     DB_Countries.flag_image,
                     func.count(DB_Post_Comment.id).label("comment_count"),
                     ).join(
                        DB_Customer_Users, DB_Customer_Users.id == DB_Post.customers_owner_id, isouter=True
                    ).join(
                        DB_Countries, DB_Customer_Users.country_id == DB_Countries.id, isouter=True
                    ).outerjoin(
                        DB_Post_Comment, DB_Post_Comment.post_id == DB_Post.id
                    ).outerjoin(
                        DB_Post_Report, DB_Post_Report.post_id == DB_Post.id
                    ).group_by(
                        DB_Post.id,
                        DB_Customer_Users.first_name,
                        DB_Customer_Users.last_name,
                        DB_Customer_Users.profile_img,
                        DB_Countries.flag_image
                    ).filter(DB_Post.published == True, DB_Post.category_id == cat_id
                    ).order_by(desc(DB_Post.created_at)).all()
                        
    return generalResponse(message="Home Posts returned successfully", data=posts[skip : skip + limit])
