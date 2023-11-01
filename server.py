import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
host = '127.0.0.1'
port = 9999

#Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()
print(f"Server is listening on {host}:{port}")

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Receive data from the client
while True:
    data = client_socket.recv(1024).decode()

    if not data:
        break

    print(f"Received {data} from the client")

    # Send data back to the client
    response = f"Server Received: {data}"
    client_socket.send(response.encode())

# Close the client socket
client_socket.close()
server_socket.close()

