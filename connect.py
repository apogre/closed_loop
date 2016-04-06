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
	zero_count = 0
	data = s.recv(1000)
	if "EmotivAffectiv" in data:
		print data
		a_split = data.split(';')
		new_fr = a_split[8]
		f = open("test.txt","a") #opens file with name of "test.txt"
		f.write(new_fr)
		f.close()
		if new_fr<0:
			zero_count = zero_count+1
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
					 l = open("C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val","r+").read()
					 if l > 1:
					 	f = open("C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val","w")
					 	f.write(l-1)
					 	f.close()
				else:
					#increase the level
					lp = open("C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val","r+").read()
					 if lp > 1:
					 	fp = open("C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val","w")
					 	fp.write(l+1)
					 	fp.close()
			else:
				li = open("C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val","r+").read()
				if li == 1:
					fi = open("C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val","w")
					fi.write(l+1)
					fi.close()
			level_count = level_count+1
			count = 0
			zero_count = 0
		# print '\n'