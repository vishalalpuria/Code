import numpy as np 

list1 = []
cnt = 0
n = int(input("Enter n: "))
for i in range(n):
    list1.append(int(input("Enter no. : ")))

arr = np.array(list1)
for i in arr:
    if i == 0:
        cnt+=1
print("No of 0 are",cnt)
