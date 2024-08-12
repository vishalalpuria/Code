# Write a Python program to calculate the factorial of a given number using a while loop.

n = int(input("Enter the number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print(f"Factorial of {n} is {fact}")

