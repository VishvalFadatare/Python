a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))

if(a<b & a<c):
	print(a,"is smallest number")
elif(b<c & b<a):
	print(b,"is smallest number")
else:
	print(c,"is smallest number")

