import math
m = (int)(input())
n = (int)(input())
def generate(m,n):
	i = m
	while i <= n:
		j = 2
		flag = 0
		while j <= math.sqrt(i):
			if i % j == 0:
				flag = 1
				break
			j = j + 1
		if flag == 0:
			print(i, end = ' ')
		i = i + 1
generate(m,n)