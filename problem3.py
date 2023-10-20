#3. Write a Python program to square the elements of a list using map() function.

list2 = [4, 5, 2, 9]

output = list(map(lambda x: x**2, list2))

print(f"Original List is {list2}")
print(f"Squared List is {output}")
