
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from app.utils.database import Base
class DB_Mentor_Banners(Base):
    __tablename__ = "mentor-banners"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    language = Column(String, nullable=False)
    image = Column(String, nullable=False)
    action_type = Column(String, nullable=True)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))