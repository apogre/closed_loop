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
while True:
	count == 0
	level_count = 1
	data = s.recv(1000)
	if "EmotivAffectiv" in data:
		print data
		a_split = data.split(';')
		new_fr = a_split[8]
		if new_fr<0:
			new_fr = 0
		if count < 233:
			count = count+1
			if count!=0:
				old_fr = old_fr+new_fr
			else:
				new_fr = fr			
		else:
			if level_count > 1:
				if level_count%2 != 0: #if odd
					new_frustration = old_fr/233
				else:
					new_frustration1 = (old_fr/233)
				if new_frustration1 < new_frustration:
					#lower the level
				else:
					#increase the level
			level_count = level_count+1
			count = 0
		# print '\n'