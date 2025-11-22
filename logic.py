import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.backends import default_backend
from pathlib import Path
import secrets



#encryption
def encrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        data = file.read()


    #generating salt
    salt = secrets.token_bytes(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    #encrypt with AES-GCM 
    aesgcm = AESGCM(key)
    nonce = secrets.token_bytes(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)

    file_path = Path(file_path)
    extension = file_path.suffix.encode()
    output_path = file_path.with_suffix(".efy")

    with open(output_path, 'wb') as file:
        file.write(salt + nonce + bytes([len(extension)]) + extension + ciphertext)

    return True

def decrypt_file(file_path, password):
    path = Path(file_path)

    with open(path, 'rb') as file:
        blob = file.read()

    salt = blob[:16]  # 16 bytes
    nonce = blob[16:28]  # next 12 bytes
    ext_len = blob[28]  # 1 byte -> length of extension
    extension = blob[29:29+ext_len].decode()  # extension string
    ciphertext = blob[29+ext_len:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    aesgcm = AESGCM(key)
    
    try:
        decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)
    except InvalidTag:
        # Raised if password is wrong or ciphertext is tampered
        return False

    out_path = path.with_suffix(extension)

    with open(out_path, 'wb') as file:
        file.write(decrypted_data)

    return True

