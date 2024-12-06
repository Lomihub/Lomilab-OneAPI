import hashlib, os, base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def sha256_encrypt(data_raw: str) -> str:
    # Encrypt data using SHA-256 -> 64-bit hash
    return hashlib.sha256(data_raw.encode()).hexdigest()

def sha256_decrypt(data_encrypted: str) -> str:
    # Decrypt data using SHA-256
    return hashlib.sha256(data_encrypted.encode()).hexdigest()

def md5_encrypt(data_raw: str) -> str:
    # Encrypt data using MD5 -> 32-bit hash
    return hashlib.md5(data_raw.encode()).hexdigest()

def base64_encrypt(data_raw: str) -> str:
    # Encrypt data using Base64
    b= base64
    return base64.b64encode(data_raw.encode()).decode()

def base64_decrypt(data_encrypted: str) -> str:
    # Decrypt data using Base64
    return base64.b64decode(data_encrypted).decode()

def aes256_encrypt(plain_text: str, key: str) -> str:
    key_bytes = key.encode('utf-8')  
    iv = os.urandom(16)  
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padding_length = 16 - len(plain_text) % 16
    plain_text_padded = plain_text + chr(padding_length) * padding_length  # Padding dữ liệu

    ciphertext = encryptor.update(plain_text_padded.encode('utf-8')) + encryptor.finalize()

    return base64.b64encode(iv + ciphertext).decode('utf-8')
    
    