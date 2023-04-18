import socket
import threading

# Define host and port
HOST = 'localhost'
PORT = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# List of connected clients
clients = []

# Function to broadcast messages to all connected clients
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    clients.append(client_socket)
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if message:
                print(f"Received message: {message.decode()}")
                # Broadcast message to all clients
                broadcast(message, client_socket)
            else:
                # Remove client from list of connected clients
                clients.remove(client_socket)
                client_socket.close()
                break
        except:
            # Remove client from list of connected clients
            clients.remove(client_socket)
            client_socket.close()
            break

# Main loop to accept incoming connections
while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    # Create new thread to handle client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
