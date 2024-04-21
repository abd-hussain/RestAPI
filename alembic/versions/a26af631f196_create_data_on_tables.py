"""create data on tables

Revision ID: a26af631f1969
Revises: 
Create Date: 2022-10-20 12:40:47.209451

"""
import datetime
from alembic import op

from app.models.database.attorney.db_attorney_review import DB_Attorney_Review
from app.models.database.attorney.db_attorney_points import DB_Attorney_Points
from app.models.database.attorney.db_attorney_user import DB_Attorney_Users, FreeCallTypes

from app.models.database.customer.db_customer_points import DB_Customer_Points
from app.models.database.customer.db_customer_user import DB_Customer_Users

from app.models.database.posts.db_posts import DB_Post
from app.models.database.posts.db_posts_comments import DB_Post_Comment
from app.models.database.posts.db_posts_reports import DB_Post_Report

from app.models.database.db_appointment import DB_Appointments, AppointmentsState, AppointmentsType, PaymentMethod
from app.models.database.db_banner import DB_Banners, UsersType
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.models.database.db_discount_type import DB_DiscountType
from app.models.database.db_notifications import DB_Notifications
from app.models.database.db_payments import DB_Attorney_Payments, PaymentStatus, DB_Attorney_PaymentsـReports
from app.models.database.db_suffix import DB_Suffix
from app.models.database.db_suggestion_reported import DB_Suggestion_Reported
from app.models.database.db_issue_reported import DB_Issues_Reported
from app.models.database.db_leads import DB_Leads

from app.utils.database import Base, engine

