
#Program for fibonacci
i = int(input())

first = 0
second = 1
t = 0
if i <= 0:
    print("Invalid")
elif i == 1:
    print(first)
else:
    while(t <= i/2):
        print(first,second,end = " ")
        t+=1
        first = first + second
        second = second + first

