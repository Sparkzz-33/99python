l = []
m = (int)(input("enter the lower bound of the range : "))
n = (int)(input("enter the upper bound of the range : "))
def addition(l,m,n):
	i = m
	while i <= n:
		l.append(i)
		i = i + 1
print(l)
addition(l,m,n)
print(l)