from datetime import datetime
from typing import List, Optional, Literal, Union
from api.connection.database import Database

class User:
    """
    
    """
    Id: int            
    BindID: str         
    Username: str
    Password: str
    DisplayName: str
    AccessToken: str
    Status: bool
    Blacklist: bool
    Role: Literal['admin', 'user']
    GoogleId: Optional[str] = None
    GithubId: Optional[str] = None
    FacebookId: Optional[str] = None
    VerificationCode: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ProfilePicture: Optional[str] = None
    
    def __init__(
        self,
        Id: int,            
        BindID: str,        
        Username: str,
        Password: str,
        DisplayName: str,
        AccessToken: str,
        Status: bool = True,
        Blacklist: bool = False,
        Role: Literal['admin', 'user'] = 'user',
        GoogleId: Optional[str] = None,
        GithubId: Optional[str] = None,
        FacebookId: Optional[str] = None,
        VerificationCode: Optional[str] = None,
        CreatedAt: Optional[datetime] = None,
        UpdatedAt: Optional[datetime] = None,
        ProfilePicture: Optional[str] = None,
    ) -> None: 
        self.Id = Id
        self.BindID = BindID
        self.Username = Username
        self.Password = Password
        self.DisplayName = DisplayName
        self.AccessToken = AccessToken
        self.Status = Status
        self.Blacklist = Blacklist
        self.Role = Role
        self.GoogleId = GoogleId
        self.GithubId = GithubId
        self.FacebookId = FacebookId
        self.VerificationCode = VerificationCode
        self.CreatedAt = CreatedAt
        self.UpdatedAt = UpdatedAt
        self.ProfilePicture = ProfilePicture
        
    def __str__(self) -> str:
        return f"User(Id={self.Id}, BindID={self.BindID}, Username={self.Username}, Password={self.Password}, DisplayName={self.DisplayName}, AccessToken={self.AccessToken}, Status={self.Status}, Blacklist={self.Blacklist}, Role={self.Role}, GoogleId={self.GoogleId}, GithubId={self.GithubId}, FacebookId={self.FacebookId}, VerificationCode={self.VerificationCode}, CreatedAt={self.CreatedAt}, UpdatedAt={self.UpdatedAt}, ProfilePicture={self.ProfilePicture})"
  

def get_all_users() -> List[User]:
    pass

def get_max_user_id() -> int:
    pass
          
def get_user_by_id(Id: int) -> User:
    pass

def get_user_by_username(Username: str) -> User:
    pass

def get_user_by_bind_id(BindID: str) -> User:
    pass

def get_user_by_google_id(GoogleId: str) -> User:
    pass

def get_user_by_github_id(GithubId: str) -> User:
    pass

def get_user_by_facebook_id(FacebookId: str) -> User:
    pass

def get_users_by_role(Role: Literal['admin', 'user']) -> List[User]:
    pass

def get_users_by_status(Status: bool) -> List[User]:
    pass

def search_users() -> List[User]:
    pass

def create_user(user: User) -> User:
    pass

def update_user(user: User) -> User:
    pass

def delete_user_by_id(Id: int) -> bool:
    pass

def delete_user_by_username(Username: str) -> bool:
    pass

def delete_user_by_bind_id(BindID: str) -> bool:
    pass

def check_validate() -> bool:
    pass

def check_is_admin() -> bool:
    pass

def check_is_email_already_exist(Email: str) -> bool:
    pass

def check_is_username_already_exist(Username: str) -> bool:
    pass

def check_is_bind_id_already_exist(BindID: str) -> bool:
    pass

def check_is_google_id_already_exist(GoogleId: str) -> bool:
    pass

def check_is_github_id_already_exist(GithubId: str) -> bool:
    pass

def check_is_facebook_id_already_exist(FacebookId: str) -> bool:
    pass

def check_is_user_blacklisted(Username: str) -> bool:
    pass

def check_is_user_activated(Username: str) -> bool:
    pass

def reset_password_by_email(Email: str) -> bool:
    pass

def reset_password_by_username(Username: str) -> bool:
    pass

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