import numpy as np

data = np.array([[1, 100],
                 [2, 200],
                 [3, 300]])

# Mean and std per column
mean = data.mean(axis=0)    # [2.0, 200.0]
std = data.std(axis=0)      # [0.816, 81.649]

# Standardize (z-score) — broadcasting handles shape mismatch
normalized = (data - mean) / std
#
# [1, 100] - [2, 200] = [-1, -100]
# [-1/0.816, -100/81.649] ≈ [-1.225, -1.225]
#
# [2, 200] - [2, 200] = [0, 0]
# → [0, 0]
#
# [3, 300] - [2, 200] = [1, 100]
# [1/0.816, 100/81.649] ≈ [1.225, 1.225]

# final result =
#  [[-1.225, -1.225],
#  [ 0.   ,  0.   ],
#  [ 1.225,  1.225]]

data = np.array([[10, 1000],
                 [20, 2000],
                 [30, 3000]])

mean = data.mean(axis=0)
std = data.std(axis=0)
print(mean)
print(std)

print((data - mean) / std)