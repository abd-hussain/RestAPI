from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Numeric, Boolean, text
from app.utils.database.database import Base
from sqlalchemy.orm import relationship



class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Subcategories(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="CASCADE"), nullable=False)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Countries(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    flag_image = Column(String, nullable=False)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    currency_arabic = Column(String, nullable=False)
    currency_english = Column(String, nullable=False)
    prefix_number = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    

class Cities(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    

class Main_banners(Base):
    __tablename__ = "main_banners"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    language = Column(String, nullable=False)
    image = Column(String, nullable=False)
    action_type = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
class Secound_banners(Base):
    __tablename__ = "secound_banners"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    language = Column(String, nullable=False)
    image = Column(String, nullable=False)
    action_type = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Versions(Base):
    __tablename__ = "versions"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    version = Column(Numeric, nullable=False)
    content_arabic = Column(String, nullable=False)
    content_english = Column(String, nullable=False)
    is_forced = Column(Boolean, server_default='FALSE')
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Terms(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    type = Column(String, nullable=False)
    title_arabic = Column(String, nullable=False)
    title_english = Column(String, nullable=False)
    content_arabic = Column(String, nullable=False)
    content_english = Column(String, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
class Accounts(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    first_name = Column(String)
    last_name = Column(String)
    mobile_number = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True)
    gender = Column(Integer)
    hide_number = Column(Boolean, server_default='FALSE')
    verified = Column(Boolean, server_default='FALSE')
    blocked = Column(Boolean, server_default='FALSE')
    referal_code = Column(String)
    profile_img = Column(String)
    os_type = Column(String, nullable=False)
    device_type_name = Column(String, nullable=False)
    os_version = Column(String, nullable=False)
    app_version = Column(String, nullable=False)
    date_of_birth = Column(String)
    last_usage = Column(String)
    last_otp = Column(String)
    api_key = Column(String, nullable=False, unique=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
class Suggestion_Reported_items(Base):
    __tablename__ = "suggestion_issue"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    content = Column(String)
    attachment1 = Column(String)
    attachment2 = Column(String)
    attachment3 = Column(String)
    solved = Column(Boolean, server_default='FALSE')


class Issues_Reported_items(Base):
    __tablename__ = "reported_issue"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    content = Column(String)
    attachment1 = Column(String)
    attachment2 = Column(String)
    attachment3 = Column(String)
    solved = Column(Boolean, server_default='FALSE')