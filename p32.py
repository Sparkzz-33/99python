m = (int)(input())
n = (int)(input())
def gcd(m, n):
	if n==0:
		return m
	return gcd(n, m%n)
k = gcd(m,n)
print(k)