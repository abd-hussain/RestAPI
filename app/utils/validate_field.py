from fastapi import HTTPException, status


def validateField(field) -> any:
    if field is not None:
        return field
    else :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Field '{field}' missing")