s = (str)(input())
def palindrome(s):
	i = 0
	n = len(s)
	flag = 0
	while i < (n/2) :
		if s[i].lower() != s[-(i+1)].lower():
			flag = 1
			break
		i = i + 1
	if flag == 1:
		print("Not palindrome...")
		return
	else:	
		print("palindrome...")
		return
palindrome(s)