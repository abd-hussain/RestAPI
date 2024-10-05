# from app.utils.database import Base
# from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text

# class DB_Suggestion_Reported(Base):
#     __tablename__ = "suggestion_issue"

#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     customers_owner_id = Column(Integer, ForeignKey(
#         "customers.id", ondelete="CASCADE"))
#     attorney_owner_id = Column(Integer, ForeignKey(
#         "attorney.id", ondelete="CASCADE"))
#     content = Column(String)
#     attachment1 = Column(String)
#     attachment2 = Column(String)
#     attachment3 = Column(String)
#     solved = Column(Boolean, server_default='FALSE')
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))