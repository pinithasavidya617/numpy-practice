# Matrix multiplication
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Rule - (row of A) × (column of B)
# (1×5) + (2×7) = 5 + 14 = 19
# (1×6) + (2×8) = 6 + 16 = 22
# (3×5) + (4×7) = 15 + 28 = 43
# (3×6) + (4×8) = 18 + 32 = 50
# [[19, 22],
#  [43, 50]]

A @ B            # matrix multiply (preferred syntax)
np.dot(A, B)     # same thing

# Dot product of vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.dot(a, b)     # 32  (1*4 + 2*5 + 3*6)

A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[1,2],
              [3,4],
              [5,6]])

print(A @ B)