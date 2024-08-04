# Check if a given string is a palindrome.
str1 = input("Enter the String: ")
str1 = str1.lower()
if(str1 == str1[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")


