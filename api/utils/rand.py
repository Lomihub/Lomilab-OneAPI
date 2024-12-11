import random, string, uuid

KEY_CHARS = string.digits + string.ascii_letters  # "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY_NUMBERS = string.digits  # "0123456789"

def generate_key() -> str:
    """
    Generate a random key 
        with 16 characters from KEY_CHARS 
            + UUID (32 characters)
    return key: 
    """
    key = [random.choice(KEY_CHARS) for _ in range(16)]
    
    uuid_str = str(uuid.uuid4()).replace('-', '') 
    
    # Convert even index to upper case
    for index, char in enumerate(uuid_str[:32]):
        if index % 2 == 0 and 'a' <= char <= 'z':
            char = char.upper()
        key.append(char)
    
    return ''.join(key)
    

def rand_string(length: int = 8) -> str:
    # random string with KEY_CHARS
    return ''.join(random.choice(KEY_CHARS) for _ in range(length))

def rand_number_string(length: int = 8) -> str:
    # random string with KEY_NUMBERS
    return ''.join(random.choice(KEY_NUMBERS) for _ in range(length))

def rand_range_int(min_val: int = 0, max_val: int = 1000) -> int:
    # [min_val, max_val)
    return random.randint(min_val, max_val - 1)

def rand_range_float(min_val: float = 0.0, max_val: float = 1000.0) -> float:
    # [min_val, max_val)
    return random.uniform(min_val, max_val)