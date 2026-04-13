import numpy as np
import time

a = np.arange(1_000_000)
b = np.arange(1_000_000)

# Loop
start = time.time()
res = [a[i] + b[i] for i in range(len(a))]
print("Loop:", time.time() - start)

# Vectorized
start = time.time()
res = a + b
print("Vectorized:", time.time() - start)