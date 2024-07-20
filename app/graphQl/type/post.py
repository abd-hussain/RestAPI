import strawberry
from typing import Optional

@strawberry.type
class Post:
    id: int
    content: str
    postImg: Optional[str]
    reportCount: Optional[int]
    customersOwnerId: Optional[int]
    categoryId: int
    createdAt: str
    customerFirstName: str
    customerLastName: str
    customerProfilePic: Optional[str]
    customerFlag: str
    commentCount: str



