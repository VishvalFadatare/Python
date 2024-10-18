a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

x=lambda a,b:a+b
print("Addition:",x(a,b))

y=lambda a,b:a-b
print("Subtraction:",y(a,b))

z=lambda a,b:a*b
print("Multiplication:",z(a,b))

m=lambda a,b:a/b
print("Division:",m(a,b))

n=lambda a,b:a%b
print("Modulus:",n(a,b))
