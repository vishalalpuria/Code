# Write a while loop that calculates the sum of the squares of integers from 1 to n, where n is provided by the user.

n = int(input("Enter a number: "))
sum_square = 0
i = 1

while i <= n:
    sum_square += i ** 2
    i += 1

print("Sum : ", sum_square)
