l = []
i = 0
while i<10:
	l.append(i)
	i = i + 1
k = (int)(input())
print(l)
def part(l,k):
	p = []
	p = l[k::]
	l = l[:k]
	print(l)
	print(p)
part(l,k)