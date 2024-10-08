# from app.utils.database import Base
# from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text

# class DB_Customer_Users(Base):
#     __tablename__ = "customers"

#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     mobile_number = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     email = Column(String, unique=True)
#     gender = Column(Integer)
#     allow_notifications = Column(Boolean, server_default='TRUE')
#     blocked = Column(Boolean, server_default='FALSE')
#     invitation_code = Column(String)
#     profile_img = Column(String)
#     app_version = Column(String, nullable=False)
#     date_of_birth = Column(String)
#     last_usage = Column(TIMESTAMP(timezone=True))
#     points = Column(Integer, nullable=False, server_default="0")
#     api_key = Column(String, nullable=False, unique=True)
#     push_token = Column(String)
#     country_id = Column(Integer, ForeignKey(
#         "countries.id", ondelete="CASCADE"), nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))