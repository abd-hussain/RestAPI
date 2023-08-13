from fastapi import Form, Request, HTTPException, status
from app.models.schemas.header import PreLoginHeaderRequest

def verifyKey(passsed_key, original_key):
    return passsed_key == original_key

def validateLanguageHeader(request: Request):
    if ((request.headers.get('lang') != None)):
        return PreLoginHeaderRequest(language=request.headers.get('lang'))
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="header missing some data")


def validateImageType(image: Form(None), imageName: str) -> Form(None):
    if image.content_type not in ["image/jpeg", "image/png", "image/jpg", "image/JPG", "application/octet-stream"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= imageName + " Format is not valid")
    else:
        return image