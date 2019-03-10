l = []
i = 0
while i < 10:
	l.append(i)
	i = i + 1
k = (int)(input())
def rotate(k,l):
	itr = 0
	while itr < k:
		i = l[0]
		j = 0
		while j < len(l) - 1:
			l[j] = l[j+1]
			j = j + 1
		l[j] = i
		itr = itr + 1
print(l)
rotate(k,l)
print(l)