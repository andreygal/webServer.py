#see http://wps.pearsoned.com/ecs_kurose_compnetw_6/216/55463/14198700.cw/-/14198926/index.html for assignments 
#import socket module for AF_INET socket.accept() 
#returns socketObj, (host, port)
from socket import *
from email.utils import formatdate
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server (might try '' argument)
serverPort = 6789
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print 'Ready to serve...'
	#The return value is a pair (conn, address) where conn is a new 
	#socket object usable to send and 
	#receive data on the connection, and address is the address bound 
	#to the socket on the other end of the connection.
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read() 
		#Send one HTTP header line into socket
		connectionSocket.send('HTTP/1.1 200 OK \n' + 
		                      'Connection: close \n' +
	                        'Date: ' +  formatdate(timeval=None, localtime=False, usegmt=True) + '\n'
                          'Content-Type: text/html \n' + '\n')
                          
    #Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#For multithreading https://docs.python.org/3/howto/sockets.html
		connectionSocket.send('HTTP/1.1 404 'File not found \n' + '\n')
		#Close client socket
		connectionSocket.close()


		
