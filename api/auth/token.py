from datetime import datetime
from typing import List, Optional


class Token():
    Id: int
    UserId: int
    NameToken: str
    Key: str
    Status: bool
    CreatedAt: Optional[datetime] = None
    AccessedTime: Optional[datetime] = None
    ExpiredTime: Optional[datetime] = None
    
    def __init__(
        self,
        Id: int,
        UserId: int,
        NameToken: str,
        Key: str,
        Status: bool = True,
        CreatedAt: Optional[datetime] = None,
        AccessedTime: Optional[datetime] = None,
        ExpiredTime: Optional[datetime] = None,
    ) -> None:
        self.Id = Id
        self.UserId = UserId
        self.NameToken = NameToken
        self.Key = Key
        self.Status = Status
        self.CreatedAt = CreatedAt
        self.AccessedTime = AccessedTime
        self.ExpiredTime = ExpiredTime


    def __str__(self) -> str:
        return f"Token(
            Id={self.Id}, 
            UserId={self.UserId}, 
            NameToken={self.NameToken}, 
            Key={self.Key}, 
            Status={self.Status}, 
            CreatedAt={self.CreatedAt}, 
            AccessedTime={self.AccessedTime}, 
            ExpiredTime={self.ExpiredTime}
            )"
     

def get_all_tokens() -> List[Token]:
    pass

def get_user_token(user_id: int) -> Token:
    pass

def get_token_by_key(key: str) -> Token:
    pass

def get_token_by_ids(name_token: str) -> Token:
    pass

def validate_user_token(user_id: int, key: str) -> bool:
    pass

# CRUD
def create_token(token: Token) -> Token:
    pass

def update_token(token: Token) -> Token:
    pass

def delete_token(token_id: int) -> None:
    pass

def count_user_tokens(user_id: int) -> int:
    pass

def invalidate_all_tokens(user_id: int) -> None:
    pass

def update_token_accessed_time(token_id: int) -> None:
    pass