# print number is prime or not
n=int(input("Enter number:"))
flag=0
for i in range(2,n):
	if(n%i==0):
		flag=1

if(flag==1):
	print("Not a prime number.....")
else:
	print("Prime Number....")
		

	
