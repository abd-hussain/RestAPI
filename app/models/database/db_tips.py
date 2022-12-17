from sqlalchemy import TIMESTAMP, Column, Integer, String, ForeignKey, text
from app.utils.database import Base

class DB_Tips(Base):
    __tablename__ = "tips"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="CASCADE"))
    title_arabic = Column(String, nullable=False)
    title_english = Column(String, nullable=False)
    desc_arabic = Column(String, nullable=False)
    desc_english = Column(String, nullable=False)
    note_arabic = Column(String, nullable=False)
    note_english = Column(String, nullable=False)
    referance_arabic = Column(String, nullable=False)
    referance_english = Column(String, nullable=False)
    image = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
class DB_TipsQuestions(Base):
    __tablename__ = "tips-questions"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    tips_id = Column(Integer, ForeignKey(
        "tips.id", ondelete="CASCADE"))
    question_arabic = Column(String, nullable=False)
    question_english = Column(String, nullable=False)
    answer1_arabic = Column(String, nullable=False)
    answer1_english = Column(String, nullable=False)
    answer1_points = Column(Integer, nullable=False)
    answer2_arabic = Column(String, nullable=False)
    answer2_english = Column(String, nullable=False)
    answer2_points = Column(Integer, nullable=False)
    answer3_arabic = Column(String)
    answer3_english = Column(String)
    answer3_points = Column(Integer, nullable=False, server_default=text('0'))
    answer4_arabic = Column(String)
    answer4_english = Column(String)
    answer4_points = Column(Integer, nullable=False, server_default=text('0'))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
class DB_TipsUsersAnswer(Base):
    __tablename__ = "tips-users-answers"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    question_id = Column(Integer, ForeignKey(
        "tips-questions.id", ondelete="CASCADE"))
    client_owner_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"))
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    point = Column(Integer, nullable=False)
    
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
class DB_TipsResult(Base):
    __tablename__ = "tips-result"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    tips_id = Column(Integer, ForeignKey(
        "tips.id", ondelete="CASCADE"))
    point = Column(String, nullable=False)
    title_arabic = Column(String, nullable=False)
    title_english = Column(String, nullable=False)
    desc_english = Column(String)
    desc_arabic = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))