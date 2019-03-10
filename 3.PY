#CALCULATOR
def	calculator(n,a,b):
	if(n==1):
		return a+b
	elif(n==2):
		return a-b
	elif(n==3):
		return a*b
	elif(n==4):
		return a/b
	elif(n==5):
		return a%b
	print('Command does not exist')
	return -1
a = (int)(input('Enter the first number : '))
b = (int)(input('Enter the second number : '))
print(' ')
print('1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for modulus')
n = (int)(input('Enter your choice : '))
print('The answer is : ')
print(calculator(n,a,b))

		