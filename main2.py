p = int(input("Enter the principle: "))
r = int(input("Enter the Rate: "))
n = int(input("Enter the Years: "))

ci = p*(1+(r/100))**n
print(ci)


a = int(input())
b = int(input())

# print(a if a > b else  b)

if(a>b):
    print(a)
else:
    print(b)
