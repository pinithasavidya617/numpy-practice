import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stack (row-wise)
np.vstack([a, b])
# [[1, 2, 3],
#  [4, 5, 6]]

# Horizontal stack (column-wise)
np.hstack([a, b])
# [1, 2, 3, 4, 5, 6]

# Column stack (adds as columns)
np.column_stack([a, b])
# [[1, 4],
#  [2, 5],
#  [3, 6]]

# General concatenation
np.concatenate([a, b], axis=0)  # same as hstack for 1D

c = np.array([1,2,3])
d = np.array([10,20,30])

print(np.vstack([c,d]))
print(np.column_stack([c,d]))