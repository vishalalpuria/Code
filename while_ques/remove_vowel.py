# Write a while loop that takes a string and removes all the vowels from it. Print the resulting string.

str1 = input("Enter a string: ")
result = ""

index = 0
while index < len(str1):
    if str1[index] not in "aeiouAEIOU":
        result += str1[index]
    index += 1

print("Result:", result)