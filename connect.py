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
	data = s.recv(500)
	engagement = 0.5
	excitementlongterm = 0.5
	excitementshortterm = 0.5
	frustration = 0.5
	meditation = 0.5
	created = datetime.now()
	db.session.add(Affectiv(engagement, excitementlongterm,excitementshortterm, frustration, meditation, created=created))
	db.session.commit()
	# print data
	# print '\n'