import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's address and port
server_address = ('127.0.0.1', 9999)

# Connect to the server
client_socket.connect(server_address)

while True:
    # Send data
    message = input("Enter a message to send to the server (or 'quit' to exit): ")
    
    if message.lower() == 'quit':
        break

    client_socket.sendall(message.encode())

    # Receive response
    response = client_socket.recv(1024).decode()

    print("Response from server: " + response)

# Close the socket
client_socket.close()


