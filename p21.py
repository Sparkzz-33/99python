l = []
i = 0
while i<10:
	l.append(i)
	i = i + 1
print(l)
k = (int)(input("Enter the value to be inserted : "))
pos = (int)(input("Enter the index at which to insert : "))
l.insert(pos, k-1)
print(l)