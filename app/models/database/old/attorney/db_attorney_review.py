# from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, DECIMAL, text
# from app.utils.database import Base

# class DB_Attorney_Review(Base):
#     __tablename__ = "attorney_review"
#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     attorney_id = Column(Integer, ForeignKey(
#         "attorney.id", ondelete="CASCADE"), primary_key=True)
#     customers_id = Column(Integer, ForeignKey(
#         "customers.id", ondelete="CASCADE"), primary_key=True)
#     stars = Column(DECIMAL, nullable=False, server_default=text('5.0'))
#     comment = Column(String)
#     attorney_response = Column(String)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))