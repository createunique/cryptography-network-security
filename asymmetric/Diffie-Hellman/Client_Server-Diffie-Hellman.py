import socket
import random

def generate_dh_public(prime,generator,private_key):
    return pow(generator,private_key,prime)

def compute_dh_shared(public_value,private_key,prime):
    return pow(public_value,private_key,prime)



def encrypt_decrypt_with_xor(text, key):
    
    
    # Convert the key to bytes for XOR operation
    key_bytes = str(key).encode()

    # Convert text to bytes if it's not already in bytes format
    if isinstance(text,bytes):
        txt_bytes = text
    else:
        txt_bytes = text.encode()


    res_bytes = []

    #XOR operation for each byte in the text
    for i in range(len(txt_bytes)):

        key_byte = key_bytes[i%len(key_bytes)]
        xor_result = txt_bytes[i]^key_byte
        res_bytes.append(xor_result)

    return bytes(res_bytes)

def start_server():

    server_socket = socket.socket()
    hostname = socket.gethostname()
    port = 12345

    server_socket.bind((hostname,port))
    server_socket.listen(5)

    server_ip = socket.gethostbyname(hostname)
    print(f"\nServer running on IP: {server_ip}")
    print("Waiting for a client to connect...")

    connection,client_address = server_socket.accept()
    print(f"\nConnected to client at {client_address[0]}:{client_address[1]}\n")



    # Diffie-Hellman parameters
    prime = 23
    generator = 5

    # Server's private and public keys
    server_private = random.randint(1,prime - 1)
    print(f"Server private key: {server_private}")
    server_public = generate_dh_public(prime,generator,server_private)
    print(f"Server public value: {server_public}")

    # Sends server's public value to client
    connection.send(str(server_public).encode())
    print("Sent server's public value to client")

    # Receives client's public value
    client_public = int(connection.recv(1024).decode())
    print(f"Received client's public value: {client_public}")

    # Computes shared key
    shared_key = compute_dh_shared(client_public,server_private,prime)
    print(f"Server shared key: {shared_key}")



    # Get message to send to client
    message = input("Enter message to send: ")
    encrypted = encrypt_decrypt_with_xor(message,shared_key)
    print(f"Encrypted message (hex): {encrypted.hex()}")

    # Send encrypted message
    connection.send(encrypted)
    print("Encrypted message sent successfully\n")

    connection.close()
    server_socket.close()

def start_client():

    client_socket = socket.socket()
    hostname = socket.gethostname()
    port = 12345

    client_socket.connect((hostname,port))
    print("Connected to server")



    prime = 23  # Must match server's prime
    generator = 5


    # Client's private and public keys
    client_private = random.randint(1,prime - 1)
    print(f"Client private key: {client_private}")
    client_public = generate_dh_public(prime,generator,client_private)
    print(f"Client public value: {client_public}")

    # Receive server's public value
    server_public = int(client_socket.recv(1024).decode())
    print(f"Received server's public value: {server_public}")


    # Send client's public value to server
    client_socket.send(str(client_public).encode())
    print("Sent client's public value to server")

    # Compute shared key
    shared_key = compute_dh_shared(server_public,client_private,prime)
    print(f"Client shared key: {shared_key}")

    # Receive and decrypt message
    encrypted = client_socket.recv(1024)
    print(f"Received encrypted message (hex): {encrypted.hex()}")
    decrypted = encrypt_decrypt_with_xor(encrypted,shared_key).decode()
    print(f"Decrypted message: {decrypted}")


    client_socket.close()

def main_menu():

    while True:
        print("\nOptions:")
        print("1.Start server to send encrypted messages")
        print("2.Start client to receive and decrypt messages")
        print("3.Exit")
        choice = input("Choose an option(1-3): ")

        if choice =='1':
            start_server()

        elif choice =='2':
            start_client()
        elif choice =='3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1,2 or 3")

if __name__ == "__main__":
    main_menu()
