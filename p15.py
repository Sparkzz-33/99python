l = []
i = 0
while i < 10:
	l.append(i)
	i = i + 1
print(l)
k = (int)(input("enter the number of duplicates you want : "))
def duplicate(l,k):
	i = 0
	n = len(l)
	while i < n:
		m = 0
		while m < k:
			l.insert(i+1, l[i])
			i = i + 1
			m = m + 1
			n = n + 1
		i = i + 1
duplicate(l,k)
print(l)