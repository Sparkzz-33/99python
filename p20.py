l = []
i = 0
while i < 10:
	l.append(i)
	i = i + 1
k = (int)(input("enter the position of number to be deleted : "))
print(l)
del l[k-1]
print(l)