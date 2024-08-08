# Write a Python program that calculates the sum of the digits of a given integer using a for loop.

i = int(input("Enter the number: "))
sum1 = 0

for i in str(i):
    sum1 += int(i)
print("Sum = ",sum1)