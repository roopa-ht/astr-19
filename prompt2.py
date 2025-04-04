'''
Write a Python program that prints the sum of two floating point numbers
The difference between two integers
The product of a floating point number and an integer
In each case, have the program print out the data type of the resulting answer.
'''

a = 40.0
b = 25.0

print("a + b = ", a+b)
print(type(a + b))

print("a - b = ", int(a) - int(b))
print(type(int(a) - int(b)))

print("a * b = ", a * int(b))
print(type((a) * int(b)))