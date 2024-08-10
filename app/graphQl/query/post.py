# import strawberry
# from typing import List
# from sqlalchemy.orm import Session
# from app.graphQl.type.post import Post
# from app.utils.database import get_db
# from app.models.database.posts.db_posts import DB_Post
# from app.models.database.posts.db_posts_comments import DB_Post_Comment 
# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.database.posts.db_posts_reports import DB_Post_Report
# from app.models.database.db_country import DB_Countries
# from sqlalchemy import func
# from sqlalchemy import desc

# @strawberry.type
# class PostQuery:
#     @strawberry.field
#     def get_posts(self, catId: int, skip: int = 0, limit: int = 10, language: str = "en") -> List[Post]:
        
#         db: Session = next(get_db())
        
#         query = db.query(
#             DB_Post.id,
#             DB_Post.content,
#             DB_Post.post_img,
#             func.count(DB_Post_Report.id).label("report_count"),
#             DB_Post.customers_owner_id,
#             DB_Post.published,
#             DB_Post.category_id,
#             DB_Post.created_at,
#             DB_Customer_Users.first_name,
#             DB_Customer_Users.last_name,
#             DB_Customer_Users.profile_img,
#             DB_Countries.flag_image,
#             func.count(DB_Post_Comment.id).label("comment_count"),
#         ).join(
#             DB_Customer_Users, DB_Customer_Users.id == DB_Post.customers_owner_id, isouter=True
#         ).join(
#             DB_Countries, DB_Customer_Users.country_id == DB_Countries.id, isouter=True
#         ).outerjoin(
#             DB_Post_Comment, DB_Post_Comment.post_id == DB_Post.id
#         ).outerjoin(
#             DB_Post_Report, DB_Post_Report.post_id == DB_Post.id
#         ).group_by(
#             DB_Post.id,
#             DB_Customer_Users.first_name,
#             DB_Customer_Users.last_name,
#             DB_Customer_Users.profile_img,
#             DB_Countries.flag_image
#         ).filter(
#             DB_Post.published == True
#         )
                        
#         if catId != 0:
#             query = query.filter(DB_Post.category_id == catId)
            
#         posts = query.order_by(desc(DB_Post.created_at)).offset(skip).limit(limit).all()
        
                    
#         return [
#             Post(
#                 id=post.id,
#                 content=post.content,
#                 postImg=post.post_img,
#                 reportCount = post.report_count,
#                 customersOwnerId=post.customers_owner_id,
#                 categoryId=post.category_id,
#                 createdAt=post.created_at,
#                 customerFirstName= post.first_name,
#                 customerLastName= post.last_name,
#                 customerProfilePic= post.profile_img,
#                 customerFlag= post.flag_image,
#                 commentCount= post.comment_count
#             ) for post in posts
#         ]

                    
     
