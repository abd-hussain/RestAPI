# from sqlalchemy import TIMESTAMP, Column, Integer, String, DECIMAL, text
# from app.utils.database import Base

# class DB_DiscountType(Base):
#     __tablename__ = "discount_type"

#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     code = Column(String, nullable=False)
#     percent_value = Column(DECIMAL, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))