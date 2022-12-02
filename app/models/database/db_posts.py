
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey
from app.utils.database import Base

class DB_Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    language = Column(String, nullable=False)
    content = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))