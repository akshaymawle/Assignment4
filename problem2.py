#2.Write a Python program to triple all numbers of a given list of integers. Use Python map.

list1 = [1, 2, 3, 4, 5, 6, 7]

result = list(map(lambda x: x * 3, list1))

print(f"Original List is {list1}")
print(f"Tripled List is {result}")
