n=int(input("Enter Year:"))

if((n%4)==0 or ((n%100)==0 and (n%400)==0)):
	print(n,"is leap year")
else:
	print(n,"is not leap year")
