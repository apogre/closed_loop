import csv
from time import sleep
import sys
import datetime
from pixelracer.models import Affectiv, db
from datetime import datetime
import socket, sys, time

path = "C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val"
path1 = "C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val_updates"

count = 0
level_count = 1
hold = 0
alert_flag = 0
addon_fr = 0

HOST = 'localhost'
PORT = 8088

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_add = (HOST, PORT)
print sys.stderr, 'connecting'
s.connect(s_add)
print 'connected'
while True:
	data = s.recv(1000)
	if "EmotivAffectiv" in data:
		# print data
		a_split = data.split(';')
		start_time = datetime.datetime.now()
		if count == 0:
			end_time = start_time + datetime.timedelta(minutes=1)
		new_fr = float(a_split[8])
		if start_time <= end_time:
			count = count+1
			if count>1:
				old_fr = old_fr+new_fr
			else:
				old_fr = new_fr+addon_fr
		else:
			if level_count > 1:
				if level_count%2 != 0: #if odd
					new_frustration = new_frustration1
					new_frustration1 = old_fr/count
				else:
					if level_count != 2:
						new_frustration = new_frustration1
					new_frustration1 = old_fr/count
				print "new_frustration==>" + str(new_frustration)	
				print "new_frustration1-==>" + str(new_frustration1)
				if new_frustration1 < new_frustration: #drop in frustration
					if alert_flag != 1: #drop without an increase
						f = open(path)
						lp=f.read()
						f.close()
						print lp
						lp = int(lp)
						if lp > 1:
							fp = open(path,"w")
							fp.write(str(lp+1))
							fp.close()
							fp1 = open(path1,"a")
							fp1.write(str(lp+1)+'\n')
							fp1.close()
					else: #Reduce Level and Start Over
						alert_flag = 0
						if lp > 1:
							fp = open(path,"w")
							fp.write(str(lp-1))
							fp.close()
							fp1 = open(path1,"a")
							fp1.write(str(lp-1)+'\n')
							fp1.close()

				else: #increase in frustration
					alert_flag = 1
					print "Increasing the level"
					f = open(path)
					lp=f.read()
					f.close()
					print lp
					lp = int(lp)
					if lp >= 1:
						fp = open(path,"w")
						fp.write(str(lp+1))
						fp.close()
						fp1 = open(path1,"a")
						fp1.write(str(lp+1)+'\n')
						fp1.close()
			else:
				new_frustration = old_fr/count
				f = open(path)
				li=f.read()
				f.close()
				print li
				li = int(li)
				if li == 1:
					fi = open(path,"w")
					fi.write(str(li+1))
					fi.close()
					fp1 = open(path1,"a")
					fp1.write(str(lp+1)+'\n')
					fp1.close()			
			level_count = level_count+1
			count = 0
			addon_fr = new_fr
