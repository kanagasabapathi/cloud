import socket
import os
import select
import sys

def prompt():
   sys.stdout.write('<You> ')
   sys.stdout.flush()

HOST = '127.0.0.1'
PORT = 8096


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

print 'Connected to remote host. Start sending messages'
prompt()

while  1:
    

    socket_list = [sys.stdin, s]

    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for sock in read_sockets:
        if sock == s:
            data = sock.recv(4096)
            if not data:
                print '\nDisconnected from chat server'
                sys.exit()
            else:
                sys.stdout.write(data)
                prompt()
        else:
	    p,q1,q2,r1,r2,b1,b2 = map(int,raw_input("Enter p,q1,q2,r1,r2,b1,b2  ").split())
  	    c1=p*q1+2*r1+b1
  	    c2=p*q2+2*r2+b2
	    print "c1 = ",c1
	    print "c2 = ",c2
	    #msg = sys.stdin.readline()
	    
            s.send(str(c1)+":"+str(c2))
	    #s.send(str(c2))

            sum1=(c1+c2)%p
	    multiplication=(c1*c2)%p
            


	  #  client_socket.send(str(sm))


	    print"Decrypt=",sum1
	    if sum1%2==0:
	   	         b=0
	    else:
	  	         b=1

	    
            print"b=",b,"value is got for addition"
	    if b==0:
	                 print "b value is even"
	    else:
	                 print "b value is odd"
 	        
	    if multiplication%2==0:
	                 b=0
	    else:
			 b=1
	    print"b=",b,"value is got for multiplication"
	    
	    if b==0:
                         print "b value is even"
            else:
                         print "b value is odd"
	    
	  
            prompt()
