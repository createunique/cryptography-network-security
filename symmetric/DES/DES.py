import base64
import hashlib
from Crypto.Cipher import DES

PASSWORD = "SecurePass123"
SALT = b'\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    
kinfo = PASSWORD.encode('utf-8')+SALT #key information
hashed = hashlib.md5(kinfo).digest()  #hashing key information to get 16 bytes key and iv

ekey,ivector = hashed[:8], hashed[8:]


def text_encryption():

    text = input("Enter text to encrypt: ")

    # Encrypt text using DES encryption in CBC mode with IV and key generated from password and salt
    encrypted = DES.new(ekey, DES.MODE_CBC, ivector).encrypt(
        text.encode() + b'\x00'*(8 - len(text) % 8)
    )
    print("\nEncrypted Result:",base64.b64encode(encrypted).decode())

def text_decryption():
    encrypted_b64 = input("Enter text to decrypt: ")

    # Decrypt text using DES decryption in CBC mode with IV and key generated from password and salt
    decrypted = DES.new(ekey, DES.MODE_CBC, ivector).decrypt(
        base64.b64decode(encrypted_b64)
    )
    print("\nDecrypted Message:",decrypted.rstrip(b'\x00').decode())


def file_encryption():

    src = input("Enter source filename: ")
    dest = input("Enter output filename: ")
    with open(src, 'rb') as f_in, open(dest, 'wb') as f_out:
        data = f_in.read()
        encrypted = DES.new(ekey, DES.MODE_CBC, ivector).encrypt(
            data + b'\x00'*(8 - len(data) % 8)
        )
        f_out.write(base64.b64encode(encrypted))
    print(f"\nFile encrypted successfully: {dest}")


def file_decryption():

    src = input("Enter encrypted filename: ")
    dest = input("Enter output filename: ")

    with open(src, 'rb') as f_in, open(dest, 'wb') as f_out:
        encrypted = base64.b64decode(f_in.read())
        decrypted = DES.new(ekey, DES.MODE_CBC, ivector).decrypt(encrypted)
        f_out.write(decrypted.rstrip(b'\x00'))

    print(f"\nFile decrypted successfully: {dest}")

    

if __name__ == "__main__":
    
    while True:

        print("\n" + "="*40)
        print("DES Encryption Toolkit")
        print("="*40)
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Encrypt File")
        print("4. Decrypt File")
        print("5. Exit Program")
        print("="*40)
    
        choice = input("Enter your choice (1-5): ")

        
        if choice == '1':
            text_encryption()
        elif choice == '2':
            text_decryption()
        elif choice == '3':
            file_encryption()
        elif choice == '4':
            file_decryption()
        elif choice == '5':
            print("\nExiting program... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
