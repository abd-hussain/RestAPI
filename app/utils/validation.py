from fastapi import Form, Request, HTTPException, status
from app.models.schemas.header import headerRequest, languageHeaderRequest

def verifyKey(passsed_key, original_key):
    return passsed_key == original_key

def validateLanguageHeader(request: Request):
    if ((request.headers.get('lang') != None)):
        return languageHeaderRequest(language=request.headers.get('lang'))
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="header missing lang")

def validate_headers(request: Request):
    # Validate 'lang' header
    lang_header = request.headers.get('lang')
    if lang_header is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="header missing lang")

    # Validate 'api_key' header
    api_key_header = request.headers.get('api_key')
    if api_key_header is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="header missing api_key")
    
    # Return both headers in a headerRequest object (or adjust as needed)
    return headerRequest(language=lang_header, api_key=api_key_header)

def validateImageType(image: Form, imageName: str) -> str :
    if image.content_type not in ["image/jpeg", "image/png", "image/jpg", "image/JPG", "application/octet-stream"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= imageName + " Format is not valid ==>" + image.content_type)
    else:
        validateFileSize(image)
        imageExtension = '.png'
        if (image.filename.endswith('.jpg')):
            imageExtension = '.jpg'
        if (image.filename.endswith('.JPG')):
            imageExtension = '.JPG'
        if (image.filename.endswith('.jpeg')):
            imageExtension = '.jpeg'
        return imageExtension
        
        
def validateFileType(file: Form, fileName: str) -> str:
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document","application/pdf", "application/octet-stream"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= fileName + " Format is not valid ==>" + file.content_type)
    else:
        validateFileSize(file)
        fileExtension = '.docx'
        if (file.filename.endswith('.pdf')):
            fileExtension = '.pdf'
        return fileExtension
    
def validateFileSize(file: Form):
    file_size = file.file.tell()
    if file_size > 2 * 1024 * 1024:
        # more than 2 MB
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="File too large")