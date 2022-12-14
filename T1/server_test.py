import json
import socket

# Create a socket object
s = socket.socket()

# Get the local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind to the port
s.bind((host, port))
print("Waiting for incoming connections...")

# Listen for incoming connections
s.listen(4)

for i in range(4):
    # Accept the incoming connection
    conn, addr = s.accept()

    # Print the client's address
    print("Connection from: " + str(addr))

    # Receive data from the client
    data = b'' + conn.recv(1024)

    # Print the received message
    print("Received message: " , json.loads(data.decode('utf-8')))

    # Send a reply to the client
    conn.sendall(str.encode("Thank you for sending a message!"))


# Close the connection
conn.close()
