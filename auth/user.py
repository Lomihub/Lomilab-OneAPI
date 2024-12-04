from pydantic import BaseModel

class User(BaseModel):
    Id: int
    BindID: str
    Username: str
    Password: str
    Email: str
    Token: str
    Blacklist: bool
    CreatedAt: str
    UpdatedAt: str
    