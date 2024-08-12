# Write a while loop that converts a binary number (given as a string) to its decimal equivalent.

n = input("Enter a binary number: ")
dec_no = 0
power = 0 # to iterate through the last 
while n != "":
    last_digit = int(n[-1])
    dec_no += last_digit * (2 ** power)
    n = n[:-1]
    power += 1

print("Decimal equivalent:", dec_no)

