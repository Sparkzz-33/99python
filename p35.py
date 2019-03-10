import math
k = (int)(input("Enter the number : "))
def generate(k):
	i = 2
	while i <= (k/2):
		if k % i == 0:
			j = 2
			flag = 0
			while j <= (i/2):
				if i % j == 0:
					flag = 1
					break
				j = j + 1
			if flag == 0:
				print(i)
		flag = 0
		i = i + 1
generate(k)