import csv
from time import sleep
import sys
import datetime

path = "C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val"
count = 0
level_count = 1
hold = 0
alert_flag = 0
addon_fr = 0
with open('export.txt') as infile:
	reader = csv.reader(infile)
	for row in reader:
		# sleep(1)
		# print row		
		
		# zero_count = 0
		start_time = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
		if count == 0:
			end_time = start_time + datetime.timedelta(minutes=1)
		new_fr = float(row[1])
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
					else: #Reduce Level and Start Over
						alert_flag = 0
						if lp > 1:
							fp = open(path,"w")
							fp.write(str(lp-1))
							fp.close()

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
			level_count = level_count+1
			count = 0
			addon_fr = new_fr
