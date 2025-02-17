from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generate a 32-byte AES key and 16-byte IV
def generate_key():
    return os.urandom(32), os.urandom(16)

# Encrypt the file
def encrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as f:
        data = f.read()

    # Pad the data to make it a multiple of block size (16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Encrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted_data)  # Prepend IV for decryption

    print(f"File encrypted successfully: {encrypted_file_path}")

# Decrypt the file
def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as f:
        iv = f.read(16)  # Read the first 16 bytes (IV)
        encrypted_data = f.read()

    # Decrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    # Write the decrypted file
    decrypted_file_path = encrypted_file_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as f:
        f.write(data)

    print(f"File decrypted successfully: {decrypted_file_path}")

# Example usage
if __name__ == "__main__":
    print("AES-256 File Encryption Tool")
    option = input("Choose an option (1-Encrypt, 2-Decrypt): ").strip()
    file_path = input("Enter the file path: ").strip()

    if option == "1":
        key, iv = generate_key()
        encrypt_file(file_path, key, iv)
        print(f"Save this key for decryption: {key.hex()}")
    elif option == "2":
        key_hex = input("Enter the key (hex format): ").strip()
        key = bytes.fromhex(key_hex)
        decrypt_file(file_path, key)
    else:
        print("Invalid option!")