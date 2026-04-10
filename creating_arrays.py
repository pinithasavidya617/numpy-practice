import numpy as np
# 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)  # [1 2 3 4 5]

# 2D array (matrix)
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b)
# [[1 2 3]
#  [4 5 6]]

# 3D array
c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print(c.shape)  # (2, 2, 2)