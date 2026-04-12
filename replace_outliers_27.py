import numpy as np

data = np.array([10, 12, 11, 500, 13, 9, 11, -100, 12])

# Define bounds
lower = np.percentile(data, 5)
upper = np.percentile(data, 95)

# Clip outliers
cleaned = np.clip(data, lower, upper)
print(cleaned)

data = np.array([1, 2, 3, 100, 5, -50])

lower = np.percentile(data, 10)
upper = np.percentile(data, 90)

print(np.clip(data, lower, upper))