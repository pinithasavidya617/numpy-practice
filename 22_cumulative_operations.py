import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(np.cumsum(a, axis=0))

# [1, 4, 7] → cumulative:
# 1
# 1+4 = 5
# 5+7 = 12

print(np.cumprod(a, axis=1))

# [1, 2, 3] → cumulative:
# 1
# 1×2 = 2
# 2×3 = 6

print(np.cumsum(a, axis=1))
print(np.cumprod(a, axis=0))
