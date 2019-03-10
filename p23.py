import random
l = []
i = 10
while i < 20:
	l.append(i)
	i = i + 1
print(l)
k = (int)(input("enter the number of times to generate : "))
def generate(l,k):
	for j in range(k):
		i = random.randint(0, len(l)-1)
		print(l[i])
generate(l, k)