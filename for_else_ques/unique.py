# Write a Python program to check if all characters in a string are unique using a for-else loop.

str1 = input("Enter String: ").lower()
lst1 = []

for i in str1:
    if i in lst1:
        print("Not every character is unique")
        break
    lst1.append(i)
else:
    print("Every character is unique in string")

