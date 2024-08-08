# Write a Python program that finds the first vowel in a string using a for-else loop. If no vowel is found, print "No vowels".

str1 = input("Enter the String: ")
str1 = str1.lower()
for i in str1:
    if 'a' == i or 'e' == i or 'i' == i or 'o' == i or 'u' == i:
        print(f"Firet vowel is {i}")
        break
else:
    print("No vowel found in string")