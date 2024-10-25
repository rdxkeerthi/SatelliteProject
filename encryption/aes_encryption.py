# /encryption/aes_encryption.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def generate_aes_key():
    return os.urandom(16)  # Generate a random 16-byte (128-bit) key

def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ct_bytes  # Prepend IV for decryption

def aes_decrypt(encrypted_data, key):
    iv = encrypted_data[:16]  # Extract IV from the start
    ct = encrypted_data[16:]  # Extract ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()
