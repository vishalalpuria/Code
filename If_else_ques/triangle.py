# Determine if a triangle is valid based on the lengths of its sides.

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


s1 = int(input("Enter the side 1: "))
s2 = int(input("Enter the side 2: "))
s3 = int(input("Enter the side 3: "))

if is_triangle(s1, s2, s3):
    print("It is a valid triangle.")
else:
    print("It is not a valid triangle.")