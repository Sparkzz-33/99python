l = []
i = 0
while i < 12:
	l.append(i)
	i = i + 1
l.append(11)
l.append(11)
l.append(12)
l.append(12)

def consecutive(l):
	i = 0
	n = len(l)
	while i<n-1:
		if l[i] == l[i+1]:
			del l[i]
			i = i - 1
			n = n-1
		i = i + 1
	
print(l)
consecutive(l)
print(l)