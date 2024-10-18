#Arithmatic operation using Function

#Addition
def add(a,b):
	result=a+b
	return result

def sub(a,b):
	result=a-b
	return result

def mul(a,b):
	result=a*b
	return result

def div(a,b):
	result=a/b
	return result

def mod(a,b):
	result=a%b
	return result

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

s1=add(a,b)
print("Addition:",s1)

s2=sub(a,b)
print("Subtraction:",s2)

s3=mul(a,b)
print("Multiplication:",s3)

s4=div(a,b)
print("Division:",s4)

s5=mod(a,b)
print("Modulus:",s5)		
