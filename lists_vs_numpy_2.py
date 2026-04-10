import numpy as np

import time

# Python list — slow
python_list = list(range(1_000_000))
start = time.time()
result = [x * 2 for x in python_list]
print(f"Python list: {time.time() - start:.4f}s")

# NumPy array — fast
np_array = np.arange(1_000_000)
start = time.time()
result = np_array * 2
print(f"NumPy array: {time.time() - start:.4f}s")

# NumPy is typically 10-100x faster for numerical operations