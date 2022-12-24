"""create data on tables

Revision ID: a26af631f1969
Revises: 
Create Date: 2022-10-20 12:40:47.209451

"""
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
            "percent_value" : 50,         
        },
        {
            "id" : 3,
            "code" : "abdo10",
            "percent_value" : 50,         
        },
        {
            "id" : 4,
            "code" : "abdo90",
            "percent_value" : 50,         
        },
        {
            "id" : 5,
            "code" : "abd100",
            "percent_value" : 50,         
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
            "class_min" : 30,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
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
            "class_min" : 45,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
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
            "class_min" : 45,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
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
            "class_min" : 30,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            "mobile_number" : "00962790000004",        
            "email" : "aboud.masoud.4@gmail.com",
            "category_id" : 4,  
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
            "class_min" : 15,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
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
            "class_min" : 15,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
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
            "class_min" : 15,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
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
            "class_min" : 45,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
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
            "class_min" : 60,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
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
            "class_min" : 60,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
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
            "class_min" : 30,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
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
            "class_min" : 50,                                                                                                                                                                                                                                                                                                                                                           
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
            "class_min" : 50,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
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
            "class_min" : 50,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
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
            "class_min" : 50,                                                                                                                                                                                                                                                                                                                                                                    
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
