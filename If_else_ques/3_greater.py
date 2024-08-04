# Find the largest of three numbers.
a = int(input("Enter the Number 1: "))
b = int(input("Enter the Number 2: "))
c = int(input("Enter the Number 2: "))

if a > b and a > c:
    print(a, "is greater")
elif b > c and b > a:
    print(b, "is greater")
else:
    print(c, "is greater")
