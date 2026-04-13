import numpy as np

rng = np.random.default_rng(42)

rng.binomial(n=10, p=0.5, size=100)          # coin flips
# n = 10 → 10 trials
# p = 0.5 → 50% success chance
rng.poisson(lam=5, size=100)
# lam = 5 → average = 5 events
# event counts
rng.exponential(scale=2.0, size=100)
# scale = 2 → average waiting time = 2 units# wait times
rng.choice([1, 2, 3, 4, 5], size=3)          # random sample
rng.choice(10, size=5, replace=False)         # sample without replacement

rng = np.random.default_rng(42)

print("Binomial:", rng.binomial(5, 0.5, 5))
print("Poisson:", rng.poisson(3, 5))
print("Exponential:", rng.exponential(1.0, 5))
print("Choice:", rng.choice([10,20,30], 3))