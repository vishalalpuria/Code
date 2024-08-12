#Program for fibonacci

i = int(input("Enter n: "))

if i <= 0:
    print("Invalid")
elif i == 1:
    print(0)
else:
    first = 0
    second = 1
    print(first, second, end=" ")
    for _ in range(2, i): # _ means placeholder, means loop variable is not requierd in the code
        next_fib = first + second
        print(next_fib, end=" ")
        first = second
        second = next_fib

