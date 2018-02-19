import socket 
import config

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = config.PORT

client_socket.connect((HOST, PORT))
msg = client_socket.recv(1024)

client_socket.close()
print (msg.decode('utf-8'))
