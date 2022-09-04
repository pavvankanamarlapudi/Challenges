import socket
from _thread import *

# Create a socket connection using the socket() of the socket library and declare the host and port on which we need to communicate with clients.
s = socket.socket()
print ("Socket successfully created")

host = '127.0.0.1'
port = 6969
threadCount=0


# Bind the host and port to the socket server we created above. So, if it binds successfully then it starts waiting for the client otherwise it just returns the error that occurred while establishing a connection
try:
    s.bind(('', port))
    print ("socket binded to %s" %(port))
except socket.error as e:
    print(str(e))


print("Waiting for Connections..")
s.listen(5)

# Define a new function named threaded_client which connects to each client at a different address given by the server
def threaded_client(connection):
    connection.send(str.encode("welcome to the server"))
    # data = connection.recv(2048)
    # reply = "Server Says: "+ data.decode("utf-8")
    # connection.sendall(str.encode(reply))
    
    while True:
        # Use the recv() function to get data from each client independently and then simply return the
        #  reply to the particular client with the same message with the string concatenate “Server Says” in the beginning
        data = connection.recv(2048)
        reply = "Server Says: "+ data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(reply))

# We want to run our Server all the time, which means we do not want to make our Server get stopped. Therefore, 
# we need to use a while loop to make it run the Server endlessly until we manually stop the Server
while True:
    # Accept connections from the client using accept the () function of the socket server.
    # It returns the type of client which has connected along with the unique thread number or address provided to it.
    client,address = s.accept()
    print("connected to "+str(address[0])+str(address[1]))
    start_new_thread(threaded_client,(client,))
    threadCount+=1
    print("ThreadNumber: "+str(threadCount))
s.close()
