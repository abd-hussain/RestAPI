from sqlalchemy.orm import Session

# //TODO

def add_archive_to_client(file, file_type, client_id, db):
    if not file:
        return