"""create data on tables

Revision ID: a26af631f1969
Revises: 
Create Date: 2022-10-20 12:40:47.209451

"""
import datetime
from alembic import op

from app.models.database.db_versions import DB_Versions
from app.models.database.db_country import DB_Countries
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users,  DB_Stories, DB_StoryReports, DB_Mentor_Review
from app.models.database.db_category import DB_Categories
from app.models.database.db_notifications import DB_Notifications
from app.models.database.db_loyality_rules import DB_Loyality
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.db_tips import DB_Tips, DB_TipsQuestions, DB_TipsUsersAnswer, DB_TipsResult
from app.models.database.client import db_client_user
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_majors import DB_Majors
from app.models.database.db_discount import DB_Discount
from app.models.database.db_appointment import DB_Appointments, AppointmentsState, AppointmentsType
from app.models.database.db_event import DB_Events, EventState

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
            "email" : "aboud.masoud.1@gmail.com",
            "gender" : 1,         
            "referal_code" : "",
            "profile_img" : "1.png",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00001",         
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
            "email" : "aboud.masoud.2@gmail.com",
            "category_id" : 1,  
            "gender" : 2,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00002",         
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
            "email" : "aboud.masoud.3@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00003",         
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
            "email" : "aboud.masoud.4@gmail.com",
            "category_id" : 1,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00004",         
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
            "email" : "aboud.masoud.5@gmail.com",
            "category_id" : 3,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00005",         
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
            "email" : "aboud.masoud.6@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00006",         
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
            "email" : "aboud.masoud.7@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00007",         
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
            "email" : "aboud.masoud.8@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00008",         
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
            "email" : "aboud.masoud.9@gmail.com",
            "category_id" : 4,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "00009",         
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
            "email" : "aboud.masoud.10@gmail.com",
            "category_id" : 3,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000010",         
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
            "email" : "aboud.masoud.11@gmail.com",
            "category_id" : 7,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000011",         
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
            "email" : "aboud.masoud.12@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000012",         
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
            "email" : "aboud.masoud.13@gmail.com",
            "category_id" : 7,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000013",         
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
            "email" : "aboud.masoud.14@gmail.com",
            "category_id" : 2,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000014",         
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
            "email" : "aboud.masoud.15@gmail.com",
            "category_id" : 5,  
            "gender" : 0,         
            "referal_code" : "",
            "profile_img" : "",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",         
            "last_otp" : "0000",         
            "api_key" : "000015",         
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
            "date_from" : datetime.datetime(2022, 12, 30, 8),
            "date_to" : datetime.datetime(2022, 12, 30, 9),
            "price_before_discount" : 20,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "discount_id" : 1,
        },
        {
            "id" : 2,
            "mentor_id" : 1,            
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 1, 4, 14),    
            "date_to" : datetime.datetime(2023, 1, 4, 14, 30),
            "price_before_discount" : 9.9,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.active,
            "discount_id" : 2,
        },
        {
            "id" : 3,
            "mentor_id" : 2,
            "client_id" : 1,
            "date_from" : datetime.datetime(2022, 12, 30, 10),    
            "date_to" : datetime.datetime(2022, 12, 30, 10, 15),
            "price_before_discount" : 10,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "discount_id" : 3,     
        },
        {
            "id" : 4,
            "mentor_id" : 2,
            "client_id" : 2,
            "date_from" : datetime.datetime(2022, 12, 30, 0),    
            "date_to" : datetime.datetime(2022, 12, 30, 0, 30),
            "price_before_discount" : 14,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "discount_id" : 3,           
        },
        {
            "id" : 5,
            "mentor_id" : 3,
            "client_id" : 1,
            "date_from" : datetime.datetime(2022, 12, 30, 10),    
            "date_to" : datetime.datetime(2022, 12, 30, 10, 15),
            "price_before_discount" : 21,
            "appointment_type" : AppointmentsType.instant,
            "state" : AppointmentsState.mentor_cancel,
            "discount_id" : 5,       
        },
        {
            "id" : 6,
            "mentor_id" : 3,
            "client_id" : 2,
            "date_from" : datetime.datetime(2022, 12, 30, 19),    
            "date_to" : datetime.datetime(2022, 12, 30, 19, 30),
            "price_before_discount" : 17,  
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.mentor_cancel,
            "discount_id" : None,           
        },
        {
            "id" : 7,
            "mentor_id" : 4,
            "client_id" : 2,
            "date_from" : datetime.datetime(2022, 12, 30, 10),    
            "date_to" : datetime.datetime(2022, 12, 30, 11),
            "price_before_discount" : 12,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.client_cancel,
            "discount_id" : None,                
        },
        {
            "id" : 8,
            "mentor_id" : 4,
            "client_id" : 1,
            "date_from" : datetime.datetime(2022, 12, 30, 17),    
            "date_to" : datetime.datetime(2022, 12, 30, 18),
            "price_before_discount" : 9,
            "appointment_type" : AppointmentsType.instant,
            "state" : AppointmentsState.client_cancel,
            "discount_id" : None,                   
        },
        {
            "id" : 9,
            "mentor_id" : 5,
            "client_id" : 1,
            "date_from" : datetime.datetime(2022, 12, 30, 14),    
            "date_to" : datetime.datetime(2022, 12, 30, 14, 15),
            "price_before_discount" : 12,
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.mentor_miss,
            "discount_id" : None,                       
        },
        {
            "id" : 10,
            "mentor_id" : 5,
            "client_id" : 2,
            "date_from" : datetime.datetime(2022, 12, 30, 15),    
            "date_to" : datetime.datetime(2022, 12, 30, 15, 15),
            "price_before_discount" : 16.3,  
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.client_miss, 
            "discount_id" : None,                        
        },
        {
            "id" : 11,
            "mentor_id" : 6,
            "client_id" : 2,
            "date_from" : datetime.datetime(2023, 1, 3, 14),    
            "date_to" : datetime.datetime(2023, 1, 3, 14, 30),
            "price_before_discount" : 12, 
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.active, 
            "discount_id" : None,                       
        },
        {
            "id" : 12,
            "mentor_id" : 6,
            "client_id" : 1,
            "date_from" : datetime.datetime(2023, 1, 3, 15),    
            "date_to" : datetime.datetime(2023, 1, 3, 15, 30),
            "price_before_discount" : 12,  
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.active, 
            "discount_id" : None,   
        },
        {
            "id" : 13,
            "mentor_id" : 7,
            "client_id" : 1,
            "date_from" : datetime.datetime(2022, 1, 6, 14),    
            "date_to" : datetime.datetime(2022, 1, 6, 15),
            "price_before_discount" : 12,    
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.active,
            "discount_id" : None,   
        },
        {
            "id" : 14,
            "mentor_id" : 7,
            "client_id" : 2,
            "date_from" : datetime.datetime(2022, 12, 30, 15),    
            "date_to" : datetime.datetime(2022, 12, 30, 16),
            "price_before_discount" : 11,   
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "discount_id" : None,     
        },
        {
            "id" : 15,
            "mentor_id" : 7,
            "client_id" : 2,
            "date_from" : datetime.datetime(2022, 12, 30, 17),    
            "date_to" : datetime.datetime(2022, 12, 30, 18),
            "price_before_discount" : 7.8,     
            "appointment_type" : AppointmentsType.schudule,
            "state" : AppointmentsState.completed,
            "discount_id" : None,   
        }
    ]
    )
    
    
    op.bulk_insert(DB_Events.__table__,
    [
          {
            "id" : 1,
            "mentor_id" : 1,
            "image" : "event1.jpeg",         
            "title" : "نقاش كتاب “أصل التفاوت بين الناس” – جان جاك روسو",        
            "description" : "يعدُّ كتاب  أصل التفاوت بين الناس لجان جاك روسو من الكلاسيكيات الفلسفية والاجتماعية العالمية، لما له من أهمية مفصلية في ترسيم حدود فاصلة يُبنَى عليها التفكير في نشأة التفاوت الاجتماعي والصراعات المترتبة عليه ويهتم هذا الكتاب بإجلاء مبادئ الديمقراطية السياسية القائمة على إرساء قواعد الاشتراكية التي دعا إليها روسو. ويحمل هذا الكتاب تأملات الإنسان التي تُستلهَم من طبيعته المتجردة التي تحمل في طَوِيَّتها جوهر الأصالة في التكوين الإنساني، وذلك من خلال دراسته للإنسان، وحاجاته الحقيقية ويشتمل الكتاب على وصف خيالي لحال الإنسان الذي تكبله الأغلال في كل مكان، كما يعلِّل الفساد القائم بين البشر بالتفاوت بين أفراد المجتمع في المعاملات ومَنْ يقرأ هذا الكتاب يدرك أنه أمام نصٍّ فلسفيٍّ فريد استطاع أن يفرض نفسه لثلاثة قرون على الفكر البشري",
            "joining_clients_ids" : [1, 2],
            "max_number_of_attendance" : 11,
            "date_from" : datetime.datetime(2023, 1, 31, 8),
            "date_to" : datetime.datetime(2023, 1, 31, 9),
            "price" : 0,
            "state" : EventState.active,
        },
            {
            "id" : 2,
            "mentor_id" : 2,
            "image" : "event2.png",         
            "title" : "دورة صناعة الصابون على الطريقة الباردة",        
            "description" : "الأهداف: 1. تعريف بأنواع الزيوت المناسبة لكل نوع بشرة والتي تدخل في صناعة الصابون 2. تعلم من الصفر طريقة صنع انواع متعددة من الصابون على الطريقة الباردة مثل • صابونة زيت الزيتون البلدي • صابونة الكركم والليمون لعلاج التصبغات الجلدية وتفتيح لون البشرة • صابونة الشوفان والعسل لعلاج جفاف البشرة ومحاربة التجاعيد • صابونة اللافندر والورد المطهرة للبشرة والمضادة للإلتهابات • صابونة المسك والعنبر المعطرة ٣- تعلم كيفية استعمال حاسبة الصابون ٤- تعلم طرق لتسويق منتجاتكم الفئة المستهدفة: المهتمون بصناعة الصابون، رواد الاعمال والعاملون في التجميل، أصحاب الصالونات ومراكز التجميل. الدورة تساعدك على:  فتح مشروع تجاري خاص  صناعة الصابون من الصفر • ستعود الي بيتك مع الصابون الذي صنعته بيديك الزمان والمكان: السبت في 28 كانون الثاني، من الساعة 10:30 صباحاً حتى 5:30 عصراً، في مركز IABC بيروت، مستديرة الطيونة، بناية سنتر الطيونة، الطابق التاسع المدربة: جنان دوغان وهي أخصائية تجميل، حاصلة على شهادة من جامة ،ESMOD Dubai كما شاركت في عدة دورات مختصة بصناعة منتجات العناية بالبشرة الطبيعية. استثمار الدورة: مليونان و500 ألف ليرة لبنانية، تشمل:  المواد الاولية والزيوت للتدريب التطبيقي  المادة التدريبية العلمية • شهادة معتمدة في تصنيع الصابون • غداء وكافي بريك ",
            "joining_clients_ids" : [3, 2],
            "max_number_of_attendance" : 8,
            "date_from" : datetime.datetime(2023, 2, 5, 8),
            "date_to" : datetime.datetime(2023, 2, 5, 8, 30),
            "price" : 10,
            "state" : EventState.active,
        },
        {
            "id" : 3,
            "mentor_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "joining_clients_ids" : [],
            "max_number_of_attendance" : 17,
            "date_from" : datetime.datetime(2023, 2, 5, 8),
            "date_to" : datetime.datetime(2023, 2, 5, 8, 30),
            "price" : 25,
            "state" : EventState.active,
        },
        {
            "id" : 4,
            "mentor_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "joining_clients_ids" : [],
            "max_number_of_attendance" : 15,
            "date_from" : datetime.datetime(2023, 1, 1, 8),
            "date_to" : datetime.datetime(2023, 1, 1, 8, 30),
            "price" : 25,
            "state" : EventState.completed,
        },
        {
            "id" : 5,
            "mentor_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "joining_clients_ids" : [],
            "max_number_of_attendance" : 20,
            "date_from" : datetime.datetime(2023, 1, 1, 8),
            "date_to" : datetime.datetime(2023, 1, 1, 8, 30),
            "price" : 25,
            "state" : EventState.mentor_miss,
        },
        {
            "id" : 6,
            "mentor_id" : 4,
            "image" : "event3.jpeg",         
            "title" : "Promotional Campaign [JUST LC]",        
            "description" : "Defining an addiction is a tricky business, and knowing how to handle it is even harder That’s why YULC will be hosting it’s 2nd Local General Assembly “LGA” where we are going to talk about addiction as an important and common problem we’re facing each day in it’s different types. As IFMSA-Jo YULC Family, we're welcoming you to join us to be together hand in hand and fight it . The event will be held on 7th of January in the faculty of medicine starting at 8 AM. It will involve different standing committee sessions and trainings :Traning new trainers ,Teaching medical skills, Sexual and reproductive health and rights sessions ,as well as our beloved speakers who will be talking about addiction. And of course not to forget the best part of an LGA the social event where you get to know each other ,make new friends and have a lot of fun.",
            "joining_clients_ids" : [],
            "max_number_of_attendance" : 4,
            "date_from" : datetime.datetime(2023, 1, 1, 8),
            "date_to" : datetime.datetime(2023, 1, 1, 8, 30),
            "price" : 25,
            "state" : EventState.mentor_cancel,
        },
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
    
    op.bulk_insert(DB_Notifications.__table__,
    [
        {
            "id" : 1,
            "title_english" : "notification title 1",
            "title_arabic" : "تنبيه رقم ١",         
            "content_english" : "notification content 1",
            "content_arabic" : "محتوى التنبيه ١",          
            "client_owner_id" : 1
        },
        {
            "id" : 2,
            "title_english" : "notification title 2",
            "title_arabic" : "تنبيه رقم ٢",         
            "content_english" : "notification content 2",
            "content_arabic" : "محتوى التنبيه ٢",          
            "client_owner_id" : 1
        },
        {
            "id" : 3,
            "title_english" : "notification title 2",
            "title_arabic" : "تنبيه رقم ٢",         
            "content_english" : "notification content 2",
            "content_arabic" : "محتوى التنبيه ٢",    
            "client_owner_id" : None,      
            "mentor_owner_id" : 1,
        }        
    ]
    )
    
    
    op.bulk_insert(DB_Loyality.__table__,
    [
        {
            "id" : 1,      
            "content_english" : "Fill your profile details",
            "content_arabic" : "املا معلومات الحساب الخاص بك",
            "points" : 3,
            "action" : "EDITPROFILE"      
        },
        {
            "id" : 2,      
            "content_english" : "For each Friend Invite",
            "content_arabic" : "لكل دعوة صديق",
            "points" : 2,
            "action" : "INVITEFRIEND"         
        },
        {
            "id" : 3,      
            "content_english" : "Add Suggestion",
            "content_arabic" : "اضافة اقتراح",
            "points" : 1,
            "action" : "REPORTSUGESTION"         
        },
        {
            "id" : 4,      
            "content_english" : "Add Issue",
            "content_arabic" : "اضافة مشكلة",
            "points" : 1,
            "action" : "REPORTISSUE"         
        },
        {
            "id" : 5,      
            "content_english" : "Add Good Review",
            "content_arabic" : "اضافة تقيم جيد للبرنامج",
            "points" : 5,
            "action" : "REVIEW"         
        },
        {
            "id" : 6,      
            "content_english" : "Like Our Facebook Page",
            "content_arabic" : "متابعة صفحتنا على فيسبوك",
            "points" : 1,
            "action" : "LIKEFACEBOOK"         
        },
        {
            "id" : 7,      
            "content_english" : "Like Our LinkedIn Page",
            "content_arabic" : "متابعة صفحتنا على لينكيدان",
            "points" : 1,
            "action" : "LIKELINKEDIN"         
        },
        {
            "id" : 8,      
            "content_english" : "Add Good Review To Mentor",
            "content_arabic" : "اضافة تقيم جيد للمدرب",
            "points" : 1,
            "action" : "REVIEWMENTOR"         
        }
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
            "image" : "banner4.jpg",
            "action_type" : "null",
            "published" : False           
        }
    ]
    )
    
    op.bulk_insert(DB_Stories.__table__,
    [
        {
            "id" : 1,      
            "language" : "en",
            "assets" : "story1.jpeg",
            "owner_id" : 1,
            "published" : True      
        },
        {
            "id" : 2,      
            "language" : "en",
            "assets" : "story2.jpeg",
            "owner_id" : 2,
            "published" : True         
        },
        {
            "id" : 3,      
            "language" : "en",
            "assets" : "story3.jpeg",
            "owner_id" : 3,
            "published" : False          
        },
        {
            "id" : 4,      
            "language" : "ar",
            "assets" : "story3.jpeg",
            "owner_id" : 1,
            "published" : True             
        },
        {
            "id" : 5,      
            "language" : "ar",
            "assets" : "story4.jpeg",
            "owner_id" : 3,
            "published" : True                
        }
    ]
    )
    
    op.bulk_insert(DB_StoryReports.__table__,
    [
        {
            "user_id" : 1,      
            "story_id" : 1,
        },
        {
            "user_id" : 1,      
            "story_id" : 2,
        }
    ]
    )
    
    op.bulk_insert(DB_Tips.__table__,
    [
        {
            "id" : 1,
            "category_id" : 3,
            "title_arabic" : "البرنامج العلاجي لاضطراب الاكتئاب",
            "title_english" : "Therapeutic program for depressive disorder",
            "desc_arabic" : "سيساعدك هذا الاختبار البسيط على تقييم و معرفة مستوى الاكتئاب لديك، اجاباتك ستساعدنا في تحديد مستوى صحتك النفسية",
            "desc_english" : "This simple test will help you assess and know your level of depression. Your answers will help us determine your level of mental health",
            "note_arabic" : "هذا الاختبار لا يعتبر اداة تشخيص او اداة علاج وقد لا تغني عن جلسة خاصة مع الطبيب او المختص المناسب",
            "note_english" : "This test is not considered a diagnostic or treatment tool and may not replace a private session with the appropriate doctor or specialist",
            "referance_arabic" : "الاطباء روبرت ال سبيتزر، جانيت بي دبليو وليامز، آيرت ارونك واخرون",
            "referance_english" : "Doctors Robert L Spitzer, Janet BW Williams, Aert Aronk and others",
            "image" : "therapeutic.jpeg",
        },
        {
            "id" : 2,
            "category_id" : 1,
            "title_arabic" : "الاحتراق الوظيفي",
            "title_english" : "Job burnout",
            "desc_arabic" : "",
            "desc_english" : "",
            "note_arabic" : "",
            "note_english" : "",
            "referance_arabic" : "",
            "referance_english" : "",
            "image" : "therapeutic.jpeg",
        },
        {
            "id" : 3,      
            "category_id" : 2,
            "title_arabic" : "الوسواس القهري",
            "title_english" : "Obsessive-compulsive disorder",
            "desc_arabic" : "",
            "desc_english" : "",
            "note_arabic" : "",
            "note_english" : "",
            "referance_arabic" : "",
            "referance_english" : "",
            "image" : "therapeutic.jpeg",
        },
        {
            "id" : 4,   
            "category_id" : 4,   
            "title_arabic" : "ادارة الغضب",
            "title_english" : "Anger management",
            "desc_arabic" : "",
            "desc_english" : "",
            "note_arabic" : "",
            "note_english" : "",
            "referance_arabic" : "",
            "referance_english" : "",
            "image" : "therapeutic.jpeg",
        },
    ]
    )

    op.bulk_insert(DB_TipsQuestions.__table__,
    [
        {
            "id" : 1,                  
            "tips_id" : 1,      
            "question_arabic" : "الشعور بقلة او فقدان الاهتمام او عدم الاستمتاع بالامور التي كنت تستمتع بها سابقا",
            "question_english" : "Feeling less or less interested in or not enjoying things you used to enjoy",
            "answer1_arabic" : "لا اشعر بذلك",
            "answer1_english" : "I don't feel it",
            "answer1_points" : 0,
            "answer2_arabic" : "اشعر بذلك بعض الايام",
            "answer2_english" : "I feel it some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "Half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 30,
        },
        {
            "id" : 2,                  
            "tips_id" : 1,      
            "question_arabic" : "الصعوبة في النوم او النوم اكثر من العادة",
            "question_english" : "Difficulty falling asleep or sleeping more than usual",
            "answer1_arabic" : "لا يوجد لدي مشكلة بذلك",
            "answer1_english" : "I don't have a problem with that",
            "answer1_points" : 0,
            "answer2_arabic" : "بعض الايام",
            "answer2_english" : "Some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 30,
        },
        {
            "id" : 3,                  
            "tips_id" : 1,      
            "question_arabic" : "الشعور بالتعب او الصعوبة بالقيام بالانشطة التي تتطلب جهد بدني",
            "question_english" : "Feeling tired or having difficulty doing activities that require physical effort",
            "answer1_arabic" : "لا يوجد لدي مشكلة بذلك",
            "answer1_english" : "I don't have a problem with that",
            "answer1_points" : 0,
            "answer2_arabic" : "بعض الايام",
            "answer2_english" : "Some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 30,
        },
        {
            "id" : 4,                  
            "tips_id" : 1,      
            "question_arabic" : "انخفاض الشهية او زيادة الرغبة بالاكل على غير المعتاد",
            "question_english" : "Decreased appetite or unusually increased desire to eat",
            "answer1_arabic" : "لا يوجد لدي مشكلة بذلك",
            "answer1_english" : "I don't have a problem with that",
            "answer1_points" : 0,
            "answer2_arabic" : "بعض الايام",
            "answer2_english" : "Some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 30,
        },
        {
            "id" : 5,                  
            "tips_id" : 1,      
            "question_arabic" : "الشعور بعدم الرضا عن النفس وجلد الذات او الشعور بالاحباط",
            "question_english" : "Feeling of self-dissatisfaction, self-flagellation, or feeling frustrated",
            "answer1_arabic" : "لا يوجد لدي مشكلة بذلك",
            "answer1_english" : "I don't have a problem with that",
            "answer1_points" : 0,
            "answer2_arabic" : "بعض الايام",
            "answer2_english" : "Some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 30,
        },
        {
            "id" : 6,                  
            "tips_id" : 1,      
            "question_arabic" : "الشعور بالانزعاج الحاد على الامور البسيطة",
            "question_english" : "Feeling very upset over simple things",
            "answer1_arabic" : "لا يوجد لدي مشكلة بذلك",
            "answer1_english" : "I don't have a problem with that",
            "answer1_points" : 0,
            "answer2_arabic" : "بعض الايام",
            "answer2_english" : "Some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 30,
        },
        {
            "id" : 7,                  
            "tips_id" : 1,      
            "question_arabic" : "بطء في الكلام او الحركة بدرجة ملحوظة من الاخرين",
            "question_english" : "Significantly slower speech or movement than others",
            "answer1_arabic" : "لا يوجد لدي مشكلة بذلك",
            "answer1_english" : "I don't have a problem with that",
            "answer1_points" : 0,
            "answer2_arabic" : "بعض الايام",
            "answer2_english" : "Some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 30,
        },
        {
            "id" : 8,                  
            "tips_id" : 1,      
            "question_arabic" : "تراودك افكار انتحارية او رغبة بإيذاء النفس",
            "question_english" : "You have suicidal thoughts or desire to harm yourself",
            "answer1_arabic" : "لا يوجد لدي مشكلة بذلك",
            "answer1_english" : "I don't have a problem with that",
            "answer1_points" : 0,
            "answer2_arabic" : "بعض الايام",
            "answer2_english" : "Some days",
            "answer2_points" : 10,
            "answer3_arabic" : "نصف الايام",
            "answer3_english" : "half days",
            "answer3_points" : 25,
            "answer4_arabic" : "دائما",
            "answer4_english" : "Always",
            "answer4_points" : 100,
        },
    ]
    )
    
    op.bulk_insert(DB_TipsUsersAnswer.__table__,
    [
        {
            "id" : 1,                  
            "question_id" : 1,      
            "client_owner_id" : 1,
            "question" : "test",
            "answer" : "test",
            "point" : 0,
        },
    ]
    )
    
    op.bulk_insert(DB_TipsResult.__table__,
    [
        {
            "id" : 1,                  
            "tips_id" : 1,      
            "point" : "low", 
            "title_arabic" : "لا يوجد اكتئاب",
            "title_english" : "No Depression",
            "desc_english" : "Your mental health calls for reassurance, we invite you to take care of increasing your mental health through a consultation from one of our specialists.",
            "desc_arabic" : "صحتك النفسية تدعو للاطمئنان، ندعوك للاهتمام بزيادة صحتك النفسية من خلال استشارة من احد المختصين لدينا",
        },
        {
            "id" : 2,                  
            "tips_id" : 1,      
            "point" : "mid", 
            "title_arabic" : "اكتئاب منخفض",
            "title_english" : "Low Depression",
            "desc_english" : "Your mental health calls for reassurance, we invite you to take care of increasing your mental health through a consultation from one of our specialists.",
            "desc_arabic" : "صحتك النفسية تدعو للاطمئنان، ندعوك للاهتمام بزيادة صحتك النفسية من خلال استشارة من احد المختصين لدينا",
        },
        {
            "id" : 3,                  
            "tips_id" : 1,      
            "point" : "high", 
            "title_arabic" : "اكتئاب مرتفع",
            "title_english" : "High Depression",
            "desc_english" : "We invite you to take care of your mental health and request a session from a specialist. Do not worry, you are not alone. We are here to help.",
            "desc_arabic" : "ندعوك للعناية بصحتك النفسية وطلب جلسة من احد المختصين، لا تقلق انت لست لوحدك نحن هنا للمساعدة",
        },
        {
            "id" : 4,                  
            "tips_id" : 1,      
            "point" : "very high", 
            "title_arabic" : "اكتئاب مرتفع جداً",
            "title_english" : "Very High Depression",
            "desc_english" : "We invite you to take care of your mental health and request a session from a specialist as soon as possible. Do not worry, you are not alone. We are here to help.",
            "desc_arabic" : "ندعوك للعناية بصحتك النفسية وطلب جلسة من احد المختصين باقرب وقت ممكن ، لا تقلق انت لست لوحدك نحن هنا للمساعدة",
        },
    ]
    )
    

    pass


def downgrade() -> None:
    pass
