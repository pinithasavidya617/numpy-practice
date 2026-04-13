### Boolean Masking
import numpy as np

a = np.array([10, 25, 30, 5, 45, 15])

# Create a mask
mask = a > 20
print(mask)  # [False, True, True, False, True, False]

# Apply the mask (selects True elements)
print(a[mask]  )    # [25, 30, 45]

# Direct filtering
a[a > 20]    # [25, 30, 45]

# Combined conditions
a[(a > 10) & (a < 40)]  # [25, 30, 15]

# Count matches
np.sum(a > 20)   # 3
np.any(a > 40)   # True
np.all(a > 0)    # True

a = np.array([5, 12, 18, 25, 3])

print(a[a > 10])
print(a[(a > 5) & (a < 20)])
print(np.sum(a < 15))