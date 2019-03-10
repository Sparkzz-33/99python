#matrix multiplication
#for matrix 1
m = (int)(input('Enter the number of rows : ')
print('happy')
n = (int)(input('Enter the number of columns : ')
matrix = []
for i in range (0,m):
	matrix += [0]
for i in range (0,m):
	matrix[i] = [0]*n
for i in range (0,m):
	for j in range(0,n):
		print('entry in row: ',i+1,' column: ', j+1)
		matrix[i][j] = int(input())
#for matrix 2
m1 = (int)(input('Enter the number of rows : ')
n1 = (int) (input('Enter the number of columns: ')
for i in range (0,m1):
	matrix1 += [0]
for i in range (0,m1):
	matrix1[i] = [0]*n1
for i in range (0,m1):
	for j in range (0,n1):
		print('entry in row :', i+1,' column: ', j+1)
		matrix1[i][j] = int(input())
c = []
for i in range (0,m):
	c += [0]
for i in range (0,m):
	c[i] = [0]*n1
for i in range (0,m):
	for j in range (0,n1):
		k = 0
		l = 0
		sum = 0
		while(k<n):
			sum += matrix[i][k]*matrix1[l][j]
			l++
			k++
		c[i][j] = sum
print(c)		
