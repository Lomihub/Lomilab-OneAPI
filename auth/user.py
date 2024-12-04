from pydantic import BaseModel

class User(BaseModel):
    Id: int
    Username: str
    Password: str
    Token: str