import numpy as np

# Initialize a 3x3 2D array
array_3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

mean_array = np.mean(array_3x3,axis=1).reshape(3, 1)
print("Original 3x3 array:")
print(array_3x3)
print("\n3x1 array with mean of corresponding rows:")
print(mean_array)