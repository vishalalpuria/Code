# Write a Python program that reverses a given string using a for loop.

str1 = input("Enter the string: ")

for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")