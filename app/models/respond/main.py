from pydantic import BaseModel

class Main(BaseModel):
    class Config:
        orm_mode = True       