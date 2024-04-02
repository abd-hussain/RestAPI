from app.utils.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text

class DB_Post_Comment(Base):
    __tablename__ = "post_comments"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    customers_owner_id = Column(Integer, ForeignKey(
        "customers.id", ondelete="CASCADE"))
    attorney_owner_id = Column(Integer, ForeignKey(
        "attorney.id", ondelete="CASCADE"))
    up = Column(Integer, server_default=text('0'))
    down = Column(Integer, server_default=text('0'))
    content = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))