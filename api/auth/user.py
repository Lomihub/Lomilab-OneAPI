class User():
    Id: int            
    BindID: str         
    Username: str
    Password: str
    Email: str
    DisplayName: str
    Token: str
    CreatedAt: str
    UpdatedAt: str
    Blacklist: bool
    
    def __init__(
        self,
        Id: int,
        BindID: str,
        Username: str,
        Password: str,
        Email: str,
        DisplayName: str,
        Token: str,
        CreatedAt: str,
        UpdatedAt: str,
        Blacklist: bool = False
    ) -> None: 
        self.Id = Id
        self.BindID = BindID
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.DisplayName = DisplayName
        self.Token = Token
        self.CreatedAt = CreatedAt
        self.UpdatedAt = UpdatedAt
        self.Blacklist = Blacklist