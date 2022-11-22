"""create data on tables

Revision ID: a26af631f1969
Revises: 
Create Date: 2022-10-20 12:40:47.209451

"""
from alembic import op

from app.models.database.db_versions import DB_Versions
from app.models.database.db_country import DB_Countries
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_category import DB_Categories
from app.models.database.db_notifications import DB_Notifications


# revision identifiers, used by Alembic.
revision = 'a26af631f1969'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.bulk_insert(DB_Versions.__table__,
    [
        {
            "id" : 1,
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
            "id" : 1,
            "flag_image" : "bahrain.png",
            "name_english" : "Bahrain",         
            "name_arabic" : "البحرين",   
            "currency_arabic" : "د.ب",
            "currency_english" : "BD",        
            "prefix_number" : "00973"
        },
        {          
            "id" : 2,
            "flag_image" : "egypt.png",
            "name_english" : "Eqypt",         
            "name_arabic" : "مصر",     
            "currency_arabic" : "ج.م",
            "currency_english" : "EGP",        
            "prefix_number" : "0020"
        }, 
        {
            "id" : 3,
            "flag_image" : "iraq.png",
            "name_english" : "Iraq",         
            "name_arabic" : "العراق",  
            "currency_arabic" : "د.ع",
            "currency_english" : "IQD",        
            "prefix_number" : "00964"
        }, 
        {
            "id" : 4,
            "flag_image" : "jordan.png",
            "name_english" : "Jordan",         
            "name_arabic" : "الاردن",         
            "currency_arabic" : "د.ا",   
            "currency_english" : "JD",        
            "prefix_number" : "00962"
        },
        {
            "id" : 5,
            "flag_image" : "kuwait.png",
            "name_english" : "Kuwait",         
            "name_arabic" : "الكويت",         
            "currency_arabic" : "د.ك",
            "currency_english" : "KWD",        
            "prefix_number" : "00965"
        },
        {
            "id" : 6,
            "flag_image" : "qatar.png",
            "name_english" : "Qatar",         
            "name_arabic" : "قطر",         
            "currency_arabic" : "ر.ق",
            "currency_english" : "QR",        
            "prefix_number" : "00974"
        }, 
        {
            "id" : 7,
            "flag_image" : "saudi.png",
            "name_english" : "Saudi Arabia",         
            "name_arabic" : "المملكة العربية السعودية",         
            "currency_arabic" : "ر.س",
            "currency_english" : "Riyal",        
            "prefix_number" : "00966"
        }, 
        {
            "id" : 8,
            "flag_image" : "emirates.png",
            "name_english" : "United Arab Emirates",         
            "name_arabic" : "الإمارات العربيّة المتّحدة",         
            "currency_arabic" : "د.إ",
            "currency_english" : "Dh",       
            "prefix_number" : "00971"
        }, 
        {
            "id" : 9,
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
            "id" : 1,
            "name_english" : "Psychology",         
            "name_arabic" : "طب نفسي",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "psychology.png"
        },
         {
            "id" : 2,
            "name_english" : "Pediatrics",         
            "name_arabic" : "طب اطفال",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "pediatrics.png"
        },
         {
            "id" : 3,
            "name_english" : "Diet & Nutrition",         
            "name_arabic" : "دايت و تغذيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "diet.png"
        },
         {
            "id" : 4,
            "name_english" : "Sexology",         
            "name_arabic" : "مشاكل جنسيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "sexology.png"
        },
         {
            "id" : 5,
            "name_english" : "Dermatology",         
            "name_arabic" : "مشاكل جلديه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "dermatology.png"
        },
         {
            "id" : 6,
            "name_english" : "Gynecology",         
            "name_arabic" : "امراض نسائيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "gynecology.png"
        },
         {
            "id" : 7,
            "name_english" : "Homeopathy",         
            "name_arabic" : "علاج بالمواد الطبيعيه",         
            "description_arabic" : "",
            "description_english" : "",        
            "icon" : "homeopathy.png"
        }
    ]
    )
    
    op.bulk_insert(DB_Client_Users.__table__,
    [
        {
            "id" : 1,
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
            "api_key" : "00101",         
            "country_id" : 4
        }
    ]
    )
    
    op.bulk_insert(DB_Mentor_Users.__table__,
    [
        {
            "id" : 1,
            "first_name" : "DR abed alrahman 1",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000001",        
            "email" : "aboud.masoud.1@gmail.com",
            "category_id" : 2,  
            "gender" : 1,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00001",         
            "country_id" : 1
        },
        {
            "id" : 2,
            "first_name" : "DR abed alrahman 2",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000002",        
            "email" : "aboud.masoud.2@gmail.com",
            "category_id" : 3,  
            "gender" : 2,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00002",         
            "country_id" : 2
        },        
        {
            "id" : 3,
            "first_name" : "DR abed alrahman 3",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000003",        
            "email" : "aboud.masoud.3@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00003",         
            "country_id" : 1
        },
        {
            "id" : 4,
            "first_name" : "DR abed alrahman 4",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000004",        
            "email" : "aboud.masoud.4@gmail.com",
            "category_id" : 4,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00004",         
            "country_id" : 1
        },
        {
            "id" : 5,
            "first_name" : "DR abed alrahman 5",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000005",        
            "email" : "aboud.masoud.5@gmail.com",
            "category_id" : 3,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00005",         
            "country_id" : 1
        },
        {
            "id" : 6,
            "first_name" : "DR abed alrahman 6",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000006",        
            "email" : "aboud.masoud.6@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00006",         
            "country_id" : 1
        },
        {
            "id" : 7,
            "first_name" : "DR abed alrahman 7",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000007",        
            "email" : "aboud.masoud.7@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00007",         
            "country_id" : 1
        },
        {
            "id" : 8,
            "first_name" : "DR abed alrahman 8",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000008",        
            "email" : "aboud.masoud.8@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00008",         
            "country_id" : 1
        },
        {
            "id" : 9,
            "first_name" : "DR abed alrahman 9",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000009",        
            "email" : "aboud.masoud.9@gmail.com",
            "category_id" : 4,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00009",         
            "country_id" : 1
        },
        {
            "id" : 10,
            "first_name" : "DR abed alrahman 10",
            "last_name" : "al haj hussain",         
            "mobile_number" : "009627900000010",        
            "email" : "aboud.masoud.10@gmail.com",
            "category_id" : 3,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000010",         
            "country_id" : 1
        },
        {
            "id" : 11,
            "first_name" : "DR abed alrahman 11",
            "last_name" : "al haj hussain",         
            "mobile_number" : "009627900000011",        
            "email" : "aboud.masoud.11@gmail.com",
            "category_id" : 7,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000011",         
            "country_id" : 3
        },
        {
            "id" : 12,
            "first_name" : "DR abed alrahman 12",
            "last_name" : "al haj hussain",         
            "mobile_number" : "009627900000012",        
            "email" : "aboud.masoud.12@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000012",         
            "country_id" : 2
        },
        {
            "id" : 13,
            "first_name" : "DR abed alrahman 13",
            "last_name" : "al haj hussain",         
            "mobile_number" : "009627900000013",        
            "email" : "aboud.masoud.13@gmail.com",
            "category_id" : 7,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000013",         
            "country_id" : 1
        },
        {
            "id" : 14,
            "first_name" : "DR abed alrahman 14",
            "last_name" : "al haj hussain",         
            "mobile_number" : "009627900000014",        
            "email" : "aboud.masoud.14@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000014",         
            "country_id" : 1
        },
        {
            "id" : 15,
            "first_name" : "DR abed alrahman 15",
            "last_name" : "al haj hussain",         
            "mobile_number" : "009627900000015",        
            "email" : "aboud.masoud.15@gmail.com",
            "category_id" : 5,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "me.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000015",         
            "country_id" : 2
        }
    ]
    )
    
    
    op.bulk_insert(DB_Notifications.__table__,
    [
        {
            "id" : 1,
            "title_english" : "notification title 1",
            "title_arabic" : "تنبيه رقم ١",         
            "content_english" : "notification content 1",
            "content_arabic" : "محتوى التنبيه ١",          
            "client_owner_id" : 1
        }
    ]
    )
    
    pass


def downgrade() -> None:
    pass
