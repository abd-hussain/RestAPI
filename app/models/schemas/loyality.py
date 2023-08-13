from typing import List, Optional
from pydantic import BaseModel

class Loyality(BaseModel):
    request_title: str
    number_of_point_requested: int
 



