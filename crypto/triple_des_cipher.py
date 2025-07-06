from Crypto.Cipher import DES3
import base64
import hashlib

def pad(data):
    return data + (8 - len(data) % 8) * chr(8 - len(data) % 8)

def unpad(data):
    return data[:-ord(data[-1])]

def encrypt_3des(data, key):
    key = hashlib.sha256(key.encode()).digest()[:24]
    cipher = DES3.new(key, DES3.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(data).encode())
    return base64.b64encode(ct_bytes).decode()

def decrypt_3des(enc_data, key):
    key = hashlib.sha256(key.encode()).digest()[:24]
    cipher = DES3.new(key, DES3.MODE_ECB)
    pt = cipher.decrypt(base64.b64decode(enc_data))
    return unpad(pt.decode())
