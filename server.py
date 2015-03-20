import socket
import os
import select
import sys

def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print 'Failed to create socket'
    sys.exit()

PORT = 8096	
HOST = '0.0.0.0'
RECV_BUFFER = 4095

server_socket.bind((HOST, PORT))
server_socket.listen(10)

input = [server_socket, sys.stdin]

print 'Chat Program'
prompt()

while 1:

    inputready, outputready, exceptready = select.select(input,[],[])

    for sock in inputready:

        if sock == server_socket:
            client, address = server_socket.accept()
            input.append(client)
        elif sock == sys.stdin:
            data = sock.readline()
            for s in input:
               if s not in(server_socket, sys.stdin):
                   s.send(data)
        else:
            data1 = sock.recv(int (RECV_BUFFER))
	   # data2 = sock.recv(int (RECV_BUFFER))
            if data1:
		#if data2:
		#	b=data1+data2
		#	print b
		#	if b%2==0:
		#		sys.stdout.write("b=0")
		#	else:
				#sys.stdout.write("b=1")
		c1=int(data1.split(":")[0])#int(data1[0:2])
		c2=int(data1.split(":")[1])#int(data1[3:5])
                print "c1=",c1
                print "c2=",c2
		#b=c1+c2;
                #d=(c1*c2)
		#if b%2==0:
		#	sys.stdout.write("b=0")
		#else:
		#	sys.stdout.write("b=1")
			#data +=data

                #if d%2=0
            else:
                msg = sys.stdin.readline()
                server_socket.send('\r<Server>: ' + msg)
                prompt()
	
	
		


server_socket.close()
