import numpy as np

# Zeros and ones
np.zeros((3, 4))          # 3×4 matrix of zeros
np.ones((2, 3))           # 2×3 matrix of ones
np.full((3, 3), 7)        # 3×3 matrix filled with 7

# Identity matrix
np.eye(4)                 # 4×4 identity matrix

# Empty (uninitialized — fast but contains garbage values)
np.empty((2, 3))

# Range
np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)      # [0.0, 0.25, 0.5, 0.75, 1.0]  (5 evenly spaced)
np.logspace(0, 3, 4)      # [1, 10, 100, 1000]  (log scale)

print(np.zeros((2,2)))
print(np.linspace(1, 10, 5))
print(np.arange(1, 10, 3))