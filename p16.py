l = []
i = 0
while i < 10:
	l.append(i)
	i = i + 1
k = (int)(input())
def removen(l,k):
	i = 0
	m = 0
	while i < len(l):
		if (i+1-m) % k == 0:
			del l[i]
			m = m + 1
		i = i + 1
print(l)
removen(l, k)
print(l)
