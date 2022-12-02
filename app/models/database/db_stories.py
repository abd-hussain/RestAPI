
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey
from app.utils.database import Base

class DB_Stories(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    language = Column(String, nullable=False)
    assets1 = Column(String, nullable=False)
    assets2 = Column(String, nullable=True)
    assets3 = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))