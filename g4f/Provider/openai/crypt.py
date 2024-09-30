from __future__ import annotations

import json
import base64
import hashlib
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def pad(data: str) -> bytes:
    # Convert the string to bytes and calculate the number of bytes to pad
    data_bytes = data.encode()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data_bytes) + padder.finalize()
    return padded_data


def encrypt(data, key):
    salt = ""
    salted = ""
    dx = bytes()

    # Generate salt, as 8 random lowercase letters
    salt = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8))

    # Our final key and IV come from the key and salt being repeatedly hashed
    for x in range(3):
        dx = hashlib.md5(dx + key.encode() + salt.encode()).digest()
        salted += dx.hex()

    # Pad the data before encryption
    data = pad(data)

    iv = bytes.fromhex(salted[64:96])
    key_bytes = bytes.fromhex(salted[:64])

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(data) + encryptor.finalize()

    return json.dumps(
        {
            "ct": base64.b64encode(ct).decode(),
            "iv": salted[64:96],
            "s": salt.encode().hex(),
        }
    )


def unpad(data: bytes) -> bytes:
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(data) + unpadder.finalize()


def decrypt(data: str, key: str):
    # Parse JSON data
    parsed_data = json.loads(data)
    ct = base64.b64decode(parsed_data["ct"])
    iv = bytes.fromhex(parsed_data["iv"])
    salt = bytes.fromhex(parsed_data["s"])

    salted = ''
    dx = b''
    for x in range(3):
        dx = hashlib.md5(dx + key.encode() + salt).digest()
        salted += dx.hex()

    key_bytes = bytes.fromhex(salted[:64])

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    data = decryptor.update(ct) + decryptor.finalize()

    if data.startswith(b'[{"key":'):
        return unpad(data).decode()
