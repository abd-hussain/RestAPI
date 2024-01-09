from fastapi import HTTPException, status
from app.utils.validation import validateFileType, validateImageType


def handle_file_upload(file, file_type, last_id, payload):
    if file_type in ['profile_img', 'id_img']:
        extension = validateImageType(file, file_type)
    else:
        extension = validateFileType(file, file_type)
    file_locations = {
        'profile_img': f"static/mentorsImg/{last_id}{extension}",
        'id_img': f"static/mentorsIDs/{last_id}{extension}",
        'cv': f"static/mentorsCVs/{last_id}{extension}",
        'cert1': f"static/mentorsCerts/{last_id}-cer1{extension}",
        'cert2': f"static/mentorsCerts/{last_id}-cer2{extension}",
        'cert3': f"static/mentorsCerts/{last_id}-cer3{extension}"
    }
    
    file_location = file_locations[file_type]
    
    try:
        contents = file.file.read()
        with open(file_location, 'wb+') as out_file:
            out_file.write(contents)
            setattr(payload, file_type, f"{last_id}{extension}")
    except Exception:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Error in uploading {file_type}")
    finally:
        file.file.close()
        
        
def edit_file_uploaded(file, file_type, last_id) -> str:
    if file_type in ['profile_img', 'id_img']:
        extension = validateImageType(file, file_type)
    else:
        extension = validateFileType(file, file_type)
        
    file_locations = {
        'profile_img': f"static/mentorsImg/{last_id}{extension}",
        'id_img': f"static/mentorsIDs/{last_id}{extension}",
        'cv': f"static/mentorsCVs/{last_id}{extension}",
        'cert1': f"static/mentorsCerts/{last_id}-cer1{extension}",
        'cert2': f"static/mentorsCerts/{last_id}-cer2{extension}",
        'cert3': f"static/mentorsCerts/{last_id}-cer3{extension}"
    }
    
    file_location = file_locations[file_type]
    try:
        contents = file.file.read()
        with open(file_location, 'wb+') as out_file:
            out_file.write(contents)
            return(f"{last_id}{extension}")
    except Exception:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Error in uploading {file_type}")
    finally:
        file.file.close()