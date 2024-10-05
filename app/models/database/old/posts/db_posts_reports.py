# from app.utils.database import Base
# from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text

# class DB_Post_Report(Base):
#     __tablename__ = "post_reports"

#     id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
#     post_id = Column(Integer, ForeignKey(
#         "post.id", ondelete="CASCADE"))
#     customers_owner_id = Column(Integer, ForeignKey(
#         "customers.id", ondelete="CASCADE"))
#     attorney_owner_id = Column(Integer, ForeignKey(
#         "attorney.id", ondelete="CASCADE"))
#     reason = Column(String)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text("timezone('utc', now())"))