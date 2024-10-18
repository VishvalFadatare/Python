# Creating a dictionary
my_dict = {
    "name": "Vishval",
    "age": 20,
    "city": "Kolhapur"
}

keys = my_dict.keys()
print("1. keys():", keys)

values = my_dict.values()
print("2. values():", values)

items = my_dict.items()
print("3. items():", items)

age = my_dict.get("age", "Not Found")
print("4. get('age'):", age)

my_dict.update({"age": 19, "email": "vishval@example.com"})
print("5. update():", my_dict)

city = my_dict.pop("city", "Not Found")
print("6. pop('city'):", city)
print("   After pop():", my_dict)

last_item = my_dict.popitem()
print("7. popitem():", last_item)
print("   After popitem():", my_dict)

country = my_dict.setdefault("country", "USA")
print("8. setdefault('country', 'USA'):", country)
print("   After setdefault():", my_dict)

my_dict.clear()
print("9. clear():", my_dict)

original_dict = {"name": "Bob", "age": 30}
copy_dict = original_dict.copy()
print("10. copy() of original_dict:", copy_dict)

