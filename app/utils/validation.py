from fastapi import Request, HTTPException, status
from app.models.schemas.header import HeaderRequest, PreLoginHeaderRequest
from app.utils.generate import generateRequestId

def verifyKey(passsed_key, original_key):
    return passsed_key == original_key

def validateLanguageHeader(request: Request):
    if ((request.headers.get('language') != None)):
        return PreLoginHeaderRequest(language=request.headers.get('language'))
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail={
        "message": f"header missing some data", "request_id": generateRequestId()})