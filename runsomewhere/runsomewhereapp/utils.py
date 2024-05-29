# hospital/utils.py
import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 256-bit key (store this securely)
# key = os.urandom(32)
# print(key.hex())  # Save this key securely and use it in your project

# Use the securely stored key (this is an example key, use your securely stored key)
key = bytes.fromhex('3a41bf435f0764d920fefc3bedecf9d8bb875738c31391330a1d50a586dcf589')

def encrypt_data(data):
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad data to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    padded_data = padder.update(data.encode()) + padder.finalize()
    
    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # Return the IV and encrypted data combined
    return (iv + encrypted_data).hex()

def decrypt_data(encrypted_data_hex):
    encrypted_data = bytes.fromhex(encrypted_data_hex)
    
    # Extract the IV from the encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]
    
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the data
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    return decrypted_data.decode()
