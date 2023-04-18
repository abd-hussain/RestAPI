"""create data on tables

Revision ID: a26af631f1969
Revises: 
Create Date: 2022-10-20 12:40:47.209451

"""
import datetime
from alembic import op

from app.models.database.db_versions import DB_Versions, Platform
from app.models.database.db_country import DB_Countries
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users, DB_Mentor_Review
from app.models.database.db_category import DB_Categories
from app.models.database.db_notifications import DB_Notifications
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.db_mentor_banners import DB_Mentor_Banners
from app.models.database.client import db_client_user
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_majors import DB_Majors
from app.models.database.db_discount import DB_Discount
from app.models.database.db_appointment import DB_Appointments, AppointmentsState, AppointmentsType
from app.models.database.db_event import DB_Events, EventState, DB_EventReports
from app.models.database.db_suffix import DB_Suffix
from app.models.database.db_payments import DB_Mentor_Payments, PaymentStatus, TransactionType, DB_Mentor_PaymentsـReports
from app.models.database.db_add_loyality_request import DB_AddLoyalityRequest
from app.models.database.db_archive import DB_Archive

from app.utils.database import engine

# revision identifiers, used by Alembic.
revision = 'a26af631f1969'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    
    db_client_user.Base.metadata.drop_all(bind=engine)
    db_client_user.Base.metadata.create_all(bind=engine)

    op.bulk_insert(DB_Discount.__table__,
    [
        {
            "id" : 1,
            "code" : "abdo50",
            "percent_value" : 50,         
        },
        {
            "id" : 2,
            "code" : "abdo30",
            "percent_value" : 30,         
        },
        {
            "id" : 3,
            "code" : "abdo10",
            "percent_value" : 10,         
        },
        {
            "id" : 4,
            "code" : "abdo90",
            "percent_value" : 90,         
        },
        {
            "id" : 5,
            "code" : "abd100",
            "percent_value" : 100,         
        }
    ]
    )
    
    op.bulk_insert(DB_Versions.__table__,
    [
        {
            "id" : 1,
            "version" : 1.0,
            "content_arabic" : "اول اصدار",         
            "content_english" : "First Build",    
            "platform" : Platform.mentor,    
            "is_forced" : False
        },
        {
            "id" : 2,
            "version" : 1.0,
            "content_arabic" : "اول اصدار",         
            "content_english" : "First Build",    
            "platform" : Platform.client,    
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
            "dialCode" : "00973",
            "minLength" : 8,
            "maxLength": 8
        },
        {          
            "id" : 2,
            "flag_image" : "egypt.png",
            "name_english" : "Eqypt",         
            "name_arabic" : "مصر",     
            "currency_arabic" : "ج.م",
            "currency_english" : "EGP",        
            "dialCode" : "0020",
            "minLength" : 10,
            "maxLength": 10
        }, 
        {
            "id" : 3,
            "flag_image" : "iraq.png",
            "name_english" : "Iraq",         
            "name_arabic" : "العراق",  
            "currency_arabic" : "د.ع",
            "currency_english" : "IQD",        
            "dialCode" : "00964",
            "minLength" : 10,
            "maxLength": 10
        }, 
        {
            "id" : 4,
            "flag_image" : "jordan.png",
            "name_english" : "Jordan",         
            "name_arabic" : "الاردن",         
            "currency_arabic" : "د.ا",   
            "currency_english" : "JD",        
            "dialCode" : "00962",
            "minLength" : 9,
            "maxLength": 9
        },
        {
            "id" : 5,
            "flag_image" : "kuwait.png",
            "name_english" : "Kuwait",         
            "name_arabic" : "الكويت",         
            "currency_arabic" : "د.ك",
            "currency_english" : "KWD",        
            "dialCode" : "00965",
            "minLength" : 8,
            "maxLength": 8
        },
        {
            "id" : 6,
            "flag_image" : "qatar.png",
            "name_english" : "Qatar",         
            "name_arabic" : "قطر",         
            "currency_arabic" : "ر.ق",
            "currency_english" : "QR",        
            "dialCode" : "00974",
            "minLength" : 8,
            "maxLength": 8
        }, 
        {
            "id" : 7,
            "flag_image" : "saudi.png",
            "name_english" : "Saudi Arabia",         
            "name_arabic" : "المملكة العربية السعودية",         
            "currency_arabic" : "ر.س",
            "currency_english" : "Riyal",        
            "dialCode" : "00966",
            "minLength" : 9,
            "maxLength": 9
        }, 
        {
            "id" : 8,
            "flag_image" : "emirates.png",
            "name_english" : "United Arab Emirates",         
            "name_arabic" : "الإمارات العربيّة المتّحدة",         
            "currency_arabic" : "د.إ",
            "currency_english" : "Dh",       
            "dialCode" : "00971",
            "minLength" : 9,
            "maxLength": 9
        },
        {
            "id" : 9,
            "flag_image" : "lebanon.png",
            "name_english" : "Lebanon",         
            "name_arabic" : "لبنان",         
            "currency_arabic" : "دولار",
            "currency_english" : "USD",       
            "dialCode" : "00961",
            "minLength" : 8,
            "maxLength": 8
        },
        {
            "id" : 10,
            "flag_image" : "palestine.png",
            "name_english" : "Palestinian Territory, Occupied",         
            "name_arabic" : "فلسطين المحتلة",         
            "currency_arabic" : "شيكل",
            "currency_english" : "₪",       
            "dialCode" : "00970",
            "minLength" : 9,
            "maxLength": 9
        }, 
        {
            "id" : 11,
            "flag_image" : "othercountry.png",
            "name_english" : "Other",         
            "name_arabic" : "اخرى",         
            "currency_arabic" : "دولار",     
            "currency_english" : "USD",        
            "dialCode" : "0000",
            "minLength" : 9,
            "maxLength": 9
        }
    ]
    )
    
    op.bulk_insert(DB_Suffix.__table__,
    [
         {
            "id" : 1,
            "name_english" : "Mr.",         
            "name_arabic" : "سيد .",         
        },
         {
            "id" : 2,
            "name_english" : "Mrs.",         
            "name_arabic" : "سيدة .",     
        },
         {
            "id" : 3,
            "name_english" : "Dr.",         
            "name_arabic" : "د .",     
        },
         {
            "id" : 4,
            "name_english" : "Eng.",         
            "name_arabic" : "م .",     
        },
        {
            "id" : 5,
            "name_english" : "Ph.",         
            "name_arabic" : "ب .",     
        },
    ]
    )
        
    op.bulk_insert(DB_Categories.__table__,
    [
         {
            "id" : 1,
            "name_english" : "Psychology",         
            "name_arabic" : "طب نفسي",              
            "icon" : "psychology.png"
        },
         {
            "id" : 2,
            "name_english" : "Pediatrics",         
            "name_arabic" : "طب اطفال",              
            "icon" : "pediatrics.png"
        },
         {
            "id" : 3,
            "name_english" : "Diet & Nutrition",         
            "name_arabic" : "دايت و تغذيه",              
            "icon" : "diet.png"
        },
         {
            "id" : 4,
            "name_english" : "Sexology",         
            "name_arabic" : "مشاكل جنسيه",               
            "icon" : "sexology.png"
        },
         {
            "id" : 5,
            "name_english" : "Dermatology",         
            "name_arabic" : "مشاكل جلديه",               
            "icon" : "dermatology.png"
        },
         {
            "id" : 6,
            "name_english" : "Gynecology",         
            "name_arabic" : "امراض نسائيه",           
            "icon" : "gynecology.png"
        },
         {
            "id" : 7,
            "name_english" : "Homeopathy",         
            "name_arabic" : "علاج بالمواد الطبيعيه",              
            "icon" : "homeopathy.png"
        }
    ]
    )
    
    op.bulk_insert(DB_Majors.__table__,
    [
        {
            "id" : 1,
            "name_english" : "social phobia",
            "name_arabic" : "الرهاب الاجتماعي",         
        },
        {
            "id" : 2,
            "name_english" : "fear of death",
            "name_arabic" : "الخوف من الموت",         
        },
        {
            "id" : 3,
            "name_english" : "fear of the dark",
            "name_arabic" : "الخوف من الظلام",         
        },
        {
            "id" : 4,
            "name_english" : "mood disorder",
            "name_arabic" : "اضطراب المزاج",         
        },
        {
            "id" : 5,
            "name_english" : "Schizophrenia",
            "name_arabic" : "الفصام",         
        },
        {
            "id" : 6,
            "name_english" : "Pelage",
            "name_arabic" : "نتف الشعر",         
        },
        {
            "id" : 7,
            "name_english" : "Gender identity disorder",
            "name_arabic" : "اضطراب الهوية الجنسية",         
        },
        {
            "id" : 8,
            "name_english" : "Suicidal ideation",
            "name_arabic" : "التفكير بالانتحار",         
        },
        {
            "id" : 9,
            "name_english" : "low self esteem",
            "name_arabic" : "ضعف تقدير الذات",         
        },
        {
            "id" : 10,
            "name_english" : "Lack of understanding between the two parties",
            "name_arabic" : "عدم التفاهم بين الطرفين",         
        },
        {
            "id" : 11,
            "name_english" : "Lack of interest and appreciation",
            "name_arabic" : "عدم الاهتمام و التقدير",         
        },
        {
            "id" : 12,
            "name_english" : "The relationship between parents and children",
            "name_arabic" : "العلاقة بين الوالدين والأبناء",         
        },
        {
            "id" : 13,
            "name_english" : "The husband fell silent",
            "name_arabic" : "صمت الزوج",         
        },
        {
            "id" : 14,
            "name_english" : "Adolescent disorders",
            "name_arabic" : "اضطرابات المراهقين",         
        },
        {
            "id" : 15,
            "name_english" : "Emotional vacuum",
            "name_arabic" : "الفراغ العاطفي",         
        },
        {
            "id" : 16,
            "name_english" : "Marital intimacy",
            "name_arabic" : "العلاقات الحميمية الزوجية",         
        },
        {
            "id" : 17,
            "name_english" : "Watching porn movies",
            "name_arabic" : "مشاهدة الافلام الاباحية",         
        },
        {
            "id" : 18,
            "name_english" : "raising a child",
            "name_arabic" : "تربية الطفل",         
        },
        {
            "id" : 19,
            "name_english" : "Dealing with the elderly",
            "name_arabic" : "التعامل مع كبار السن",         
        },
        {
            "id" : 20,
            "name_english" : "Social communication skills",
            "name_arabic" : "مهارات التواصل الاجتماعي",         
        },
        {
            "id" : 21,
            "name_english" : "Promote positive thinking",
            "name_arabic" : "تعزيز التفكير الايجابي",         
        },
        {
            "id" : 22,
            "name_english" : "work discrimination",
            "name_arabic" : "التمييز بالعمل",         
        },
        {
            "id" : 23,
            "name_english" : "time management",
            "name_arabic" : "إدارة الوقت",         
        },
        {
            "id" : 24,
            "name_english" : "Isolation and introversion",
            "name_arabic" : "العزلة و الانطواء",         
        },
        {
            "id" : 25,
            "name_english" : "delusional illness",
            "name_arabic" : "توهم المرض",         
        },
        {
            "id" : 26,
            "name_english" : "Depression",
            "name_arabic" : "الاكتئاب",         
        },
        {
            "id" : 27,
            "name_english" : "anxiety",
            "name_arabic" : "القلق",         
        },
        {
            "id" : 28,
            "name_english" : "Obsessive",
            "name_arabic" : "الوسواس",         
        },
        {
            "id" : 29,
            "name_english" : "suspicion and jealousy",
            "name_arabic" : "الشك والغيرة",         
        },
        {
            "id" : 30,
            "name_english" : "lying",
            "name_arabic" : "الكذب",         
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
            "profile_img" : "",
            "os_type" : "iOS",         
            "device_type_name" : "iPhone XR",        
            "os_version" : "16.2",         
            "app_version" : "1.0",         
            "date_of_birth" : "1992/05/22",         
            "last_otp" : "0000",         
            "api_key" : "00101",
            "push_token" : "",         
            "country_id" : 4
        },
        {
            "id" : 2,
            "first_name" : "mohammed",
            "last_name" : "maswadeh",         
            "mobile_number" : "00962795190661",        
            "email" : "aboud.masoud.91@gmail.com",         
            "gender" : 2,         
            "hide_number" : False,         
            "hide_email" : False,        
            "allow_notifications" : True,         
            "blocked" : True,         
            "referal_code" : "",
            "profile_img" : "",
            "os_type" : "iOS",         
            "device_type_name" : "iPhone XR",        
            "os_version" : "16.2",         
            "app_version" : "1.0",         
            "date_of_birth" : "1992/05/22",         
            "last_otp" : "0000",         
            "api_key" : "00102",
            "push_token" : "",         
            "country_id" : 4
        }
    ]
    )
            
    op.bulk_insert(DB_Mentor_Users.__table__,
    [
        {
            "id" : 1,
            "category_id" : 1,
            "suffixe_name" : "Sr.",
            "first_name" : "abed alrahman 1",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 0],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000001",
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",
            "email" : "aboud.masoud.1@gmail.com",
            "gender" : 1,
            "hour_rate" : 20.5,         
            "referal_code" : "",
            "profile_img" : "1.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",   
            "experience_since" : "1992",
            "last_otp" : "0000",         
            "api_key" : "00001",
            "push_token" : "",    
            "country_id" : 1
        },
        {
            "id" : 2,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 2",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",          
            "speaking_language" : ["English", "العربية"],  
            "majors" : [1, 2, 3, 4, 5, 6, 7, 19, 18, 15, 17, 16, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000002",
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",        
            "email" : "aboud.masoud.2@gmail.com",
            "category_id" : 1,  
            "gender" : 2,  
            "hour_rate" : 34.7,                
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",   
            "experience_since" : "1999",      
            "last_otp" : "0000",         
            "api_key" : "00002",
            "push_token" : "",         
            "country_id" : 2
        },        
        {
            "id" : 3,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 3",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],            
            "majors" : [21, 22, 20, 24, 23, 6, 7, 19, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000003",
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",        
            "email" : "aboud.masoud.3@gmail.com",
            "category_id" : 2,
            "hour_rate" : 12.1,                  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2000",               
            "last_otp" : "0000",         
            "api_key" : "00003", 
            "push_token" : "",        
            "country_id" : 1
        },
        {
            "id" : 4,
            "suffixe_name" : "Mr.",
            "first_name" : "abed alrahman 4",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000004",   
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",             
            "email" : "aboud.masoud.4@gmail.com",
            "category_id" : 1,
            "hour_rate" : 65.0,                    
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2014",                        
            "last_otp" : "0000",         
            "api_key" : "00004",
            "push_token" : "",         
            "country_id" : 1
        },
        {
            "id" : 5,
            "suffixe_name" : "Mrs.",
            "first_name" : "abed alrahman 5",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000005",
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",                
            "email" : "aboud.masoud.5@gmail.com",
            "category_id" : 3,
            "hour_rate" : 33.0,                      
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2014",                                 
            "last_otp" : "0000",         
            "api_key" : "00005",
            "push_token" : "",         
            "country_id" : 1
        },
        {
            "id" : 6,
            "suffixe_name" : "Mrs.",
            "first_name" : "abed alrahman 6",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية", 
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000006",
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",                
            "email" : "aboud.masoud.6@gmail.com",
            "category_id" : 2,  
            "gender" : 0,
            "hour_rate" : 17.8,                               
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2014",                                 
            "last_otp" : "0000",         
            "api_key" : "00006",
            "push_token" : "",         
            "country_id" : 1
        },
        {
            "id" : 7,
            "suffixe_name" : "Mr.",
            "first_name" : "abed alrahman 7",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000007", 
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",               
            "email" : "aboud.masoud.7@gmail.com",
            "category_id" : 2,  
            "gender" : 0,
            "hour_rate" : 43.0,                                        
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2014",                              
            "last_otp" : "0000",         
            "api_key" : "00007",
            "push_token" : "",         
            "country_id" : 1
        },
        {
            "id" : 8,
            "suffixe_name" : "Sr.",
            "first_name" : "abed alrahman 8",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21],
            "mobile_number" : "00962790000008", 
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",               
            "email" : "aboud.masoud.8@gmail.com",
            "category_id" : 2,
            "hour_rate" : 77.2,                                          
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2019",                                       
            "last_otp" : "0000",         
            "api_key" : "00008",
            "push_token" : "",        
            "country_id" : 1
        },
        {
            "id" : 9,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 9",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "00962790000009",   
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",             
            "email" : "aboud.masoud.9@gmail.com",
            "category_id" : 4,
            "hour_rate" : 12.2,                                            
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2020",                                                
            "last_otp" : "0000",         
            "api_key" : "00009",
            "push_token" : "",        
            "country_id" : 1
        },
        {
            "id" : 10,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 10",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "009627900000010", 
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",               
            "email" : "aboud.masoud.10@gmail.com",
            "category_id" : 3,
            "hour_rate" : 28.9,                                              
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2000",                                                         
            "last_otp" : "0000",         
            "api_key" : "000010",
            "push_token" : "",         
            "country_id" : 1
        },
        {
            "id" : 11,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 11",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "009627900000011",   
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",             
            "email" : "aboud.masoud.11@gmail.com",
            "category_id" : 7,  
            "gender" : 0,
            "hour_rate" : 35.2,                                                       
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2000",                                                                  
            "last_otp" : "0000",         
            "api_key" : "000011",
            "push_token" : "",         
            "country_id" : 3
        },
        {
            "id" : 12,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 12",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "009627900000012", 
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",               
            "email" : "aboud.masoud.12@gmail.com",
            "category_id" : 2,  
            "gender" : 0,
            "hour_rate" : 52.1,                                                                
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2001",                                                                  
            "last_otp" : "0000",         
            "api_key" : "000012",
            "push_token" : "",         
            "country_id" : 2
        },
        {
            "id" : 13,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 13",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "009627900000013",  
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",              
            "email" : "aboud.masoud.13@gmail.com",
            "category_id" : 7,  
            "gender" : 0,  
            "hour_rate" : 11.0,                           
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2011",                                                                           
            "last_otp" : "0000",         
            "api_key" : "000013",
            "push_token" : "",         
            "country_id" : 1
        },
        {
            "id" : 14,
            "suffixe_name" : "Mr.",
            "first_name" : "abed alrahman 14",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "009627900000014", 
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",               
            "email" : "aboud.masoud.14@gmail.com",
            "category_id" : 2,  
            "gender" : 0,
            "hour_rate" : 14.0,                    
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2020",                                                                                    
            "last_otp" : "0000",         
            "api_key" : "000014",
            "push_token" : "",         
            "country_id" : 1
        },
        {
            "id" : 15,
            "suffixe_name" : "Mr.",
            "first_name" : "abed alrahman 15",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "majors" : [30, 22, 20, 28, 23, 6, 7, 29, 25, 27, 17, 26, 14],
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "mobile_number" : "009627900000015",
            "password" : "$2b$12$BVdr8Xp/t4AiwvmaCRfaKuicRzK5ss08le5t52lOXdRs2ndAHxhke",                
            "email" : "aboud.masoud.15@gmail.com",
            "category_id" : 5,  
            "gender" : 0, 
            "hour_rate" : 84.0,                            
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2021",                                                                                             
            "last_otp" : "0000",         
            "api_key" : "000015",
            "push_token" : "",         
            "country_id" : 2
        }
    ]
    )
    
    op.bulk_insert(DB_Appointments.__table__,
    [
        {
            "id" : 1,
            "mentor_id" : 1,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 2, 12, 8),
            "date_to" : datetime.datetime(2023, 2, 12, 9),
            "price_before_discount" : 20,
            "price_after_discount" : 10,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : "this is mentor note",
        },
        {
            "id" : 2,
            "mentor_id" : 1,            
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 2, 23, 14),    
            "date_to" : datetime.datetime(2023, 2, 23, 14, 30),
            "price_before_discount" : 9.9,
            "price_after_discount" : 9.9,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.active,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : None,
        },
        {
            "id" : 3,
            "mentor_id" : 2,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 2, 22, 10),    
            "date_to" : datetime.datetime(2023, 2, 22, 10, 15),
            "price_before_discount" : 10,
            "price_after_discount" : 10,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "note_from_client" : None,
            "note_from_mentor" : "this is mentor note",
        },
        {
            "id" : 4,
            "mentor_id" : 2,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 2, 28, 0),    
            "date_to" : datetime.datetime(2023, 2, 28, 0, 30),
            "price_before_discount" : 14,
            "price_after_discount" : 14,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "note_from_client" : None,
            "note_from_mentor" : "this is mentor note",
        },
        {
            "id" : 5,
            "mentor_id" : 3,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 3, 30, 10),    
            "date_to" : datetime.datetime(2023, 3, 30, 10, 15),
            "price_before_discount" : 21,
            "price_after_discount" : 20,
            "appointment_type" : AppointmentsType.instant,
            "state" : AppointmentsState.mentor_cancel,
            "note_from_client" : None,
            "note_from_mentor" : None,
        },
        {
            "id" : 6,
            "mentor_id" : 3,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 2, 28, 19),    
            "date_to" : datetime.datetime(2023, 2, 28, 19, 30),
            "price_before_discount" : 17,
            "price_after_discount" : 15,  
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.mentor_cancel,
            "note_from_client" : None,
            "note_from_mentor" : None,
        },
        {
            "id" : 7,
            "mentor_id" : 4,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 2, 28, 10),    
            "date_to" : datetime.datetime(2023, 2, 28, 11),
            "price_before_discount" : 12,
            "price_after_discount" : 12,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.client_cancel,
            "note_from_client" : None,
            "note_from_mentor" : None,
        },
        {
            "id" : 8,
            "mentor_id" : 4,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 2, 28, 17),    
            "date_to" : datetime.datetime(2023, 2, 28, 18),
            "price_before_discount" : 9,
            "price_after_discount" : 9,
            "appointment_type" : AppointmentsType.instant,
            "state" : AppointmentsState.client_cancel,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : None,
        },
        {
            "id" : 9,
            "mentor_id" : 5,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 2, 14, 14),    
            "date_to" : datetime.datetime(2023, 2, 14, 14, 15),
            "price_before_discount" : 12,
            "price_after_discount" : 12,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.mentor_miss,
            "note_from_client" : None,
            "note_from_mentor" : None,
        },
        {
            "id" : 10,
            "mentor_id" : 5,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 4, 30, 15),    
            "date_to" : datetime.datetime(2023, 4, 30, 15, 15),
            "price_before_discount" : 16.3,
            "price_after_discount" : 16,  
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.client_miss,
            "note_from_client" : None,
            "note_from_mentor" : None,
        },
        {
            "id" : 11,
            "mentor_id" : 6,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 2, 3, 14),    
            "date_to" : datetime.datetime(2023, 2, 3, 14, 30),
            "price_before_discount" : 12,
            "price_after_discount" : 12,   
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed, 
            "note_from_mentor" : "this is mentor note",
            "note_from_client" : None,
        },
        {
            "id" : 12,
            "mentor_id" : 6,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 2, 15, 15),    
            "date_to" : datetime.datetime(2023, 2, 15, 15, 30),
            "price_before_discount" : 12,
            "price_after_discount" : 12,     
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.active, 
            "note_from_client" : None,
            "note_from_mentor" : None,
        },
        {
            "id" : 13,
            "mentor_id" : 7,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 2, 16, 14),    
            "date_to" : datetime.datetime(2023, 2, 16, 15),
            "price_before_discount" : 12,
            "price_after_discount" : 12,       
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.active,
            "note_from_client" : None,
            "note_from_mentor" : None,
        },
        {
            "id" : 14,
            "mentor_id" : 7,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 4, 15, 15),    
            "date_to" : datetime.datetime(2023, 4, 15, 16),
            "price_before_discount" : 11,
            "price_after_discount" : 8.75,          
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : None,
        },
        {
            "id" : 15,
            "mentor_id" : 7,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 3, 17, 17),    
            "date_to" : datetime.datetime(2023, 3, 17, 18),
            "price_before_discount" : 7.8,
            "price_after_discount" : 7.8,               
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : None,
        }
    ]
    )
    
    op.bulk_insert(DB_Mentor_Review.__table__,
    [
        {
            "id" : 1,
            "mentor_id" : 4,
            "client_id" : 1,         
            "stars" : 4.7,        
            "comment" : "nice 1"
        },
        {
            "id" : 2,
            "mentor_id" : 4,
            "client_id" : 2,         
            "stars" : 3.2,        
            "comment" : "nice 2"
        },
    ]
    )
    
    op.bulk_insert(DB_Archive.__table__,
    [
       
        {
            "id" : 1,
            "mentor_id" : 1,
            "client_id" : 1,
            "appointment_type" : AppointmentsType.schudule,
            "date_from" : datetime.datetime(2023, 2, 12, 8),
            "date_to" : datetime.datetime(2023, 2, 12, 9),
            "price_before_discount" : 30,
            "price_after_discount" : 15,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : "this is mentor note",
            "attachment" : "32rcv2324f.mp4"
        },
        {
            "id" : 2,
            "mentor_id" : 1,            
            "client_id" : 2,
            "appointment_type" : AppointmentsType.schudule,
            "date_from" : datetime.datetime(2023, 2, 12, 8),
            "date_to" : datetime.datetime(2023, 2, 12, 9),
            "price_before_discount" : 20,
            "price_after_discount" : 20,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : "this is mentor note",
            "attachment" : "234t32rf23fv.mp4"
        },
        {
            "id" : 3,
            "mentor_id" : 2,
            "client_id" : 1,
            "appointment_type" : AppointmentsType.instant,
            "date_from" : datetime.datetime(2023, 2, 12, 8),
            "date_to" : datetime.datetime(2023, 2, 12, 9),
            "price_before_discount" : 20,
            "price_after_discount" : 10,
            "note_from_client" : "this is Client note",
            "note_from_mentor" : "this is mentor note",
            "attachment" : "326982364.mp4"
        },
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
            "client_owner_id" : 1,
            "mentor_owner_id" : None,
        },
        {
            "id" : 2,
            "title_english" : "notification title 2",
            "title_arabic" : "تنبيه رقم ٢",         
            "content_english" : "notification content 2",
            "content_arabic" : "محتوى التنبيه ٢",          
            "client_owner_id" : 1,
            "mentor_owner_id" : None,
        },
        {
            "id" : 3,
            "title_english" : "notification title 3",
            "title_arabic" : "تنبيه رقم 3",         
            "content_english" : "notification content 3",
            "content_arabic" : "محتوى التنبيه 3",    
            "client_owner_id" : None,      
            "mentor_owner_id" : 1,
        },
        {
            "id" : 4,
            "title_english" : "notification title 4",
            "title_arabic" : "تنبيه رقم 4",         
            "content_english" : "notification content 4",
            "content_arabic" : "محتوى التنبيه 4",    
            "client_owner_id" : None,      
            "mentor_owner_id" : 1,
        }          
    ]
    )
    
    op.bulk_insert(DB_AddLoyalityRequest.__table__,
    []
    )
    
    op.bulk_insert(DB_Mentor_Banners.__table__,
    [
        {
            "id" : 1,      
            "language" : "en",
            "image" : "banner1.jpg",
            "published" : True      
        },
        {
            "id" : 2,      
            "language" : "en",
            "image" : "banner2.jpg",
            "action_type" : "https://www.youtube.com/watch?v=FrCO41i2tWM&ab_channel=%D8%AD%D8%B3%D9%86%D8%A7%D9%84%D9%81%D8%A7%D8%B6%D9%84%D9%8A-ElfadiliTV",
            "published" : True         
        },
        {
            "id" : 3,      
            "language" : "ar",
            "image" : "banner3.jpg",
            "published" : True            
        },
        {
            "id" : 4,      
            "language" : "ar",
            "image" : "banner4.jpeg",
            "published" : True           
        },
    ]
    )
    
    op.bulk_insert(DB_Client_Banners.__table__,
    [
        {
            "id" : 1,      
            "language" : "en",
            "image" : "banner1.jpg",
            "published" : True      
        },
        {
            "id" : 2,      
            "language" : "en",
            "image" : "banner2.jpg",
            "action_type" : "https://www.youtube.com/watch?v=FrCO41i2tWM&ab_channel=%D8%AD%D8%B3%D9%86%D8%A7%D9%84%D9%81%D8%A7%D8%B6%D9%84%D9%8A-ElfadiliTV",
            "published" : True         
        },
        {
            "id" : 3,      
            "language" : "ar",
            "image" : "banner3.jpg",
            "action_type" : "https://www.youtube.com/watch?v=FrCO41i2tWM&ab_channel=%D8%AD%D8%B3%D9%86%D8%A7%D9%84%D9%81%D8%A7%D8%B6%D9%84%D9%8A-ElfadiliTV",
            "published" : True            
        },
        {
            "id" : 4,      
            "language" : "ar",
            "image" : "banner4.jpg",
            "published" : True           
        },
        {
            "id" : 5,      
            "language" : "ar",
            "image" : "banner4.jpeg",
            "action_type" : "null",
            "published" : False           
        }
    ]
    )
    
    op.bulk_insert(DB_Events.__table__,
    [
          {
            "id" : 1,
            "owner_id" : 1,
            "image" : "event1.jpeg",         
            "title" : "نقاش كتاب “أصل التفاوت بين الناس” – جان جاك روسو",        
            "description" : "يعدُّ كتاب  أصل التفاوت بين الناس لجان جاك روسو من الكلاسيكيات الفلسفية والاجتماعية العالمية، لما له من أهمية مفصلية في ترسيم حدود فاصلة يُبنَى عليها التفكير في نشأة التفاوت الاجتماعي والصراعات المترتبة عليه ويهتم هذا الكتاب بإجلاء مبادئ الديمقراطية السياسية القائمة على إرساء قواعد الاشتراكية التي دعا إليها روسو. ويحمل هذا الكتاب تأملات الإنسان التي تُستلهَم من طبيعته المتجردة التي تحمل في طَوِيَّتها جوهر الأصالة في التكوين الإنساني، وذلك من خلال دراسته للإنسان، وحاجاته الحقيقية ويشتمل الكتاب على وصف خيالي لحال الإنسان الذي تكبله الأغلال في كل مكان، كما يعلِّل الفساد القائم بين البشر بالتفاوت بين أفراد المجتمع في المعاملات ومَنْ يقرأ هذا الكتاب يدرك أنه أمام نصٍّ فلسفيٍّ فريد استطاع أن يفرض نفسه لثلاثة قرون على الفكر البشري",
            "max_number_of_attendance" : 11,
            "date_from" : datetime.datetime(2023, 5, 31, 8),
            "date_to" : datetime.datetime(2023, 5, 31, 9),
            "price" : 0,
            "state" : EventState.active,
        },
            {
            "id" : 2,
            "owner_id" : 2,
            "image" : "event2.png",         
            "title" : "دورة صناعة الصابون على الطريقة الباردة",        
            "description" : "الأهداف: 1. تعريف بأنواع الزيوت المناسبة لكل نوع بشرة والتي تدخل في صناعة الصابون 2. تعلم من الصفر طريقة صنع انواع متعددة من الصابون على الطريقة الباردة مثل • صابونة زيت الزيتون البلدي • صابونة الكركم والليمون لعلاج التصبغات الجلدية وتفتيح لون البشرة • صابونة الشوفان والعسل لعلاج جفاف البشرة ومحاربة التجاعيد • صابونة اللافندر والورد المطهرة للبشرة والمضادة للإلتهابات • صابونة المسك والعنبر المعطرة ٣- تعلم كيفية استعمال حاسبة الصابون ٤- تعلم طرق لتسويق منتجاتكم الفئة المستهدفة: المهتمون بصناعة الصابون، رواد الاعمال والعاملون في التجميل، أصحاب الصالونات ومراكز التجميل. الدورة تساعدك على:  فتح مشروع تجاري خاص  صناعة الصابون من الصفر • ستعود الي بيتك مع الصابون الذي صنعته بيديك الزمان والمكان: السبت في 28 كانون الثاني، من الساعة 10:30 صباحاً حتى 5:30 عصراً، في مركز IABC بيروت، مستديرة الطيونة، بناية سنتر الطيونة، الطابق التاسع المدربة: جنان دوغان وهي أخصائية تجميل، حاصلة على شهادة من جامة ،ESMOD Dubai كما شاركت في عدة دورات مختصة بصناعة منتجات العناية بالبشرة الطبيعية. استثمار الدورة: مليونان و500 ألف ليرة لبنانية، تشمل:  المواد الاولية والزيوت للتدريب التطبيقي  المادة التدريبية العلمية • شهادة معتمدة في تصنيع الصابون • غداء وكافي بريك ",
            "max_number_of_attendance" : 8,
            "date_from" : datetime.datetime(2023, 4, 5, 8),
            "date_to" : datetime.datetime(2023, 4, 5, 8, 30),
            "price" : 10,
            "state" : EventState.active,
        },
        {
            "id" : 3,
            "owner_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "max_number_of_attendance" : 17,
            "date_from" : datetime.datetime(2023, 7, 5, 8),
            "date_to" : datetime.datetime(2023, 7, 5, 8, 30),
            "price" : 25,
            "state" : EventState.active,
        },
        {
            "id" : 4,
            "owner_id" : 4,
            "image" : "event4.jpeg",         
            "title" : "مساابقة القدس لحفظ القرآن الكريم وتجويده(الموسم السادس)]",        
            "description" : "مساابقة القدس لحفظ القرآن الكريم وتجويده(الموسم السادس)",
            "max_number_of_attendance" : 30,
            "date_from" : datetime.datetime(2023, 4, 4, 12),
            "date_to" : datetime.datetime(2023, 4, 4, 12, 30),
            "price" : 0,
            "state" : EventState.active,
        },
        {
            "id" : 5,
            "owner_id" : 1,
            "image" : "event5.jpeg",         
            "title" : "يوم الأرض زراعة النباتات في حدائق المتحف الفلسطيني | Planting in the Palestinian Museum gardens",        
            "description" : "Land Day Planting in the Palestinian Museum gardens Thursday, March 30th | 10:00-14:00 Location: Palestinian Museum gardens Language: Arabic Join us for a fun event in the gardens of the Palestinian Museum to commemorate Land Day. Together we will plant seedlings of various vegetables, such as tomatoes, cucumbers, zucchini, okra, and perhaps some flowers and decorative plants. Enjoy learning useful and fun facts on how to successfully plant!",
            "max_number_of_attendance" : 100,
            "date_from" : datetime.datetime(2023, 5, 15, 22),
            "date_to" : datetime.datetime(2023, 5, 15, 23),
            "price" : 0,
            "state" : EventState.active,
        },
        {
            "id" : 6,
            "owner_id" : 2,
            "image" : "event6.jpeg",         
            "title" : "Summer Jam 6",        
            "description" : "Summer Jam (6) The Jungle Land They say if you want to be a party animal you have to live in the jungle! Well now the jungle is brought to you by Summer Jam (6).. Get ready to unleash the party animal inside you! * 12 Hours of NON-STOP music performed by: - Top artists in Mena region - Best Djs in town - This event is family oriented - Kids area - Pet friendly - Food courts and play areas * P.S. This event is alcohol free Buy your early bird tickets starting today for 30 JDs Or get the Regular ticket in April for 40 JDS And if you’re lazy, you can just buy the ticket at the door for 50 JDs Stay tuned for more information, and until then, spread the news! For more information: +962 7 7565 6765",
            "max_number_of_attendance" : 100,
            "date_from" : datetime.datetime(2023, 5, 5, 22),
            "date_to" : datetime.datetime(2023, 5, 5, 23, 59),
            "price" : 30,
            "state" : EventState.active,
        },
        {
            "id" : 7,
            "owner_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "max_number_of_attendance" : 15,
            "date_from" : datetime.datetime(2023, 1, 1, 8),
            "date_to" : datetime.datetime(2023, 1, 1, 8, 30),
            "price" : 25,
            "state" : EventState.completed,
        },
        {
            "id" : 8,
            "owner_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "max_number_of_attendance" : 20,
            "date_from" : datetime.datetime(2023, 1, 1, 8),
            "date_to" : datetime.datetime(2023, 1, 1, 8, 30),
            "price" : 25,
            "state" : EventState.mentor_miss,
        },
        {
            "id" : 9,
            "owner_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "max_number_of_attendance" : 4,
            "date_from" : datetime.datetime(2023, 1, 1, 8),
            "date_to" : datetime.datetime(2023, 1, 1, 8, 30),
            "price" : 25,
            "state" : EventState.mentor_cancel,
        },
    ]
    )
    
    op.bulk_insert(DB_EventReports.__table__,
    [
        {
            "user_id" : 1,      
            "event_id" : 1,
        },
    ]
    )

    op.bulk_insert(DB_Mentor_Payments.__table__,
    [
        {
            "id" : 1,
            "mentor_id" : 1,
            "status" : PaymentStatus.pending,   
            "amount" : 12,   
            "currency_arabic" : "د.ا",   
            "currency_english" : "JD",    
            "descriptions" : "Meeting with client saleh yousef",    
            "durations" : 30, 
            "type" : TransactionType.debit,                                                                                       
        },
        {
            "id" : 2,
            "mentor_id" : 1,
            "status" : PaymentStatus.pending,   
            "amount" : 40.2,   
            "currency_arabic" : "د.ا",   
            "currency_english" : "JD",    
            "descriptions" : "Meeting with client zaid Barghouthi",    
            "durations" : 45, 
            "type" : TransactionType.debit,                                                                                       
        },        
        {
            "id" : 3,
            "mentor_id" : 2,
            "status" : PaymentStatus.pending,   
            "amount" : 19.2,   
            "currency_arabic" : "د.ا",   
            "currency_english" : "JD",    
            "descriptions" : "Meeting with client zaid Barghouthi",    
            "durations" : 45, 
            "type" : TransactionType.debit,                                                                                       
        }, 
        {
            "id" : 4,
            "mentor_id" : 1,
            "status" : PaymentStatus.approved,   
            "amount" : 18.56,   
            "currency_arabic" : "د.ا",   
            "currency_english" : "JD",    
            "descriptions" : "Meeting with client Moahmmed Flafil",    
            "durations" : 60, 
            "type" : TransactionType.credit,  
            "notes" : "delay allowance"                                                                                 
        },
    ]
    )
    
    op.bulk_insert(DB_Mentor_PaymentsـReports.__table__,
    [
        {
            "id" : 1,
            "mentor_id" : 1,
            "payment_id" : 1,   
            "message" : "There is Something wrong",                                                                                      
        },
        {
            "id" : 2,
            "mentor_id" : 1,
            "payment_id" : 4,   
            "message" : "There is Something wrong",                                                                                     
        },     
    ]
    )

    pass


def downgrade() -> None:
    pass
