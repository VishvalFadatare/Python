# Sum of digit
n=int(input("Enter number"))
sum=0
rem=0
while n>0:
	rem=n%10
	sum=sum+rem
	n=n//10
	print(rem)
