from app.utils.database import Base
from sqlalchemy import  TIMESTAMP, ForeignKey, Column, Integer, String, text, Boolean
from sqlalchemy.orm import relationship

class DB_Stories(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    language = Column(String, nullable=False)
    assets = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    owner = relationship("DB_Mentor_Users")


class DB_StoryReports(Base):
    __tablename__ = "story_reports"
    user_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    story_id = Column(Integer, ForeignKey(
        "stories.id", ondelete="CASCADE"), primary_key=True)