import numpy as np

a = np.array([10, 20, 30, 40, 50])

a[0]      # 10     (first element)
a[-1]     # 50     (last element)
a[1:4]    # [20, 30, 40]  (slice)
a[::2]    # [10, 30, 50]  (every other element)
a[::-1]   # [50, 40, 30, 20, 10]  (reversed)