from app.utils.database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from sqlalchemy.dialects.postgresql import JSONB

class DB_Mus7af(Base):
    __tablename__ = "mus7af"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name_referance = Column(String, nullable=False)
    description = Column(String)
    language = Column(String, nullable=False)
    previewImage = Column(String, nullable=False)
    attachmentLocation = Column(String, nullable=False)
    addedPagesAttachmentLocation = Column(String, nullable=False)
    published = Column(Boolean, server_default='True')
    juz2ToPageNumbers = Column(JSONB, nullable=False)
    sorahToPageNumbers = Column(JSONB, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))
    

