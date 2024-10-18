n=int(input("Enter number:"))
a=97
for i in range(0,n):
	for j in range(a,a+i):
		print(chr(j),end=" ")
	print()
