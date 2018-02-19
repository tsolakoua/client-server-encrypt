import socket
import hashlib

def encrypt(str):
	encoded_input = str.encode('utf-8')
	hash_sha1 = hashlib.sha1(encoded_input)
	return hash_sha1.hexdigest()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 8323
MAX_REQUESTS = 10

server_socket.bind((HOST, PORT))
server_socket.listen(MAX_REQUESTS)

while True:
	client_socket, addr = server_socket.accept()

	print("Connected with: ", str(addr))
	client_socket.send(encrypt(str(addr)).encode('utf-8'))
	client_socket.close()