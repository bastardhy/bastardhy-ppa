import socket

handlerSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 6666

handlerSocket.connect((serverIP,serverPort))
print 'connected to server'

while True:
	message = raw_input("write your message: ")
	
	handlerSocket.send(message)
	
	print 'server: ',message
message = handlerSocket.recv(1024)