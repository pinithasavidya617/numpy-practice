import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

np.argmin(a)        # 0   (index of min in flattened array)
np.argmax(a)        # 8   (index of max in flattened array)
np.argmin(a, axis=0)  # [0, 0, 0]  (row index of min per column)
np.argmax(a, axis=1)  # [2, 2, 2]  (col index of max per row)

# Unravel flat index to multi-dim index
# convert flat index to 2D
np.unravel_index(np.argmax(a), a.shape)  # (2, 2)

a = np.array([[3, 1, 9],
              [8, 2, 5]])

print(np.argmax(a))
print(np.unravel_index(np.argmax(a), a.shape))