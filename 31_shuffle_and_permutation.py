import numpy as np

a = np.array([1,2,3,4,5])

rng = np.random.default_rng(42)

b = rng.permutation(a)
print("Original:", a)
print("Permutation:", b)

rng.shuffle(a)
print("Shuffled:", a)