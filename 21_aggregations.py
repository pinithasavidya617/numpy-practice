import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Global aggregations
np.sum(a)       # 45
np.mean(a)      # 5.0
np.std(a)       # 2.582
np.var(a)       # 6.667
np.min(a)       # 1
np.max(a)       # 9
np.median(a)    # 5.0

# Along an axis
np.sum(a, axis=0)    # [12, 15, 18]  (column sums)
np.sum(a, axis=1)    # [6, 15, 24]   (row sums)
np.mean(a, axis=0)   # [4, 5, 6]     (column means)
np.mean(a, axis=1)   # [2, 5, 8]     (row means)

a = np.array([[2,4,6],
              [1,3,5]])

print(np.sum(a, axis=0))
print(np.sum(a, axis=1))