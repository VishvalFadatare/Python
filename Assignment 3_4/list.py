
# Creating a list
my_list = [1, 2, 3, 4, 5]

# 1. append(element)
my_list.append(6)
print("1. append(6):", my_list)

# 2. clear()
copy_list = my_list.copy()  # Creating a copy to clear
copy_list.clear()
print("2. clear() copy_list:", copy_list)

# 3. copy()
list_copy = my_list.copy()
print("3. copy() of my_list:", list_copy)

# 4. count(element)
count_of_3 = my_list.count(3)
print("4. count(3):", count_of_3)

# 5. extend(iterable)
my_list.extend([7, 8, 9])
print("5. extend([7, 8, 9]):", my_list)

# 6. index(element, start, end)
index_of_4 = my_list.index(4)
print("6. index(4):", index_of_4)

# 7. insert(index, element)
my_list.insert(0, 0)
print("7. insert(0, 0):", my_list)

# 8. pop(index)
popped_element = my_list.pop()
print("8. pop():", popped_element, "->", my_list)

# 9. remove(element)
my_list.remove(3)
print("9. remove(3):", my_list)

# 10. reverse()
my_list.reverse()
print("10. reverse():", my_list)

# 11. sort(key=None, reverse=False)
my_list.sort()
print("11. sort():", my_list)

# 12. _len_() (used implicitly by len())
length_of_list = len(my_list)
print("12. len(my_list):", length_of_list)

#13.list slicing 
print("Slicing:",my_list[1:5])
