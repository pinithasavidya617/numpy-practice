import numpy as np

a = np.arange(12)  # [0, 1, 2, ..., 11]

# Reshape to 3×4
b = a.reshape(3, 4)
# [[ 0,  1,  2,  3],
#  [ 4,  5,  6,  7],
#  [ 8,  9, 10, 11]]

# -1 ->>> “Fix one dimension → NumPy fills the other”
# Use -1 to auto-calculate one dimension
c = a.reshape(2, -1)   # 2×6
d = a.reshape(-1, 3)   # 4×3

# Flatten back to 1D
b.ravel()    # returns a view (fast)
b.flatten()  # returns a copy (safe)

b = np.arange(20)

print(b.reshape(4, -1))   # 5 columns
print(b.reshape(-1, 5))   # 4 rows