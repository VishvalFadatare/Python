f=frozenset([1,2,3,4])
f1=frozenset([4,5,6,7,8])
print(f)

# 1. copy()
set_copy = f.copy()
print("1. copy() of set1:", set_copy)

# 2. difference(set)
difference = f.difference(f1)
print("2. difference between f and f1:", difference)

# 3. intersection(set)
intersection = f.intersection(f1)
print("3. intersection of f and f1:", intersection)

# 4. isdisjoint(set)
is_disjoint = f.isdisjoint(f1)
print("4. isdisjoint between set1 and set2:", is_disjoint)

# 5. issubset(set)
is_subset = f.issubset({1, 2, 3, 4, 5, 6, 7, 8})
print("5. issubset check for set1:", is_subset)

# 6. issuperset(set)
is_superset = f.issuperset({1, 2, 3})
print("6. issuperset check for set1:", is_superset)

# 7. symmetric_difference(set)
symmetric_diff = f.symmetric_difference(f1)
print("7. symmetric_difference between set1 and set2:", symmetric_diff)

# 8. union(set)
union_set = f.union(f1)
print("8. union of set1 and set2:", union_set)
