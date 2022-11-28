from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text
from app.utils.database import Base

class DB_Client_Users(Base):
    __tablename__ = "client-users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    first_name = Column(String)
    last_name = Column(String)
    mobile_number = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True)
    gender = Column(Integer)
    allow_notifications = Column(Boolean, server_default='TRUE')
    blocked = Column(Boolean, server_default='FALSE')
    referal_code = Column(String)
    invitation_code = Column(String)
    profile_img = Column(String)
    os_type = Column(String, nullable=False)
    device_type_name = Column(String, nullable=False)
    os_version = Column(String, nullable=False)
    app_version = Column(String, nullable=False)
    date_of_birth = Column(String)
    last_usage = Column(String)
    last_otp = Column(String)
    points = Column(Integer, nullable=False, server_default="0")
    api_key = Column(String, nullable=False, unique=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))