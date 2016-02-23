import socket, sys, time

HOST = 'localhost'
PORT = 8088

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_add = (HOST, PORT)
print sys.stderr, 'connecting'
s.connect(s_add)
print 'connected'

while True:
	data = s.recv(500)
	print data
	# print '\n'