
from fastapi import Request, Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models.database.db_posts import DB_Posts
from app.models.database.db_vote import DB_Votes
from app.models.respond.general import generalResponse
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from typing import Optional
from sqlalchemy import func
from app.utils.oauth2 import get_current_user
from app.models.schemas.post import Post

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/")
async def get_posts(request: Request, db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    myHeader = validateLanguageHeader(request)
    
    posts = db.query(DB_Posts.id, DB_Posts.content, DB_Posts.owner_id, func.count(DB_Votes.post_id).label("votes")).join(
        DB_Votes, DB_Votes.post_id == DB_Posts.id, isouter=True).group_by(DB_Posts.id).filter(DB_Posts.language == myHeader.language).filter(DB_Posts.published == True).filter(DB_Posts.content.contains(search)).limit(limit).offset(skip).all()
    
    return generalResponse(message="posts return successfully", data=posts)

@router.post("/")
def create_post(content: str, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    new_post = Post(language = myHeader.language, owner_id = get_current_user.user_id, content = content)
    obj = DB_Posts(**new_post.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)

    return generalResponse(message= "successfully create post", data=obj)

@router.put("/")
def update_post(postId: int, content: str, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)

    post_query = db.query(DB_Posts).filter(DB_Posts.id == postId)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {postId} does not exist")

    if post.owner_id != get_current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    update_post = Post(language = myHeader.language, owner_id = get_current_user.user_id, content = content)

    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(post_query)

    return generalResponse(message= "successfully update post", data=post_query)

@router.delete("/")
def delete_post(postId: int, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):

    post_query = db.query(DB_Posts).filter(DB_Posts.id == postId)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != get_current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return generalResponse(message= "successfully delete post", data=None)

@router.post("/vote")
async def vote(postId: int, isItUp: bool, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):

    post = db.query(DB_Posts).filter(DB_Posts.id == postId).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {postId} does not exist")
        
    vote_query = db.query(DB_Votes).filter(
        DB_Votes.post_id == postId, DB_Votes.user_id == get_current_user.user_id)
    
    found_vote = vote_query.first()
    if (isItUp):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {get_current_user.user_id} has alredy voted on this post")
    
        obj = DB_Votes(**{"user_id" : get_current_user.user_id, "post_id" : postId})
        db.add(obj)
        db.commit()
        return generalResponse(message= "successfully Vote added", data= None)
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return generalResponse(message= "successfully Vote deleted", data= None)
