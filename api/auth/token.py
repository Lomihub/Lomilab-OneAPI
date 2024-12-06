from pydantic import BaseModel
from typing import List, Literal

TOKEN_TYPE = Literal["admin", "user"]
    
class Token():
    Id: int
    UserID: int
    NameToken: str
    Status: bool
    Key: str
    TokenType: TOKEN_TYPE
    CreatedAt: str
    AccessedTime: str
    ExpiredTime: str
    RemainQuota: int
    LimitedQuota: int
    QuotaResetTime: str
    Models: List[str]
    Subnet: str
    
    def __init__(
        self,
        Id: int,
        UserID: int,
        NameToken: str,
        Status: bool,
        Key: str,
        TokenType: TOKEN_TYPE,
        CreatedAt: str,
        AccessedTime: str,
        ExpiredTime: str,
        RemainQuota: int,
        LimitedQuota: int,
        QuotaResetTime: str,
        Models: List[str],
        Subnet: str
    ) -> None:
        self.Id = Id
        self.UserID = UserID
        self.NameToken = NameToken
        self.Status = Status
        self.Key = Key
        self.TokenType = TokenType
        self.CreatedAt = CreatedAt
        self.AccessedTime = AccessedTime
        self.ExpiredTime = ExpiredTime
        self.RemainQuota = RemainQuota
        self.LimitedQuota = LimitedQuota
        self.QuotaResetTime = QuotaResetTime
        self.Models = Models
        self.Subnet = Subnet