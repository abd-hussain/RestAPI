from app.utils.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text

class DB_Issues_Reported(Base):
    __tablename__ = "reported_issue"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    api_key = Column(String, ForeignKey("unknown_users.api_key", ondelete="CASCADE"))
    content = Column(String)
    attachment1 = Column(String)
    attachment2 = Column(String)
    attachment3 = Column(String)
    solved = Column(Boolean, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))