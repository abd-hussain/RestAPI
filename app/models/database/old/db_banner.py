# from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, Enum
# from app.utils.database import Base
# import enum

# class UsersType(enum.Enum):
#     attorney = 1
#     customer = 2

# class DB_Banners(Base):
#     __tablename__ = "banners"

#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     language = Column(String, nullable=False)
#     image = Column(String, nullable=False)
#     action_type = Column(String, nullable=True)
#     published = Column(Boolean, server_default='TRUE')
#     targeted = Column(Enum(UsersType))
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))