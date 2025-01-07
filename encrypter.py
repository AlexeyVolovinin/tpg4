from cryptography.fernet import Fernet

def load_key_from_file(key_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    return key

def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def main():
    key_file = 'require.gitcache'
    input_file = 'requirements.gitcache'
    output_file = 'requirements.gitcache'
    key = load_key_from_file(key_file)
    encrypt_file(input_file, output_file, key)

if __name__ == '__main__':
    main()