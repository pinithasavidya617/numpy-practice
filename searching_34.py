import numpy as np

a = np.array([10, 20, 30, 40, 50])

# Find index of value
np.searchsorted(a, 25)    # 2 (where 25 would be inserted)

# Find indices of non-zero elements
b = np.array([0, 5, 0, 3, 0, 7])
np.nonzero(b)              # (array([1, 3, 5]),)
np.flatnonzero(b)          # [1, 3, 5]

# Unique values
c = np.array([3, 1, 2, 1, 3, 2, 3])
np.unique(c)                        # [1, 2, 3]
np.unique(c, return_counts=True)    # ([1, 2, 3], [2, 2, 3])
# | Value | Count |
# | ----- | ----- |
# | 1     | 2     |
# | 2     | 2     |
# | 3     | 3     |

np.unique(c, return_index=True)
# First appears at index# ([1, 2, 3], [1, 2, 0])
# | Value | First appears at index |
# | ----- | ---------------------- |
# | 1     | 1                      |
# | 2     | 2                      |
# | 3     | 0                      |

a = np.array([2, 4, 6, 8])

print(np.searchsorted(a, 5))

b = np.array([0,1,0,2,3])
print(np.flatnonzero(b))

c = np.array([1,1,2,3,3,3])
print(np.unique(c, return_counts=True))