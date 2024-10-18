#String is palindrome or not
s=input("Enter String:")
flag=0
i=0
j=len(s)-1

while(i<=j):
	if(s[i]!=s[j]):
		flag=flag+1
	i=i+1
	j=j-1

if(flag==0):
	print("Prindrome....")
else:
	print("Not Palindrome...")



