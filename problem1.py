#1.Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
add = lambda x: x + 25

number = int(input("Enter a number: "))

result = add(number)

print(f"Result is {result}")
