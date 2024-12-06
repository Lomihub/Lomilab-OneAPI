from typing import Literal, Optional
from datetime import datetime

class User():
    Id: int            
    BindID: str         
    Username: str
    Password: str
    DisplayName: str
    Role: Literal["admin", "user"] = "user"
    Status: bool
    Email: Optional[str] = None
    GoogleID: Optional[str] = None
    FacebookID: Optional[str] = None
    GithubID: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ProfilePicture: Optional[str] = None
    Blacklist: bool
    
    def __init__(
        self,
        Id: int,            
        BindID: str,        
        Username: str,
        Password: str,
        DisplayName: str,
        Role: Literal["admin", "user"] = "user",
        Status: bool = True,
        Email: Optional[str] = None,
        GoogleID: Optional[str] = None,
        FacebookID: Optional[str] = None,
        GithubID: Optional[str] = None,
        CreatedAt: Optional[datetime] = None,
        UpdatedAt: Optional[datetime] = None,
        ProfilePicture: Optional[str] = None,
        Blacklist: bool = False
    ) -> None:
        self.Id = Id
        self.BindID = BindID
        self.Username = Username
        self.Password = Password
        self.DisplayName = DisplayName
        self.Role = Role
        self.Status = Status
        self.Email = Email
        self.GoogleID = GoogleID
        self.FacebookID = FacebookID
        self.GithubID = GithubID
        self.CreatedAt = CreatedAt
        self.UpdatedAt = UpdatedAt
        self.ProfilePicture = ProfilePicture
        self.Blacklist = Blacklist
    
    def __str__(self) -> str:
        return f"User(
            Id={self.Id}, 
            BindID={self.BindID}, 
            Username={self.Username}, 
            Password={self.Password}, 
            DisplayName={self.DisplayName}, 
            Role={self.Role}, 
            Status={self.Status}, 
            Email={self.Email}, 
            GoogleID={self.GoogleID}, 
            FacebookID={self.FacebookID}, 
            GithubID={self.GithubID}, 
            CreatedAt={self.CreatedAt}, 
            UpdatedAt={self.UpdatedAt}, 
            ProfilePicture={self.ProfilePicture}, 
            Blacklist={self.Blacklist}
            )"