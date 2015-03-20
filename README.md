# cloud

the following function is a fully homomorphic encryption in python 


fullhome.py

p,q1,q2,r1,r2,b1,b2 = map(int,raw_input("Enter p,q1,q2,r1,r2,b1,b2  ").split())
c1=p*q1+2*r1+b1
c2=p*q2+2*r2+b2

print "c1 = ",c1,"c2 = ",c2

ad=(c1+c2)%p

if ad%2==0:
	b=0
else:
	b=1

print "b = ",b



so i try this program in server and client process
