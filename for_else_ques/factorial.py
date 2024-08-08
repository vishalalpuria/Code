# Write a Python program to compute the factorial of a given number using a for loop.

n = int(input("Enter the number : "))
f = 1

for i in range(1, n + 1):
    f *= i
print("Factorial is", f)