# revision identifiers, used by Alembic.
revision = 'a26af631f1969'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    op.bulk_insert(DB_DiscountType.__table__,
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
    
    op.bulk_insert(DB_Countries.__table__,
    [
        {
            "id" : 1,
            "flag_image" : "bahrain.png",
            "name_english" : "Bahrain",         
            "name_arabic" : "البحرين",   
            "currency_arabic" : "د.ب",
            "currency_english" : "BHD",   
            "country_code" : "BH",
            "currency_code" : "BHD",       
            "dialCode" : "00973",
            "minLength" : 8,
            "maxLength": 8,
            "dollar_equivalent" : 2.64
        },
        {          
            "id" : 2,
            "flag_image" : "egypt.png",
            "name_english" : "Eqypt",         
            "name_arabic" : "مصر",     
            "currency_arabic" : "ج.م",
            "currency_english" : "EGP",
            "country_code" : "EG",
            "currency_code" : "EGP",      
            "dialCode" : "0020",
            "minLength" : 10,
            "maxLength": 10,
            "dollar_equivalent" : 0.032
        }, 
        {
            "id" : 3,
            "flag_image" : "iraq.png",
            "name_english" : "Iraq",         
            "name_arabic" : "العراق",  
            "currency_arabic" : "د.ع",
            "currency_english" : "IQD",
            "country_code" : "IQ",
            "currency_code" : "IQD",         
            "dialCode" : "00964",
            "minLength" : 10,
            "maxLength": 10,
            "dollar_equivalent" : 0.00076
        }, 
        {
            "id" : 4,
            "flag_image" : "jordan.png",
            "name_english" : "Jordan",         
            "name_arabic" : "الاردن",         
            "currency_arabic" : "د.ا",   
            "currency_english" : "JOD",
            "country_code" : "JO",  
            "currency_code" : "JOD",          
            "dialCode" : "00962",
            "minLength" : 9,
            "maxLength": 9,
            "dollar_equivalent" : 1.41
        },
        { 
            "id" : 5,
            "flag_image" : "kuwait.png",
            "name_english" : "Kuwait",         
            "name_arabic" : "الكويت",         
            "currency_arabic" : "د.ك",
            "currency_english" : "KWD",
            "country_code" : "KW",
            "currency_code" : "KWD",          
            "dialCode" : "00965",
            "minLength" : 8,
            "maxLength": 8,
            "dollar_equivalent" : 3.24
        },
        {
            "id" : 6,
            "flag_image" : "qatar.png",
            "name_english" : "Qatar",         
            "name_arabic" : "قطر",         
            "currency_arabic" : "ر.ق",
            "currency_english" : "QAR",
            "country_code" : "QA",
            "currency_code" : "QAR",          
            "dialCode" : "00974",
            "minLength" : 8,
            "maxLength": 8,
            "dollar_equivalent" : 0.27
        }, 
        {
            "id" : 7,
            "flag_image" : "saudi.png",
            "name_english" : "Saudi Arabia",         
            "name_arabic" : "المملكة العربية السعودية",         
            "currency_arabic" : "ر.س",
            "currency_english" : "SAR",
            "country_code" : "SA",
            "currency_code" : "SAR",          
            "dialCode" : "00966",
            "minLength" : 9,
            "maxLength": 9,
            "dollar_equivalent" : 0.27
        }, 
        {
            "id" : 8,
            "flag_image" : "emirates.png",
            "name_english" : "United Arab Emirates",         
            "name_arabic" : "الإمارات العربيّة المتّحدة",         
            "currency_arabic" : "د.إ",
            "currency_english" : "AED",
            "country_code" : "AE",
            "currency_code" : "AED",         
            "dialCode" : "00971",
            "minLength" : 9,
            "maxLength": 9,
            "dollar_equivalent" : 0.27
        },
        {
            "id" : 9,
            "flag_image" : "lebanon.png",
            "name_english" : "Lebanon",         
            "name_arabic" : "لبنان",         
            "currency_arabic" : "دولار",
            "currency_english" : "USD",
            "country_code" : "US",
            "currency_code" : "USD",         
            "dialCode" : "00961",
            "minLength" : 8,
            "maxLength": 8,
            "dollar_equivalent" : 1.0
        },
        {
            "id" : 10,
            "flag_image" : "palestine.png",
            "name_english" : "Palestinian Territory, Occupied",         
            "name_arabic" : "فلسطين المحتلة",         
            "currency_arabic" : "شيكل",
            "currency_english" : "ILS",
            "country_code" : "IL",
            "currency_code" : "ILS",       
            "dialCode" : "00970",
            "minLength" : 9,
            "maxLength": 9,
            "dollar_equivalent" : 0.27
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
            "name_english" : "Family",         
            "name_arabic" : "عائلي",              
            "icon" : "family.png"
        },
         {
            "id" : 2,
            "name_english" : "Employment",         
            "name_arabic" : "توظيف",              
            "icon" : "employment.png"
        },
         {
            "id" : 3,
            "name_english" : "Criminal Defense",         
            "name_arabic" : "الجنائي",              
            "icon" : "criminal.png"
        },
         {
            "id" : 4,
            "name_english" : "Real Estate",         
            "name_arabic" : "العقارات",               
            "icon" : "estate.png"
        },
         {
            "id" : 5,
            "name_english" : "Business",         
            "name_arabic" : "اعمال",               
            "icon" : "business.png"
        },
         {
            "id" : 6,
            "name_english" : "Immigration",         
            "name_arabic" : "هجره",           
            "icon" : "immigration.png"
        },
         {
            "id" : 7,
            "name_english" : "Personal Injury",         
            "name_arabic" : "إصابة شخصية",              
            "icon" : "injury.png"
        },
         {
            "id" : 8,
            "name_english" : "Wills, Trusts & Estates",         
            "name_arabic" : "الوصايا والصناديق الاستئمانية والعقارات",              
            "icon" : "wills.png"
        },
         {
            "id" : 9,
            "name_english" : "Bankruptcy & Finances",         
            "name_arabic" : "الإفلاس والمالية",              
            "icon" : "bankruptcy.png"
        },
         {
            "id" : 10,
            "name_english" : "Government",         
            "name_arabic" : "حكومة",              
            "icon" : "government.png"
        },
         {
            "id" : 11,
            "name_english" : "Products & Services",         
            "name_arabic" : "المنتجات والخدمات",              
            "icon" : "products.png"
        },
         {
            "id" : 12,
            "name_english" : "Intellectual Property",         
            "name_arabic" : "الملكية الفكرية",              
            "icon" : "intellectual.png"
        },
         {
            "id" : 13,
            "name_english" : "Insurance Law",         
            "name_arabic" : "قانون التأمين",              
            "icon" : "insurance.png"
        }
    ]
    )
    
    op.bulk_insert(DB_Banners.__table__,
    [
        {
            "id" : 1,      
            "language" : "en",
            "image" : "banner1.png",
            "published" : True,
            "targeted" : UsersType.attorney  
        },
        {
            "id" : 2,      
            "language" : "en",
            "image" : "banner2.jpg",
            "action_type" : "https://www.youtube.com/watch?v=FrCO41i2tWM&ab_channel=%D8%AD%D8%B3%D9%86%D8%A7%D9%84%D9%81%D8%A7%D8%B6%D9%84%D9%8A-ElfadiliTV",
            "published" : True,
            "targeted" : UsersType.attorney   
        },
        {
            "id" : 3,      
            "language" : "ar",
            "image" : "banner3.jpg",
            "published" : True,
            "targeted" : UsersType.attorney          
        },
        {
            "id" : 4,      
            "language" : "ar",
            "image" : "banner4.png",
            "published" : True,
            "targeted" : UsersType.attorney        
        },
        {
            "id" : 5,      
            "language" : "ar",
            "image" : "banner5.png",
            "published" : False,
            "targeted" : UsersType.attorney         
        },
        {
            "id" : 6,      
            "language" : "en",
            "image" : "banner6.png",
            "published" : False,
            "targeted" : UsersType.attorney        
        },
        {
            "id" : 7,      
            "language" : "en",
            "image" : "banner1.png",
            "published" : True,
            "targeted" : UsersType.customer       
        },
        {
            "id" : 8,      
            "language" : "en",
            "image" : "banner2.jpg",
            "action_type" : "https://www.youtube.com/watch?v=FrCO41i2tWM&ab_channel=%D8%AD%D8%B3%D9%86%D8%A7%D9%84%D9%81%D8%A7%D8%B6%D9%84%D9%8A-ElfadiliTV",
            "published" : True,
            "targeted" : UsersType.customer        
        },
        {
            "id" : 9,      
            "language" : "ar",
            "image" : "banner3.jpg",
            "published" : True,
            "targeted" : UsersType.customer         
        },
        {
            "id" : 10,      
            "language" : "ar",
            "image" : "banner4.png",
            "published" : True,
            "targeted" : UsersType.customer        
        },
        {
            "id" : 11,      
            "language" : "ar",
            "image" : "banner5.png",
            "published" : False,
            "targeted" : UsersType.customer       
        },
        {
            "id" : 12,      
            "language" : "en",
            "image" : "banner6.png",
            "published" : False,
            "targeted" : UsersType.customer       
        },
    ]
    )
    
    op.bulk_insert(DB_Customer_Users.__table__,
    [
        {
            "id" : 1,
            "first_name" : "abed alrahman",
            "last_name" : "al haj hussain",         
            "mobile_number" : "00962790000001",        
            "email" : "cus1@gmail.com",
            "password" : "123",          
            "gender" : 1,  
            "allow_notifications" : True,
            "blocked" : False,
            "invitation_code" : "123456",
            "profile_img" : "1.png",
            "app_version" : "1.0",
            "date_of_birth" : "1992/05/22",             
            "push_token" : "",         
            "country_id" : 4,
            "api_key" : "00101",
            "points" : 0
        },
        {
            "id" : 2,
            "first_name" : "mohammed",
            "last_name" : "maswadeh",         
            "mobile_number" : "00962790000002",        
            "email" : "cus2@gmail.com",    
            "password" : "123",       
            "gender" : 2,              
            "allow_notifications" : True,         
            "blocked" : True,         
            "invitation_code" : "234567",
            "profile_img" : "2.png",       
            "app_version" : "1.0",         
            "date_of_birth" : "1992/05/22",  
            "push_token" : "",
            "country_id" : 2,          
            "api_key" : "00102",
            "points" : 0
        }
    ]
    )
    
    op.bulk_insert(DB_Attorney_Users.__table__,
    [
        {
            "id" : 1,
            "category_id" : 1,
            "suffixe_name" : "Sr.",
            "first_name" : "abed alrahman 1",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "hour_rate" : 20.5,
            "iban" : "ibaaan number 1",
            "mobile_number" : "00962790000010",
            "password" : "079",
            "email" : "att1@gmail.com",
            "gender" : 1,
            "blocked" : False,
            "published" : True, 
            "free_call" : FreeCallTypes.free_15_min,
            "invitation_code" : "123",
            "profile_img" : "1.jpeg",
            "id_img" : "1.png",
            "cv" : "1.pdf",
            "cert1" : "1.pdf",
            "cert2" : "2.pdf",
            "cert3" : "3.pdf",
            "app_version" : "1.0",
            "date_of_birth" : "22/05/1992",
            "experience_since" : "1992",
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 0],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "api_key" : "00001",
            "push_token" : "",    
            "country_id" : 6
        },
        {
            "id" : 2,
            "category_id" : 1,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 2",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",          
            "speaking_language" : ["English", "العربية"],
            "hour_rate" : 8.0,
            "iban" : "ibaaan number 2", 
            "mobile_number" : "00962790000020",
            "password" : "123",        
            "email" : "att2@gmail.com",
            "gender" : 2,
            "blocked" : False,
            "published" : True,
            "free_call" : FreeCallTypes.free_disabled,
            "invitation_code" : "234",
            "profile_img" : "2.jpeg",
            "id_img" : "1.png",
            "cv" : "1.pdf",
            "cert1" : "1.pdf",
            "cert2" : "2.pdf",
            "cert3" : "3.pdf",
            "app_version" : "1.0", 
            "date_of_birth" : "22/05/1992",   
            "experience_since" : "1999", 
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "api_key" : "00002",
            "push_token" : "",         
            "country_id" : 2
        },        
        {
            "id" : 3,
            "category_id" : 3,
            "suffixe_name" : "Dr.",
            "first_name" : "abed alrahman 3",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"], 
            "hour_rate" : 12.1,
            "iban" : "ibaaan number 3",  
            "mobile_number" : "00962790000030",
            "password" : "123",        
            "email" : "att3@gmail.com",
            "gender" : 0,
            "blocked" : False,
            "published" : True,
            "free_call" : FreeCallTypes.free_disabled,
            "invitation_code" : "345",
            "profile_img" : "",
            "id_img" : "1.png",
            "cv" : "1.pdf",
            "cert1" : "1.pdf",
            "cert2" : "2.pdf",
            "cert3" : "3.pdf",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2000",    
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],
            "api_key" : "00003", 
            "push_token" : "",        
            "country_id" : 7 
        },
        {
            "id" : 4,
            "category_id" : 4,
            "suffixe_name" : "Mr.",
            "first_name" : "abed alrahman 4",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "hour_rate" : 65.0,
            "iban" : "ibaaan number 4",
            "mobile_number" : "00962790000040",
            "password" : "123",             
            "email" : "att4@gmail.com",
            "gender" : 0,
            "blocked" : False,
            "published" : True,
            "free_call" : FreeCallTypes.free_15_min_with_promocode,
            "invitation_code" : "456",
            "profile_img" : "",
            "id_img" : "1.png",
            "cv" : "1.pdf",
            "cert1" : "1.pdf",
            "cert2" : "2.pdf",
            "cert3" : "3.pdf",
            "app_version" : "1.0",         
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2014", 
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],                    
            "api_key" : "00004",
            "push_token" : "",         
            "country_id" : 6
        },
        {
            "id" : 5,
            "category_id" : 5,
            "suffixe_name" : "Mrs.",
            "first_name" : "abed alrahman 5",
            "last_name" : "al haj hussain",
            "bio" : "استشاري الأسرة و الصحة النفسية و علاج الإدمان حاصل على ٦ زمالات السعودية و العربية و الاستراليه و الامريكيه جامعتي هارفورد و كاليفورنيا اريفاين والاسترالية الطبيب الاردني الوحيد الحاصل على زمالة الصحة النفسية الاولية و رئيس برنامج زمالة الصحة النفسيه الاردنية",
            "speaking_language" : ["English", "العربية"],
            "hour_rate" : 33.0,
            "iban" : "ibaaan number 5",
            "mobile_number" : "00962790000050",
            "password" : "123",                
            "email" : "att5@gmail.com",
            "gender" : 0,
            "blocked" : False,
            "published" : True,
            "free_call" : FreeCallTypes.free_15_min_with_promocode,
            "invitation_code" : "567",
            "profile_img" : "",
            "id_img" : "1.png",
            "cv" : "1.pdf",
            "cert1" : "1.pdf",
            "cert2" : "2.pdf",
            "cert3" : "3.pdf",
            "app_version" : "1.0",
            "date_of_birth" : "22/05/1992",
            "experience_since" : "2014",
            "working_hours_saturday" : [1, 2, 3, 4, 6, 7],
            "working_hours_sunday" : [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "working_hours_monday" : [4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
            "working_hours_tuesday" : [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22],
            "working_hours_wednesday" : [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23],
            "working_hours_thursday" : [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0],
            "working_hours_friday" : [8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 0],                               
            "api_key" : "00005",
            "push_token" : "",         
            "country_id" : 1
        }
    ]
    )
    
    op.bulk_insert(DB_Attorney_Review.__table__,
    [
        {
            "id" : 1,
            "attorney_id" : 2,
            "customers_id" : 1,
            "stars" : 3.7,
            "comment" : "comment 1",
            "attorney_response" : "respond one"
        },
        {
            "id" : 2,
            "attorney_id" : 1,
            "customers_id" : 2,
            "stars" : 1.7,
            "comment" : "comment 2",
            "attorney_response" : ""
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
            "customers_owner_id" : 1,
            "attorney_owner_id" : None,
        },
        {
            "id" : 2,
            "title_english" : "notification title 2",
            "title_arabic" : "تنبيه رقم ٢",         
            "content_english" : "notification content 2",
            "content_arabic" : "محتوى التنبيه ٢",          
            "customers_owner_id" : 1,
            "attorney_owner_id" : None,
        },
        {
            "id" : 3,
            "title_english" : "notification title 3",
            "title_arabic" : "تنبيه رقم 3",         
            "content_english" : "notification content 3",
            "content_arabic" : "محتوى التنبيه 3",    
            "customers_owner_id" : None,      
            "attorney_owner_id" : 1,
        },
        {
            "id" : 4,
            "title_english" : "notification title 4",
            "title_arabic" : "تنبيه رقم 4",         
            "content_english" : "notification content 4",
            "content_arabic" : "محتوى التنبيه 4",    
            "customers_owner_id" : None,      
            "attorney_owner_id" : 1,
        }          
    ]
    )
    
    op.bulk_insert(DB_Post.__table__,
    [
        {
            "id" : 1,
            "customers_owner_id" : 1,
            "category_id" : 1,
            "content" : "content post 1"
        },
        {
            "id" : 2,
            "customers_owner_id" : 2,
            "category_id" : 2,
            "content" : "content post 2"
        },
        {
            "id" : 3,
            "customers_owner_id" : 1,
            "category_id" : 3,
            "content" : "content post 3"
        },
        {
            "id" : 4,
            "customers_owner_id" : 2,
            "category_id" : 4,
            "content" : "content post 4"
        }          
    ]
    )
    
    op.bulk_insert(DB_Appointments.__table__,
    [
        {
            "id" : 1,
            "attorney_id" : 1,
            "customers_id" : 1,
            "appointment_type" : AppointmentsType.schudule,
            "date_from" : datetime.datetime(2024, 4, 20, 8),
            "date_to" : datetime.datetime(2024, 4, 20, 9),
            "state" : AppointmentsState.completed,
            "discount_id" : None,
            "is_free" : False,
            "price" : 20,
            "total_price" : 20,
            "payment_type" : PaymentMethod.apple,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 20,
            "note_from_customers" : "example customers note",
            "note_from_attorney" : "example attorney note",
            "attorney_join_call" : datetime.datetime(2024, 1, 25, 8),
            "customers_join_call" : datetime.datetime(2024, 1, 25, 8),
            "attorney_date_of_close" : datetime.datetime(2024, 1, 25, 9),
            "customers_date_of_close" : datetime.datetime(2024, 1, 25, 9),
            "channel_id" : "test1"
        },
        {
            "id" : 2,
            "attorney_id" : 3,            
            "customers_id" : 2,
            "appointment_type" : AppointmentsType.instant,
            "date_from" : datetime.datetime(2024, 4, 5, 14),    
            "date_to" : datetime.datetime(2024, 4, 5, 14, 15),
            "state" : AppointmentsState.active,
            "discount_id" : None,
            "is_free" : True,
            "price" : 0,
            "total_price" : 0,
            "payment_type" : PaymentMethod.free,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 20,
            "note_from_customers" : "this is customers note",
            "note_from_attorney" : None,
            "attorney_join_call" : None,
            "customers_join_call" : None,
            "attorney_date_of_close" : None,
            "customers_date_of_close" : None,
              "channel_id" : "test2"
        },
        {
            "id" : 3,
            "attorney_id" : 4,
            "customers_id" : 1,
            "appointment_type" : AppointmentsType.instant,
            "date_from" : datetime.datetime(2024, 4, 6, 10),    
            "date_to" : datetime.datetime(2024, 4, 6, 10, 15),
            "state" : AppointmentsState.active,
            "discount_id" : None,
            "is_free" : True,
            "price" : 0,
            "total_price" : 0,
            "payment_type" : PaymentMethod.free,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 20,
            "note_from_customers" : None,
            "note_from_attorney" : "this is attorney note",
            "attorney_join_call" : None,
            "customers_join_call" : None,
            "attorney_date_of_close" : None,
            "customers_date_of_close" : None,
            "channel_id" : "test3"
        },
        {
            "id" : 4,
            "attorney_id" : 5,
            "customers_id" : 1,
            "appointment_type" : AppointmentsType.instant,
            "date_from" : datetime.datetime(2024, 1, 1, 0),    
            "date_to" : datetime.datetime(2024, 1, 1, 0, 30),
            "state" : AppointmentsState.completed,
            "discount_id" : 1,
            "is_free" : False,
            "price" : 20,
            "total_price" : 10,
            "payment_type" : PaymentMethod.paypal,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 20,
            "note_from_customers" : None,
            "note_from_attorney" : "this is attorney note",
            "attorney_join_call" : datetime.datetime(2024, 1, 1, 0),
            "customers_join_call" : datetime.datetime(2024, 1, 1, 0),
            "attorney_date_of_close" : datetime.datetime(2024, 1, 1, 0, 30),
            "customers_date_of_close" : datetime.datetime(2024, 1, 1, 0, 30),
            "channel_id" : "test4"
        },
        {
            "id" : 5,
            "attorney_id" : 2,
            "customers_id" : 1,
            "appointment_type" : AppointmentsType.instant,
            "date_from" : datetime.datetime(2024, 4, 18, 10),    
            "date_to" : datetime.datetime(2024, 4, 18, 10, 15),
            "state" : AppointmentsState.attorney_cancel,
            "discount_id" : 2,
            "is_free" : False,
            "price" : 20,
            "total_price" : 10,
            "payment_type" : PaymentMethod.google,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 20,
            "note_from_customers" : None,
            "note_from_attorney" : None,
            "attorney_join_call" : None,
            "customers_join_call" : None,
            "attorney_date_of_close" : None,
            "customers_date_of_close" : None,
            "channel_id" : "test5"
        },
        {
            "id" : 6,
            "attorney_id" : 2,
            "customers_id" : 2,
            "appointment_type" : AppointmentsType.schudule,
            "date_from" : datetime.datetime(2024, 4, 17, 19),    
            "date_to" : datetime.datetime(2024, 4, 17, 19, 30),
            "state" : AppointmentsState.customers_cancel,
            "discount_id" : None,
            "is_free" : False,
            "price" : 20,
            "total_price" : 20,
            "payment_type" : PaymentMethod.apple,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 20,
            "note_from_customers" : None,
            "note_from_attorney" : None,
            "attorney_join_call" : None,
            "customers_join_call" : None,
            "attorney_date_of_close" : None,
            "customers_date_of_close" : None,
            "channel_id" : "test6"
        },
        {
            "id" : 7,
            "attorney_id" : 1,
            "customers_id" : 1,
            "appointment_type" : AppointmentsType.schudule,
            "date_from" : datetime.datetime(2024, 4, 30, 20),    
            "date_to" : datetime.datetime(2024, 4, 30, 21),
            "state" : AppointmentsState.active,
            "discount_id" : None,
            "is_free" : False,
            "price" : 20,
            "total_price" : 20,
            "payment_type" : PaymentMethod.paypal,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 20,
            "note_from_customers" : None,
            "note_from_attorney" : None,
            "attorney_join_call" : None,
            "customers_join_call" : None,
            "attorney_date_of_close" : None,
            "customers_date_of_close" : None,
            "channel_id" : "test7"
        },
        {
            "id" : 8,
            "attorney_id" : 4,
            "customers_id" : 1,
            "appointment_type" : AppointmentsType.instant,
            "date_from" : datetime.datetime(2024, 4, 7, 21),    
            "date_to" : datetime.datetime(2024, 4, 7, 22),
            "state" : AppointmentsState.active,
            "discount_id" : 2,
            "is_free" : False,
            "price" : 20,
            "total_price" : 10,
            "payment_type" : PaymentMethod.google,
            "currency_english" : "JD",
            "currency_arabic" : "د.ا",
            "attorney_hour_rate" : 40,
            "note_from_customers" : None,
            "note_from_attorney" : "this is attorney note",
            "attorney_join_call" : None,
            "customers_join_call" : None,
            "attorney_date_of_close" : None,
            "customers_date_of_close" : None,
            "channel_id" : "test8"
        }
    ]
    )

    op.bulk_insert(DB_Attorney_Payments.__table__,
    [
        {
            "id" : 1,
            "attorney_id" : 1,
            "appointment_id" : 1,
            "status" : PaymentStatus.pending  
        },
        {
            "id" : 2,
            "attorney_id" : 2,
            "appointment_id" : 4,
            "status" : PaymentStatus.sended
        }
    ]
    )
    
    op.bulk_insert(DB_Attorney_PaymentsـReports.__table__,
    [
        {
            "id" : 1,
            "attorney_id" : 1,
            "payment_id" : 1,   
            "message" : "There is Something wrong",                                                                                      
        }    
    ]
    )

    pass


def downgrade() -> None:
    pass
