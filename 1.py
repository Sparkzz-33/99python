#print('hello welcome to python')
import math
def isprime(n):
	i = 1
	flag = 0
	for i in range(2,(int)(math.sqrt(n))):
		if(n%i==0):
			flag = 1
			break
	if(flag==1):
		print('Not prime')
	else: 
		print('Prime')
n = (int)(input("enter the number: "))
isprime(n)