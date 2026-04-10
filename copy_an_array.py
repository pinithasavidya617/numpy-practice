# Copy an array
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

b = np.copy(a)
b = a.copy()

# Create from a function
np.fromfunction(lambda i, j: i + j, (3, 3))

# [0+0, 0+1, 0+2] → [0,1,2]
# [1+0, 1+1, 1+2] → [1,2,3]
# [2+0, 2+1, 2+2] → [2,3,4]

print(np.fromfunction(lambda i, j: i - j, (3, 3)))