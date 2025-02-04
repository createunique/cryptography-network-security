# This is a basic client server program to send and receive messages between two systems

import socket

def send():

    # Create socket
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.bind((host, port))
    s.listen(5)

    server_ip = socket.gethostbyname(host)
    print("\nListening to ip:",server_ip)
    print('Waiting for connection...')

    conn,addr = s.accept()
    print(f"\nConnection established with {addr[0]} : {addr[1]}\n")

    # Get text input from user
    message = input("Enter your message to send: ")

    # Send the message
    conn.send(message.encode())
    print('Message sent successfully\n')

    conn.close()


def receive():

    # Create socket
    s = socket.socket()
    host = "10.1.76.184"  # sender's IP
    port = 12345

    s.connect((host, port))
    print('Connected to sender')

    # Receive the message
    message = s.recv(1024).decode()
    print("\nReceived message:", message)

    s.close()



def main():
    while True:
        print("\n1. Send message to receiver \n2. Receive message from sender \n3. Stop")
        choice = int(input("Enter the choice : "))


        if choice == 1:
            send()
        
        elif choice == 2:
            receive()
        elif choice == 3:
            break
        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()
