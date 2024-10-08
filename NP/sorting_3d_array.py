import numpy as np

# Create a 2D array of 9 names
arr = np.array([
    ["Charlie", "Alice", "Bob"],
    ["Frank", "David", "Eve"],
    ["Ivan", "Grace", "Heidi"]
])
arr = arr.flatten()


n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

arr = arr.reshape(3, 3)
print(arr)



