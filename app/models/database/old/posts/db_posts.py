# from app.utils.database import Base
# from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text

# class DB_Post(Base):
#     __tablename__ = "post"

#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     category_id = Column(Integer, ForeignKey(
#         "categories.id", ondelete="CASCADE"), nullable=False)
#     customers_owner_id = Column(Integer, ForeignKey(
#         "customers.id", ondelete="CASCADE"))
#     content = Column(String)
#     post_img = Column(String)
#     published = Column(Boolean, server_default='FALSE') 
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))