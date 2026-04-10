import numpy as np
a = np.array([1, 5, 3, 8, 2])
b = np.array([4, 2, 6, 1, 9])

np.sin(a)           # trigonometric
np.cos(a)
np.tan(a)
np.pi               # 3.14159...
np.e                # 2.71828...

np.ceil(2.3)        # 3.0
np.floor(2.7)       # 2.0
np.clip(a, 2, 6)    # clip values to [2, 6]

np.maximum(a, b)    # element-wise max
np.minimum(a, b)

a = np.array([-5, 0, 5, 10])

print(np.clip(a, 0, 6))
print(np.maximum(a, 2))
print(np.minimum(a, 3))