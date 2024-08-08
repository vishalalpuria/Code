# Write a Python program that finds the first divisor (other than 1) of a given number using a for-else loop. If the number has no divisors, the program should print "Prime".

n = int(input("Enter Number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"The first divisor is {i}")
        break
else:
    print("Number is prime")
