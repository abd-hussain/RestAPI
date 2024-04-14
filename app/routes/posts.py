from fastapi import Request, Depends ,Form, APIRouter, status, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.posts.db_posts import DB_Post
from app.models.database.posts.db_posts_reports import DB_Post_Report
from app.models.schemas.post import Post
from app.models.respond.general import generalResponse
from app.utils.oauth2 import get_current_user
from app.utils.validate_field import validateField
from app.utils.file_upload import edit_file_uploaded, handle_file_upload

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/report")
async def report_posts(post_id: int, user_type: str, reason: str, request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Check if the post exists
    post = db.query(DB_Post).filter(DB_Post.id == post_id).first()
    raise_http_exception_if_none(post, "Post ID not valid")

    # Check if the current user has already reported this post
    existing_report = db.query(DB_Post_Report).filter(
        DB_Post_Report.post_id == post_id,
        ((DB_Post_Report.attorney_owner_id == current_user.user_id) if user_type == "attorney" else (DB_Post_Report.customers_owner_id == current_user.user_id))
    ).first()

    if existing_report:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="You have already reported this post"
        )
        
    # Create a new report object based on user type
    if user_type == "attorney":
        obj = DB_Post_Report(**{"post_id" : post_id, 
                            "customers_owner_id" : None, 
                            "attorney_owner_id" : current_user.user_id, "reason" : reason})
    elif user_type == "customer":
        obj = DB_Post_Report(**{"post_id" : post_id, 
                            "customers_owner_id" : current_user.user_id, 
                            "attorney_owner_id" : None, "reason" : reason})
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")
    
    db.add(obj)
    db.commit()
    return generalResponse(message= "Successfully reported the post", data= None)


@router.post("/add")
async def add_post(cat_id: int = Form(None),
                    content: str = Form(None),
                    post_img: UploadFile = File(default=None), 
                        db: Session = Depends(get_db),
                            current_user: int = Depends(get_current_user)):
        
    lastId = db.query(DB_Post).order_by(DB_Post.id.desc()).first().id + 1

    payload = Post(id=lastId,
                   customers_owner_id=current_user.user_id,
                   category_id=validateField(cat_id),
                   content = validateField(content), 
                )
    if post_img is not None:
        handle_file_upload(post_img, 'post_img', lastId, payload)
             
    obj = DB_Post(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return generalResponse(message= "Post Created successfully", data=None)


@router.post("/edit")
async def edit_post(cat_id: int = Form(None),
                    post_id: str = Form(None),
                    content: str = Form(None),
                    post_img: UploadFile = File(default=None), 
                        db: Session = Depends(get_db),
                        current_user: int = Depends(get_current_user)):
        
     # Check if the post exists
    post = db.query(DB_Post).filter(DB_Post.id == post_id, DB_Post.customers_owner_id == current_user.user_id).first()
    raise_http_exception_if_none(post, "Post ID not valid or not related to you")
    
    if cat_id is not None:
        post.category_id = cat_id
        
    if content is not None:
        post.content = content
        
    if post_img is not None:
        post.post_img = edit_file_uploaded(post_img, 
                                            'post_img', 
                                            current_user.user_id)


    db.commit()    
    return generalResponse(message= "Post Edited successfully", data=None)


@router.delete("/delete")
async def delete_post(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Check if the post exists
    post = db.query(DB_Post).filter(DB_Post.id == post_id, DB_Post.customers_owner_id == current_user.user_id).first()
    raise_http_exception_if_none(post, "Post ID not valid or not related to you")

    db.delete(post)
    db.commit()
    return generalResponse(message= "Post Deleted successfully", data=None)

#############################################################################################

def raise_http_exception_if_none(entity, message: str):
    if entity is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=message)

