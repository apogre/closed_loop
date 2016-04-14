import csv
from time import sleep
import sys
import datetime

path = "C:\\Users\\apradha7\\Downloads\\git2016\\closed_loop\\pixelracer\\controllers\\level_val"
count = 0
level_count = 1
hold = 0
alert_flag = 0
with open('export.txt') as infile:
	reader = csv.reader(infile)
	for row in reader:
		# sleep(1)
		# print row		
		
		# zero_count = 0
		start_time = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
		if count == 0 and hold == 0:
			end_time = start_time + datetime.timedelta(minutes=1)
		new_fr = float(row[1])
		# print new_fr
		# print count
		# if new_fr<0:
		# 	print "new fr in zero"
		# 	zero_count = zero_count+1
		# 	new_fr = 0
		if start_time <= end_time:
			hold = 0
			# print "here"
			# print count
		# 	abc = inputs()
			count = count+1
			if count>1:
				old_fr = old_fr+new_fr
			else:
				old_fr = new_fr
			# print old_fr			
		else:
			# print old_fr
			# print "level 1"
			# print count
			# raw_input()
			# abc = input()
			if level_count > 1:
				# print "level count > 1s"
				# sys.exit(1)
				# pass
				if level_count%2 != 0: #if odd
					new_frustration = new_frustration1
					new_frustration1 = old_fr/count
				else:
					if level_count != 2:
						new_frustration = new_frustration1
					new_frustration1 = old_fr/count
				print "new_frustration==>" + str(new_frustration)
			
				print "new_frustration1-==>" + str(new_frustration1)
				# print 
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
					else:
						# pass
						alert_flag = 0
						hold = 2
						end_time = start_time + datetime.timedelta(minutes=2)
						print "keep the level"
					# #lower the level
					# f = open(path)
					# ll=f.read()
					# f.close()
					# ll = int(ll)
					# if l > 1:
					# 	f = open(path,"w")
					# 	f.write(l-1)
					# 	f.close()
				else: #increase in frustration
					alert_flag = 1
					print "Increasing the level"

					# sys.exit(1)
		# 			#increase the level
					# lp = open(path,"r+").read()
					f = open(path)
					lp=f.read()
					f.close()
					print lp
					lp = int(lp)
					if lp > 1:
						fp = open(path,"w")
						fp.write(str(lp+1))
						fp.close()
					# sys.exit(1)
			else:
				# print "here"
				new_frustration = old_fr/count
				f = open(path)
				li=f.read()
				f.close()
				print li
				li = int(li)
				if li == 1:
					# print "over writing"
					# print li+1
					fi = open(path,"w")
					fi.write(str(li+1))
					fi.close()
					
			level_count = level_count+1
			count = 0
