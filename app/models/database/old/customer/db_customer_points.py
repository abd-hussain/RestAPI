# from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
# from app.utils.database import Base

# class DB_Customer_Points(Base):
#     __tablename__ = "customer_points"
#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     user_customer_id = Column(Integer, ForeignKey(
#         "customers.id", ondelete="CASCADE"), primary_key=True)
#     invited_customers_id = Column(Integer, ForeignKey(
#         "customers.id", ondelete="CASCADE"), nullable=True)
#     invited_attorney_id = Column(Integer, ForeignKey(
#         "attorney.id", ondelete="CASCADE"), nullable=True)
#     point = Column(Integer, server_default=text('1'))
#     reason = Column(String)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))