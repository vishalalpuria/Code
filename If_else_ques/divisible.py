# Determine if a number is divisible by both 3 and 5

i = int(input("Enter the number: "))

if(i%3 ==0 and i%5==0):
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 or 5, or both")
