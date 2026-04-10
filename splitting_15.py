import numpy as np

a = np.arange(12).reshape(3, 4)

# Split into 2 along columns
np.hsplit(a, 2)    # two 3×2 arrays

# Split into 3 along rows
np.vsplit(a, 3)    # three 1×4 arrays

# Split at specific indices
np.split(a, [1, 3], axis=1)  # split at col 1 and col 3

b = np.arange(16).reshape(4,4)

print(np.hsplit(b, 2))
print(np.vsplit(b, 2))