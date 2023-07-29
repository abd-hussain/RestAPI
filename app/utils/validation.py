from fastapi import Request, HTTPException, status
from app.models.schemas.header import PreLoginHeaderRequest

def verifyKey(passsed_key, original_key):
    return passsed_key == original_key

def validateLanguageHeader(request: Request):
    if ((request.headers.get('lang') != None)):
        return PreLoginHeaderRequest(language=request.headers.get('lang'))
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="header missing some data")