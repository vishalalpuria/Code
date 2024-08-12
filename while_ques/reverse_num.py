# Write a Python program that uses a while loop to reverse a given integer number.

n = int(input("Enter the number: "))

rev_num = 0

while n > 0:
    tmp = int(n % 10)
    rev_num = int((rev_num * 10) + tmp)
    n = int(n / 10)

print("Reverse number is", rev_num)
