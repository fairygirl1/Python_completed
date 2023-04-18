import socket
import threading

# Define host and port
HOST = 'localhost'
PORT = 12345

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))

# Function to receive messages from server
def receive():
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024)
            print(message.decode())
        except:
            # An error occurred, close the client socket
            client_socket.close()
            break

# Function to send messages to server
def send():
    while True:
        message = input()
        # Send message to server
        client_socket.send(message.encode())

# Create threads for sending and receiving messages
receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

# Start threads
receive_thread.start()
send_thread.start()
