
from cryptography.fernet import Fernet

def aes_encrypt(text):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(text.encode())
    print("Cipher text : ", cipher_text)
    return cipher_text, key

def aes_decrypt(cipher_text, key):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    print("Plain text : ", plain_text)
    return plain_text





def send():
    import socket

    # Create socket
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.bind((host, port))
    s.listen(5)

    server_ip = socket.gethostbyname(host)
    print("\nListening to ip:", server_ip)
    print('Waiting for connection...')

    conn, addr = s.accept()
    print(f"\nConnection established with {addr[0]} : {addr[1]}\n")


    text = input("Enter the plain text : ")
    encrypted_text, key = aes_encrypt(text) 

    # Send the encrypted text and key
    conn.send(encrypted_text)
    conn.send(key)
    print('Message and key sent successfully\n')

    conn.close()


def receive():

    import socket

    # Create socket
    s = socket.socket()
    host = "10.1.86.93"
    port = 12345

    s.connect((host, port))
    print('Connected to sender')

    # Receive the message
    # message = s.recv(1024).decode()
    # Receive the encrypted message and key
    encrypted_message = s.recv(1024)
    key = s.recv(1024)
    print("Received encrypted message")
    
    decrypt_message = aes_decrypt(encrypted_message, key)
    print("\nReceived message:", decrypt_message)
    s.close()



def main():
    while True:
        print("\n1 - Send \n2 - receive  \n3 - Stop")
        choice = int(input("Enter the choice : "))
        
        if choice == 1:
            send()
        if choice == 2:
            receive()
        elif choice == 3:
            print("Stopping the program.....")
            exit()


if __name__ == "__main__":
    main()
