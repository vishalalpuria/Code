# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a 4x4 matrix filled with zeros using np.zeros()
x = np.zeros((4, 4))
print(x)
# Setting elements in alternate rows and columns to 1
# Setting elements in even rows (0-based indexing) and odd columns to 1
x[::2, 1::2] = 1

# Setting elements in odd rows and even columns to 1
x[1::2, ::2] = 1

# Printing the modified matrix 'x'
print(x)