from typing import List, Optional
from pydantic import BaseModel


class ReferalCode(BaseModel):
    code: str