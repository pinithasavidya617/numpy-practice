import numpy as np

rng = np.random.default_rng(seed=42)  # reproducible

# Uniform [0, 1)
rng.random(5)           # 5 random floats
rng.random((3, 4))      # 3×4 matrix

# Uniform [low, high)
rng.uniform(10, 20, size=5)

# Integer [low, high)
rng.integers(1, 7, size=10)   # dice rolls

# Normal distribution (mean=0, std=1)
# Bell-shaped distribution
rng.standard_normal(1000)

# Normal with specific mean and std
rng.normal(loc=100, scale=15, size=1000)  # IQ scores
# Mean = 100
# Std = 15

rng = np.random.default_rng(42)
# Why seed=42?
#
#  Makes results reproducible
#
# Same seed → same random numbers every time

print(rng.integers(0, 10, size=5))
print(rng.uniform(0, 1, size=3))
print(rng.normal(0, 1, size=3))