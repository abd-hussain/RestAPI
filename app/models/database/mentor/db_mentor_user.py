from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, DECIMAL, Boolean, text
from app.utils.database import Base
from sqlalchemy.orm import relationship

class DB_Mentor_Users(Base):
    __tablename__ = "mentor-users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="CASCADE"), nullable=False)
    suffixe_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    class_min = Column(Integer, nullable=False)
    hour_rate_by_JD = Column(DECIMAL, nullable=False, server_default=text('10.0'))
    rate = Column(DECIMAL, nullable=False, server_default=text('5.0'))
    mobile_number = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True)
    gender = Column(Integer)
    blocked = Column(Boolean, server_default='FALSE') 
    referal_code = Column(String)
    invitation_code = Column(String)
    profile_img = Column(String)
    app_version = Column(String, nullable=False)
    date_of_birth = Column(String)
    last_usage = Column(String)
    last_otp = Column(String)
    api_key = Column(String, nullable=False, unique=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
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