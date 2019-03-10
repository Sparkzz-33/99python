l = []
i = 0
while i < 10:
	l.append(i)
	i = i + 1
print(l)
def duplicate(l):
	i = 0
	n = len(l)
	while i < n:
		l.insert(i+1, l[i])
		i = i + 2
		n = n + 1
duplicate(l)
print(l)
