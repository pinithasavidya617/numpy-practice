import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

a.T
# [[1, 4],
#  [2, 5],
#  [3, 6]]

# For higher dimensions
np.transpose(a, axes=(1, 0))  # same as .T for 2D

#(rows, cols) → (cols, rows)

# [1 2 3]
# [4 5 6]
#
# [1 4]
# [2 5]
# [3 6]

b = np.array([[1,2],[3,4],[5,6]])

print(b.shape)
print(b.T.shape)