a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
#a,b=int(input("Enter numbers:")).split()

print("assignment operator:")
a+=b
print("a+=b:",a)
a-=b
print("a-=b:",a)
a*=b
print("a*=b:",a)
a/=b
print("a/=b:",a)

print("Comparison Operator:")
print(a>b)
print(a==b)
print(a<b)
print(a<=b)
print(a>=b)
print(a!=b)

print("Logical Operator:")
print(a<b and a==b)
print(a>b and a!=b)
print(a>b or a==b)
print(not(a>b or a==b))

print("Bitwise operator:")
print(6&3)
print(6|3)
print(6<<3)
print(6>>3)
print(6^3)
print(~3)

print("Identity Operator:")
x=13
y=13
z=2
print(x is y)
print(x is z)
print(x is not y)





