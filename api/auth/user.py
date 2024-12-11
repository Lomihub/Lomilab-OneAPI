from datetime import datetime
from typing import List, Optional, Literal, Union
from .base import Base
from ..connection.database import session
from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime
class User(Base):
    __tablename__ = 'User'
    
    Id= Column(Integer, primary_key=True, autoincrement=True)            
    BindID = Column(String(48), nullable=False, unique=True)         
    Username = Column(String(12), unique=True, index=True, nullable=False)
    Password = Column(String(48), nullable=False)
    DisplayName = Column(String(48), nullable=False, index=True)
    AccessToken: str = Column(String(48), nullable=False, unique=True)
    Status = Column(Boolean, default=True)
    Blacklist = Column(Boolean, default=False)
    Role = Column(Enum('admin', 'user'), default='user')
    GoogleId = Column(String(48), unique=True)
    GithubId = Column(String(48), unique=True)
    FacebookId = Column(String(48), unique=True)
    VerificationCode = Column(String(48), unique=True)
    CreatedAt = Column(DateTime, default=datetime.now())
    UpdatedAt = Column(DateTime, default=datetime.now())
    ProfilePicture: str = Column(String(48), nullable=True)
    
# Get all users from database
def get_all_users(start_index: int, limit_number: int):
    user = session.query(User).order_by(User.Id.desc()) \
        .offset(start_index).limit(limit_number).all()
    
    return user if user else None

# Get max user id from database
def get_max_user_id() -> int:
    user = session.query(User).order_by(User.Id.desc()).first()
    return user.Id if user else 0

# Get user by id from database
def get_user_by_id(Id: int) -> User:
    user = session.query(User).filter(User.Id == Id).first()
    return user if user else None

# Get user by username from database
def get_user_by_username(Username: str) -> User:
    user = session.query(User).filter(User.Username == Username).first()
    return user if user else None

# Get user by email from database
def get_user_by_bind_id(BindID: str) -> User:
    user = session.query(User).filter(User.BindID == BindID).first()
    return user if user else None

# Get user by google_id oauth from database
def get_user_by_google_id(GoogleId: str) -> User:
    user = session.query(User).filter(User.GoogleId == GoogleId).first()
    return user if user else None

# Get user by github_id oauth from database
def get_user_by_github_id(GithubId: str) -> User:
    user = session.query(User).filter(User.GithubId == GithubId).first()
    return user if user else None

# Get user by facebook_id oauth from database
def get_user_by_facebook_id(FacebookId: str) -> User:
    user = session.query(User).filter(User.FacebookId == FacebookId).first()
    return user if user else None

# Get list user by role from database
def get_users_by_role(Role: Literal['admin', 'user']) -> List[User]:
    users = session.query(User).filter(User.Role == Role).all()
    return users if users else None

# Get list user by status from database
def get_users_by_status(Status: bool) -> List[User]:
    users = session.query(User).filter(User.Status == Status).all()
    return users if users else None

# Search user by keyword from database
def search_users(keyword: str) -> List[User]:
    keyword = f"%{keyword}%"
    users = session.query(User).filter(
        (User.Id == keyword) |
        (User.Username.like(keyword)) |
        (User.DisplayName.like(keyword)) |
        (User.Email.like(keyword))
    ).all()
    return users if users else None

def create_user(user_data) -> Boolean:
    new_user = User(
        BindID = user_data['BindID'],
        Username = user_data['Username'],
        Password = user_data['Password'],
        DisplayName = user_data['DisplayName'],
        AccessToken = user_data['AccessToken'],
        Status = user_data['Status'],
        Blacklist = user_data['Blacklist'],
        Role = user_data['Role'],
        GoogleId = user_data['GoogleId'],
        GithubId = user_data['GithubId'],
        FacebookId = user_data['FacebookId'],
        VerificationCode = user_data['VerificationCode'],
        CreatedAt = user_data['CreatedAt'],
        UpdatedAt = user_data['UpdatedAt'],
        ProfilePicture = user_data['ProfilePicture']
    )
    try : 
        session.add(new_user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def update_user(user_id: int, update_data, update_password = False) -> User:
    user = session.query(User).filter(User.Id == user_id).first()
    if not user:
        return False
    
    if update_password:
        user.Password = update_data['Password']
    
    for key, value in update_data.items():
        setattr(user, key, value)
        
    try:
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def delete_user_by_id(user_Id: int) -> bool:
    user = session.query(User).filter(User.Id == user_Id).first()
    if not user:
        return False
    
    try:
        session.delete(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def delete_user_by_username(Username: str) -> bool:
    user: User = session.query(User).filter(User.Username == Username).first()
    if not user:
        return False
    
    try:
        session.delete(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def delete_user_by_bind_id(BindID: str) -> bool:
    user: User = session.query(User).filter(User.BindID == BindID).first()
    if not user:
        return False
    
    try:
        session.delete(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def check_validate(username: str, password: str) :
    user = session.query(User).filter(User.Username == username).first()
    if not user or user.Status == False:
        return None
    return user

def check_is_email_already_exist(Email: str) -> bool:
    return session.query(User).filter(User.Email == Email).first() is not None
    
def check_is_username_already_exist(Username: str) -> bool:
    return session.query(User).filter(User.Username == Username).first() is not None

def check_is_bind_id_already_exist(BindID: str) -> bool:
    return session.query(User).filter(User.BindID == BindID).first() is not None

def check_is_google_id_already_exist(GoogleId: str) -> bool:
    return session.query(User).filter(User.GoogleId == GoogleId).first() is not None

def check_is_github_id_already_exist(GithubId: str) -> bool:
    return session.query(User).filter(User.GithubId == GithubId).first() is not None

def check_is_facebook_id_already_exist(FacebookId: str) -> bool:
    return session.query(User).filter(User.FacebookId == FacebookId).first() is not None

def check_is_user_blacklisted(Username: str) -> bool:
    return session.query(User).filter(User.Username == Username).first().Blacklist

def check_is_user_activated(Username: str) -> bool:
    return session.query(User).filter(User.Username == Username).first().Status

def reset_password_by_email(Email: str, new_password: str) -> bool:
    user = session.query(User).filter(User.Email == Email).first()
    if not user:
        return False

    user.Password = new_password
    try:
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def reset_password_by_username(Username: str, new_password: str) -> bool:
    user = session.query(User).filter(User.Username == Username).first()
    if not user:
        return False

    user.Password = new_password
    try:
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def generate_verification_code() -> str:
    pass

def reset_verification_code(Username: str) -> bool:
    pass

def is_email_verified(Email: str) -> bool:
    pass

def generate_access_token() -> str:
    pass

def invalidate_all_sessions(Username: str) -> bool:
    pass
