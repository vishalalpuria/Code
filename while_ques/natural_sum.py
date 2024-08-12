# Write a Python program using a while loop to find the sum of the first n natural numbers.

n = int(input("Enter the number: "))
s = 0
i = 0
while i<n:
    s += i
    i+=1
print("The sum is",s)


