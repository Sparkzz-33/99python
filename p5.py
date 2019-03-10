l = []
i = 0
def reverse(l):
	i  = 0;
	while i < (len(l))/2 :
		temp = l[i]
		l[i] = l[-(i+1)]
		l[-(i+1)] = temp
		i = i + 1
i = 0
while i<10:
	l.append(i)
	i = i + 1
print(l)
reverse(l)
print(l)