# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. add(element)
set1.add(6)
print("1. add(6) to set1:", set1)

# 2. clear()
set_copy = set1.copy()  # Creating a copy to clear
set_copy.clear()
print("2. clear() set_copy:", set_copy)

# 3. copy()
set_copy = set1.copy()
print("3. copy() of set1:", set_copy)

# 4. difference(set)
difference = set1.difference(set2)
print("4. difference between set1 and set2:", difference)

# 5. difference_update(set)
set1.difference_update(set2)
print("5. difference_update set1 with set2:", set1)

# Resetting set1 for further operations
set1 = {1, 2, 3, 4, 5}

# 6. discard(element)
set1.discard(5)
print("6. discard(5) from set1:", set1)

# 7. intersection(set)
intersection = set1.intersection(set2)
print("7. intersection of set1 and set2:", intersection)

# 8. intersection_update(set)
set1.intersection_update(set2)
print("8. intersection_update set1 with set2:", set1)

# Resetting set1 for further operations
set1 = {1, 2, 3, 4, 5}

# 9. isdisjoint(set)
is_disjoint = set1.isdisjoint(set2)
print("9. isdisjoint between set1 and set2:", is_disjoint)

# 10. issubset(set)
is_subset = set1.issubset({1, 2, 3, 4, 5, 6, 7, 8})
print("10. issubset check for set1:", is_subset)

# 11. issuperset(set)
is_superset = set1.issuperset({1, 2, 3})
print("11. issuperset check for set1:", is_superset)

# 12. pop()
popped_element = set1.pop()
print("12. pop() element from set1:", popped_element, "->", set1)

# 13. remove(element)
set1.remove(2)
print("13. remove(2) from set1:", set1)

# 14. symmetric_difference(set)
symmetric_diff = set1.symmetric_difference(set2)
print("14. symmetric_difference between set1 and set2:", symmetric_diff)

# 15. symmetric_difference_update(set)
set1.symmetric_difference_update(set2)
print("15. symmetric_difference_update set1 with set2:", set1)

# Resetting set1 for further operations
set1 = {1, 2, 3, 4, 5}

# 16. union(set)
union_set = set1.union(set2)
print("16. union of set1 and set2:", union_set)

# 17. update(set)
set1.update(set2)
print("17. update set1 with set2:", set1)
