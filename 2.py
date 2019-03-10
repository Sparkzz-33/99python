#tower of hanoii
A = 'A'
B = 'B'
C = 'C'
n = (int)(input('Enter the number of discs: '))
def towerofhanoii(n,fro,to,aux):
	s = "Move disc "
	t = " from rod "
	u = " to rod "
	if(n==1):
		print('{}{}{}{}{}{}'.format(s,n,t,fro,u,to))
		return
	towerofhanoii(n-1, fro,aux,to)
	print('{}{}{}{}{}{}'.format(s,n,t,fro,u,to))
	towerofhanoii(n-1, aux, to, fro)
towerofhanoii(n,A,B,C)