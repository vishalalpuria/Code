# Check if a given year is a leap year.
yr = int(input("Enter the Numeber: "))

if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")
