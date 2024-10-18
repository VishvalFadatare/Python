# String for demonstration
sample_str = "Hello, Python!"

# 1. capitalize()
print("1. capitalize():", sample_str.capitalize())

# 2. casefold()
print("2. casefold():", sample_str.casefold())

# 3. center(width, fillchar)
print("3. center(50, '*'):", sample_str.center(30, '*'))

# 4. count(substring, start, end)
print("4. count('o'):", sample_str.count('o'))

# 5. encode(encoding, errors)
print("5. encode('utf-8'):", sample_str.encode('utf-8'))

# 6. endswith(suffix, start, end)
print("6. endswith('ing.'):", sample_str.endswith('ing.'))

# 7. expandtabs(tabsize)
sample_str_with_tabs = "Hello\tWorld"
print("7. expandtabs(4):", sample_str_with_tabs.expandtabs(4))

# 8. find(substring, start, end)
print("8. find('Python'):", sample_str.find('Python'))

# 9. format(*args, **kwargs)
print("9. format():", "Hello, {}!".format("World"))

# 10. format_map(mapping)
print("10. format_map():", "{name} is {age} years old.".format_map({'name': 'John', 'age': 25}))

# 11. index(substring, start, end)
print("11. index('Python'):", sample_str.index('Python'))

# 12. isalnum()
print("12. isalnum():", "Python3".isalnum())

# 13. isalpha()
print("13. isalpha():", "Python".isalpha())

# 14. isascii()
#print("14. isascii():", "Python3!".isascii())

# 15. isdecimal()
print("15. isdecimal():", "12345".isdecimal())

# 16. isdigit()
print("16. isdigit():", "12345".isdigit())

# 17. isidentifier()
print("17. isidentifier():", "Python3".isidentifier())

# 18. islower()
print("18. islower():", "python".islower())

# 19. isnumeric()
print("19. isnumeric():", "12345".isnumeric())

# 20. isprintable()
print("20. isprintable():", "Hello, World!".isprintable())

# 21. isspace()
print("21. isspace():", "   ".isspace())

# 22. istitle()
print("22. istitle():", "Hello, World!".istitle())

# 23. isupper()
print("23. isupper():", "HELLO".isupper())

# 24. join(iterable)
print("24. join():", "-".join(["Python", "is", "fun"]))

# 25. ljust(width, fillchar)
print("25. ljust(20, '*'):", "Python".ljust(20, '*'))

# 26. lower()
print("26. lower():", sample_str.lower())

# 27. lstrip(chars)
print("27. lstrip('He'):", sample_str.lstrip('He'))

# 28. partition(sep)
print("28. partition('Python'):", sample_str.partition('Python'))

# 29. replace(old, new, count)
print("29. replace('Python', 'Java'):", sample_str.replace('Python', 'Java'))

# 30. rfind(substring, start, end)
print("30. rfind('o'):", sample_str.rfind('o'))

# 31. rindex(substring, start, end)
print("31. rindex('o'):", sample_str.rindex('o'))

# 32. rjust(width, fillchar)
print("32. rjust(20, '*'):", "Python".rjust(20, '*'))
