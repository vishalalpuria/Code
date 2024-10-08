import numpy as np 
arr = np.array([1,4,5,7,2,3])

print(arr)
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j + 1]:
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp

print(arr)
