import numpy as np

a = np.array([1, 2, 3, 4, 5])

# Slicing creates a VIEW (shared memory!)
view = a[1:4]
view[0] = 99
print(a)  # [1, 99, 3, 4, 5]  ← original changed!

# Explicit copy
safe_copy = a[1:4].copy()
safe_copy[0] = 0
print(a)  # [1, 99, 3, 4, 5]  ← original unchanged