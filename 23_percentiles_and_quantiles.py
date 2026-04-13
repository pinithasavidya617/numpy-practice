import numpy as np

data = np.random.randn(1000)

np.percentile(data, 25)     # 25th percentile (Q1)
np.percentile(data, 50)     # 50th percentile (median)
np.percentile(data, 75)     # 75th percentile (Q3)
np.percentile(data, [25, 50, 75])  # all three at once

np.quantile(data, 0.95)

data = np.array([1, 2, 3, 4, 5])

print(np.percentile(data, 50))  # median
print(np.quantile(data, 0.5))   # same