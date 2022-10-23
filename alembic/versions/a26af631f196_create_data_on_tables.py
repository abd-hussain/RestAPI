"""create data on tables

Revision ID: a26af631f1969
Revises: 
Create Date: 2022-10-20 12:40:47.209451

"""
from alembic import op
import sqlalchemy as sa

from app.models.database.db_versions import DB_Versions
from app.models.database.db_country import DB_Countries
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
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
            "flag_image" : "bahrain.png",
            "name_english" : "Bahrain",         
            "name_arabic" : "البحرين",   
            "currency_arabic" : "د.ب",
            "currency_english" : "BD",        
            "prefix_number" : "00973"
        },
        {
            "flag_image" : "egypt.png",
            "name_english" : "Eqypt",         
            "name_arabic" : "مصر",     
            "currency_arabic" : "ج.م",
            "currency_english" : "EGP",        
            "prefix_number" : "0020"
        }, 
        {
            "flag_image" : "iraq.png",
            "name_english" : "Iraq",         
            "name_arabic" : "العراق",  
            "currency_arabic" : "د.ع",
            "currency_english" : "IQD",        
            "prefix_number" : "00964"
        }, 
        {
            "flag_image" : "jordan.png",
            "name_english" : "Jordan",         
            "name_arabic" : "الاردن",         
            "currency_arabic" : "د.ا",   
            "currency_english" : "JD",        
            "prefix_number" : "00962"
        },
        {
            "flag_image" : "kuwait.png",
            "name_english" : "Kuwait",         
            "name_arabic" : "الكويت",         
            "currency_arabic" : "د.ك",
            "currency_english" : "KWD",        
            "prefix_number" : "00965"
        },
        {
            "flag_image" : "qatar.png",
            "name_english" : "Qatar",         
            "name_arabic" : "قطر",         
            "currency_arabic" : "ر.ق",
            "currency_english" : "QR",        
            "prefix_number" : "00974"
        }, 
        {
            "flag_image" : "saudi.png",
            "name_english" : "Saudi Arabia",         
            "name_arabic" : "المملكة العربية السعودية",         
            "currency_arabic" : "ر.س",
            "currency_english" : "Riyal",        
            "prefix_number" : "00966"
        }, 
        {
            "flag_image" : "emirates.png",
            "name_english" : "United Arab Emirates",         
            "name_arabic" : "الإمارات العربيّة المتّحدة",         
            "currency_arabic" : "د.إ",
            "currency_english" : "Dh",       
            "prefix_number" : "00971"
        }, 
        {
            "flag_image" : "othercountry.png",
            "name_english" : "Other",         
            "name_arabic" : "اخرى",         
            "currency_arabic" : "دولار",     
            "currency_english" : "USD",        
            "prefix_number" : "00000"
        }
    ]
    )
    
    op.bulk_insert(DB_Categories.__table__,
    [
        {
            "name_english" : "Medical",         
            "name_arabic" : "طب",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "1.png"
        },
         {
            "name_english" : "Psychology",         
            "name_arabic" : "طب نفسي",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "2.png"
        },
         {
            "name_english" : "Pediatrics",         
            "name_arabic" : "طب اطفال",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "3.png"
        },
         {
            "name_english" : "Diet & Nutrition",         
            "name_arabic" : "دايت و تغذيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "4.png"
        },
         {
            "name_english" : "Sexology",         
            "name_arabic" : "مشاكل جنسيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "5.png"
        },
         {
            "name_english" : "Dermatology",         
            "name_arabic" : "مشاكل جلديه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "6.png"
        },
         {
            "name_english" : "Gynecology",         
            "name_arabic" : "امراض نسائيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "7.png"
        },
         {
            "name_english" : "Homeopathy",         
            "name_arabic" : "علاج بالمواد الطبيعيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "8.png"
        }
    ]
    )
    
    op.bulk_insert(DB_Client_Users.__table__,
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
    
    op.bulk_insert(DB_Mentor_Users.__table__,
    [
        {
            "first_name" : "DR abed alrahman",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962795190663",        
            "email" : "aboud.masoud.92@gmail.com",         
            "gender" : 1,         
            "referal_code" : "",
            "profile_img" : "me.png",
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
