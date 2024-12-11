from datetime import datetime
from typing import List, Optional
from .base import Base
from sqlalchemy import Column, DateTime, Integer, String, Boolean, BigInteger, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Token(Base):
    __tablename__ = 'Token'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey('User.Id'), nullable=False)
    Nam1eToken = Column(String(255), nullable=False)
    Key = Column(String(48), nullable=False)
    Status = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=datetime.now())
    AccessedTime = Column(DateTime, default=datetime.now())
    ExpiredTime = Column(DateTime, nullable=True)
    Models = Column(Text, nullable=True)

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