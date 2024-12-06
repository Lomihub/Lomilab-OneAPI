from datetime import datetime
from typing import List, Literal, Optional
    
class Token():
    Id: int
    UserID: int
    NameToken: str
    Status: bool
    Key: str
    TokenType: Literal["admin", "user"] = "user"
    CreatedAt: Optional[datetime] = None
    AccessedTime: Optional[datetime] = None
    ExpiredTime: Optional[datetime] = None
    RemainQuota: Optional[datetime] = None
    LimitedQuota: int
    QuotaResetTime: Optional[datetime] = None
    Models: List[str]
    Subnet: str
    
    def __init__(
        self,
        Id: int,
        UserID: int,
        NameToken: str,
        Status: bool,
        Key: str,
        TokenType: Literal["admin", "user"] = "user",
        CreatedAt: Optional[datetime] = None,
        AccessedTime: Optional[datetime] = None,
        ExpiredTime: Optional[datetime] = None,
        RemainQuota: Optional[datetime] = None,
        LimitedQuota: int = 10,
        QuotaResetTime: Optional[datetime] = None,
        Models: List[str] = [],
        Subnet: str = ""
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
        
    def __str__(self) -> str:
        return f"Token(
            Id={self.Id}, 
            UserID={self.UserID}, 
            NameToken={self.NameToken}, 
            Status={self.Status}, 
            Key={self.Key}, 
            TokenType={self.TokenType}, 
            CreatedAt={self.CreatedAt}, 
            AccessedTime={self.AccessedTime}, 
            ExpiredTime={self.ExpiredTime}, 
            RemainQuota={self.RemainQuota}, 
            LimitedQuota={self.LimitedQuota}, 
            QuotaResetTime={self.QuotaResetTime}, 
            Models={self.Models}, 
            Subnet={self.Subnet}
        )"