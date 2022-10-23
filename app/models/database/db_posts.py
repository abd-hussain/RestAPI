from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from app.utils.database import Base

class DB_Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    content = Column(String)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    owner_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner = relationship("DB_Mentor_Users")

class Comments(Base):
    __tablename__ = "comments"
    user_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)