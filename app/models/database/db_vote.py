from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey
from app.utils.database import Base

class DB_Votes(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)