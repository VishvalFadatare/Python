import array as arr
a=arr.array('i',[1,2,3,4])
print("Array",end= " ")
for i in range(0,4):
	print(a[i],end=" ")
print()

#Accessing
print("Accessing element:",a[0])

#Modifying
a[0]=8
print("Modifying element:",a[0])

#Addind element
print("Appending element:")
a.append(11)
for i in range(0,4):
	print(a[i],end=" ")
print()

#Removing 
print("Removing element:")
a.remove(2)
for i in range(0,4):
	print(a[i],end=" ")
print()

