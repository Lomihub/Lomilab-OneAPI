from pydantic import BaseModel
from typing import List

class Token(BaseModel):
    Id: int
    UserID: int
    NameToken: str
    Status: bool
    Key: str
    TokenType: str
    CreatedAt: str
    AccessedTime: str
    ExpiredTime: str
    RemainQuota: int
    LimitedQuota: int
    QuotaResetTime: str
    Models: List[str]
    Subnet: str

    
    
    

