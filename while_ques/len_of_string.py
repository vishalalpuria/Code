# Write a while loop to find the length of a string without using the len() function.

str1 = "Hello, World!"
length = 0

while str1[length:]:
    length += 1

print("Length :", length)

