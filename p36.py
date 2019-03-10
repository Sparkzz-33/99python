import math
k = (int)(input())
l = []
def factorisation(k, l):
	while(k % 2 == 0):
		k = k / 2
		l.append(2)
	for i in range(3, (int)(math.sqrt(k))+1, 2):
		while k % i == 0:
			k = k / i
			l.append(i)
	if k > 2:
		l.append((int)(k))
factorisation(k, l)
print(l)