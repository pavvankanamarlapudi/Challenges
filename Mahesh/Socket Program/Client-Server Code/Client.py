# Create a Client script

# We need the same socket library to establish a connection with the Server-Side and 
# assign the same host and port number to the client as we defined in the Server otherwise 
# it will not make the connection between them.
import socket

clientsocket = socket.socket()

host = '127.0.0.1'
port = 6969

try:
    # Set up a connection using connect() of the socket library which establishes 
    # a connection with the server using the host and port we provided.
    clientsocket.connect((host,port))
except socket.error as e:
    print(str(e))

Response = clientsocket.recv(1024)
print(Response.decode('utf-8'))
# We want is to make sure that the Client keeps running as the Server is Running.
while True:
    #  And we also going to provide an input option to the client
    Input = input("Say Something:")
    clientsocket.send(str.encode(Input))
    # so that it can send data back to the Server and along with this we also use the recv() function to receive data from Server Side
    response = clientsocket.recv(1024)
    print(response.decode("utf-8"))

clientsocket.close()