# Write a Python program that sums a list of integers but skips negative numbers

lst1 = [-5,2,-6,4,2,-4,-9,8,6]

s = 0
for i in lst1:
    if(i >= 0):
        s += i
print(f"The sum of non negative numbers is {s}")