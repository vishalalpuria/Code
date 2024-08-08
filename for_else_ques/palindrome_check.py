# Write a Python program that checks whether a given string is a palindrome using a for-else loop.

str1 = input("Enter the string: ")
str1 = str1.lower()
l = len(str1)
lst = l - 1
for i in range(0, l // 2): # To go only the half string 
    if str1[i] != str1[lst]:
        print("Not palindrome")
        break
    lst -= 1
else:
    print("Palindrome")
