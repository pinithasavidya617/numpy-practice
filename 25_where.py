import numpy as np

a = np.array([1, -2, 3, -4, 5])

# Replace negatives with 0
np.where(a > 0, a, 0)  # [1, 0, 3, 0, 5]

# Categorize
labels = np.where(a > 0, 'positive', 'negative')
# ['positive', 'negative', 'positive', 'negative', 'positive']

# Find indices where condition is true
np.where(a > 0)  # (array([0, 2, 4]),)

a = np.array([10, -5, 0, 8, -2])

print(np.where(a > 0, 1, 0))  # binary classification
print(np.where(a == 0))       # find zeros