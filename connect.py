from pixelracer.models import Affectiv, db
from datetime import datetime
import socket, sys, time

HOST = 'localhost'
PORT = 8088

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_add = (HOST, PORT)
print sys.stderr, 'connecting'
s.connect(s_add)
print 'connected'
count == 0
while True:
	data = s.recv(1000)
	if "EmotivAffectiv" in data:
		print data
		a_split = data.split(';')
		fr = a_split[8]
		for i in range()
		print '\n'