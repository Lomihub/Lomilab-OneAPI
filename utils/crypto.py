import bcrypt

def hash_password(password: str) -> str:
    SALT = bcrypt.gensalt()
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), SALT)
    return hashed_password
    
    
def validate_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))