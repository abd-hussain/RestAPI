
# from app.utils.database import Base
# from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, DECIMAL

# class DB_Countries(Base):
#     __tablename__ = "countries"

#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     flag_image = Column(String, nullable=False)
#     name_arabic = Column(String, nullable=False)
#     name_english = Column(String, nullable=False)
#     currency_arabic = Column(String, nullable=False)
#     currency_english = Column(String, nullable=False)
#     country_code = Column(String, nullable=False)
#     currency_code = Column(String, nullable=False)
#     dialCode = Column(String, nullable=False)
#     minLength = Column(Integer, nullable=False)
#     maxLength = Column(Integer, nullable=False)
#     dollar_equivalent = Column(DECIMAL, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))