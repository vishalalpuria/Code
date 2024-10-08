import numpy as np

# Create a square matrix
arr = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
sum1 = 0
# Print the diagonal elements
diagonal_elements = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i == j) or i+j == len(arr) - 1 :
            diagonal_elements.append(int(arr[i][j]))
            sum1 += int(arr[i][j])
        
print("Diagonal elements:", diagonal_elements)
print(sum1)