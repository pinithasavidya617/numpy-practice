import numpy as np

a = np.array([1, 5, 3, 8, 2])

a > 3          # [False, True, False, True, False]
a == 5         # [False, True, False, False, False]
a != 3         # [True, True, False, True, True]
(a > 2) & (a < 6)   # [False, True, True, False, False]
(a < 2) | (a > 7)   # [True, False, False, True, False

a = np.array([10, 15, 20, 25, 30])

print(a[a > 20])
print(a[(a >= 15) & (a <= 25)])