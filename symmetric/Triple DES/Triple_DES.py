import base64
import hashlib
from Crypto.Cipher import DES3

PASSWORD = "SecurePass123"
SALT = b'\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'

kinfo = PASSWORD.encode('utf-8') + SALT
hashed = hashlib.md5(kinfo).digest()

# Generate a 24-byte key for Triple DES by combining parts of the MD5 hash
ekey = hashed[:8] + hashed[8:16] + hashed[:8]  # Results in a 24-byte key
ivector = hashed[8:16] 

def text_encryption():
    text = input("Enter text to encrypt: ")

    # Pad the text with null bytes to make its length a multiple of 8
    data = text.encode()
    pad = 8 - (len(data) % 8)
    padded_data = data + b'\x00' * pad

    cipher = DES3.new(ekey, DES3.MODE_CBC, ivector)
    encrypted = cipher.encrypt(padded_data)
    print("\nEncrypted Result:", base64.b64encode(encrypted).decode())

def text_decryption():

    encrypted_b64 = input("Enter text to decrypt: ")

    encrypted_data = base64.b64decode(encrypted_b64)
    cipher = DES3.new(ekey, DES3.MODE_CBC, ivector)
    decrypted = cipher.decrypt(encrypted_data)

    # Remove null bytes padding
    unpadded = decrypted.rstrip(b'\x00')
    print("\nDecrypted Message:", unpadded.decode())




if __name__ == "__main__":
    while True:
        print("\n" + "="*40)
        print("Triple DES Encryption Toolkit")
        print("="*40)
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit Program")
        print("="*40)
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text_encryption()
        elif choice == '2':
            text_decryption()
        elif choice == '3':
            print("\nExiting program... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
