from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Anahtar ve IV oluşturma
def generate_key_and_iv():
    key = os.urandom(32)  # AES-256 için 32 baytlık anahtar
    iv = os.urandom(16)   # 16 baytlık IV
    return key, iv

# Dosyayı şifreleme
def encrypt_file(file_path, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    with open(file_path, 'rb') as f:
        data = f.read()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    with open(file_path + ".enc", 'wb') as f:
        f.write(iv + encrypted_data)  # IV'yi şifreli verinin başına ekleyin
    
    print(f"{file_path} dosyası şifrelendi ve {file_path}.enc olarak kaydedildi.")

# Dosyayı çözme
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        iv = f.read(16)  # İlk 16 bayt IV
        encrypted_data = f.read()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()
    
    with open(file_path.replace(".enc", ""), 'wb') as f:
        f.write(data)
    
    print(f"{file_path} dosyası çözüldü ve {file_path.replace('.enc', '')} olarak kaydedildi.")

if __name__ == "__main__":
    # Anahtar ve IV oluşturma (bir kez yapmanız yeterli)
    key, iv = generate_key_and_iv()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

    # Dosya şifreleme
    encrypt_file("important_data.txt", key, iv)

    # Şifrelenmiş dosyayı çözme (deneme amaçlı)
    decrypt_file("important_data.txt.enc", key)
