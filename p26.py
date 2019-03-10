import random
l = []
m = 0
while m < 10:
	i = random.randint(1,100)
	l.append(i)
	m = m + 1
k = (int)(input("enter the count of numbers you want : "))
def generate(l,k):
	if k <= 0:
		yield []
		return
	for i in range (len(l)):
		number = l[i:i+1]
		for one in combination(k-1, l[i+1:]):
			yield number + one
generate(l,k)