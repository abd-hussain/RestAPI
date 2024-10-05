from fastapi import Request, Depends ,APIRouter, status
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validate_headers
from app.models.database.quran_kareem.db_mus7af import DB_Mus7af
import json

router = APIRouter(
    prefix="/quran",
    tags=["Quran_Kareem"]
)

@router.get("/copies", status_code=status.HTTP_200_OK)
async def get_all_copies_avaliable(request: Request, 
                       db: Session = Depends(get_db)):
    
    validate_headers(request)
    data = db.query(DB_Mus7af.id, DB_Mus7af.previewImage, 
                    DB_Mus7af.description,
                    DB_Mus7af.addedPagesAttachmentLocation,
                    DB_Mus7af.name_referance, DB_Mus7af.language,
                    DB_Mus7af.attachmentLocation).filter(DB_Mus7af.published == True
                    ).all()
    return generalResponse(message= "List of quran copies returned successfully", data = data)

@router.get("/settings", status_code=status.HTTP_200_OK)
async def get_all_copies_avaliable(request: Request,
                        copy_id: str,
                        db: Session = Depends(get_db)):
    
    validate_headers(request)
    data = db.query(DB_Mus7af.juz2ToPageNumbers, 
                    DB_Mus7af.sorahToPageNumbers,
                    ).filter(DB_Mus7af.published.is_(True)
                    ).filter(DB_Mus7af.id == copy_id
                    ).first()
                    
       # Convert the string fields to JSON
    if data:
        data = {
            "juz2ToPageNumbers": json.loads(data.juz2ToPageNumbers),
            "sorahToPageNumbers": json.loads(data.sorahToPageNumbers)
        }
    return generalResponse(message= "List of quran copies returned successfully", data = data)

