import socket

listenerSocket = socket.socket()

serverIP = "127.0.0.1"
serverPort = 6666

listenerSocket.bind((serverIP,serverPort))
listenerSocket.listen(0)

while True:
	handlerSocket, addr = listenerSocket.accept()
	print 'new client are connected: ',addr
	
while True:
	message = handlerSocket.recv(1024)
	print 'client: ',message
	message = raw_input("write your message: ")
	handlerSocket.send(message)
	