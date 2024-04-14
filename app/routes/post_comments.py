from fastapi import Request, Depends , APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.posts.db_posts_comments import DB_Post_Comment 
from app.models.database.customer.db_customer_user import DB_Customer_Users
from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
from app.models.database.posts.db_posts_reports import DB_Post_Report
from app.models.schemas.post import PostComment
from app.models.database.db_country import DB_Countries
from sqlalchemy import desc
from app.models.respond.general import generalResponse
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/comment")
async def get_post_comments(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    comments = db.query(DB_Post_Comment.id,
                      DB_Post_Comment.content,
                      DB_Post_Comment.created_at,
                      DB_Post_Comment.up,
                      DB_Post_Comment.down,
                      DB_Post_Comment.post_id,
                     DB_Post_Comment.customers_owner_id,
                     DB_Post_Comment.attorney_owner_id,
                     DB_Customer_Users.first_name.label("customer_first_name"),
                     DB_Customer_Users.last_name.label("customer_last_name"),
                     DB_Customer_Users.profile_img.label("customer_profile_img"),
                        DB_Attorney_Users.suffixe_name.label("attorney_suffixe_name"),
                        DB_Attorney_Users.first_name.label("attorney_first_name"),
                        DB_Attorney_Users.last_name.label("attorney_last_name"),
                        DB_Attorney_Users.profile_img.label("attorney_profile_img"),
                        DB_Countries.flag_image,
                     ).join(
                        DB_Customer_Users, DB_Customer_Users.id == DB_Post_Comment.customers_owner_id, isouter=True
                    ).join(
                        DB_Attorney_Users, DB_Attorney_Users.id == DB_Post_Comment.attorney_owner_id, isouter=True
                    ).join(
                        DB_Countries, DB_Customer_Users.country_id == DB_Countries.id, isouter=True
                    ).order_by(desc(DB_Post_Comment.created_at)).all()
                        
    return generalResponse(message="Home Posts returned successfully", data=comments[skip : skip + limit])

@router.post("/comment")
async def add_comment_to_post(payload: PostComment, request: Request, 
        db: Session = Depends(get_db),
        current_user: int = Depends(get_current_user)):
        
    lastId = db.query(DB_Post_Comment).order_by(DB_Post_Comment.id.desc()).first().id + 1
            
    # Create a new comment object based on user type
    if payload.user_type == "attorney":
        obj = DB_Post_Comment(**{"id" : lastId,
                            "post_id" : payload.post_id, 
                            "customers_owner_id" : None, 
                            "attorney_owner_id" : current_user.user_id, 
                            "up" : payload.up, 
                            "down" : payload.down, 
                            "content" : payload.content})
    elif payload.user_type == "customer":
        obj = DB_Post_Comment(**{"id" : lastId,
                            "post_id" : payload.post_id, 
                            "customers_owner_id" : current_user.user_id, 
                            "attorney_owner_id" : None, 
                            "up" : payload.up, 
                            "down" : payload.down, 
                            "content" : payload.content})
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")
    

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return generalResponse(message= "Post Comment Created successfully", data=None)


@router.delete("/comment")
async def delete_comment(comment_id: int, user_type: str, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    if user_type == "attorney":
        # Check if the post exists
        comment = db.query(DB_Post_Comment).filter(DB_Post_Comment.id == comment_id, 
                                                    DB_Post_Comment.attorney_owner_id == current_user.user_id).first()
    elif user_type == "customer":
        # Check if the post exists
        comment = db.query(DB_Post_Comment).filter(DB_Post_Comment.id == comment_id, 
                                                    DB_Post_Comment.customers_owner_id == current_user.user_id).first()
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")
        
    
    raise_http_exception_if_none(comment, "Comment ID not valid or not related to you")

    db.delete(comment)
    db.commit()
    return generalResponse(message= "Comment Deleted successfully", data=None)

#############################################################################################

def raise_http_exception_if_none(entity, message: str):
    if entity is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=message)