"""create data on tables

Revision ID: a26af631f1969
Revises: 
Create Date: 2022-10-20 12:40:47.209451

"""
from alembic import op
import sqlalchemy as sa

from app.models.database.db_versions import DB_Versions
from app.models.database.db_country import DB_Countries
from app.models.database.db_user import DB_Users
from app.models.database.db_category import DB_Categories


# revision identifiers, used by Alembic.
revision = 'a26af631f1969'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.bulk_insert(DB_Versions.__table__,
    [
        {
            "version" : 1.0,
            "content_arabic" : "اول اصدار",         
            "content_english" : "First Build",        
            "is_forced" : False
        }
    ]
    )
    
    op.bulk_insert(DB_Countries.__table__,
    [
        {
            "flag_image" : "jordan.png",
            "name_english" : "Jordan",         
            "name_arabic" : "الاردن",         
            "currency_arabic" : "د.ا",
            "currency_english" : "JD",        
            "prefix_number" : "00962"
        }
    ]
    )
    
    op.bulk_insert(DB_Categories.__table__,
    [
        {
            "name_english" : "Doctor",         
            "name_arabic" : "طب",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "1.png"
        }
    ]
    )
    
    op.bulk_insert(DB_Users.__table__,
    [
        {
            "first_name" : "abed alrahman",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962795190663",        
            "email" : "aboud.masoud.92@gmail.com",         
            "gender" : 1,         
            "hide_number" : False,         
            "hide_email" : False,        
            "allow_notifications" : True,         
            "blocked" : False,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "os_type" : "iOS",         
            "device_type_name" : "iPhone XR",        
            "os_version" : "16.2",         
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00100",         
            "country_id" : 1
        }
    ]
    )
    
    pass


def downgrade() -> None:
    pass
