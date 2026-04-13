import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
a + b       # [11, 22, 33, 44]
a - b       # [-9, -18, -27, -36]
a * b       # [10, 40, 90, 160]
a / b       # [0.1, 0.1, 0.1, 0.1]
a ** 2      # [1, 4, 9, 16]
a % 2       # [1, 0, 1, 0]
print(np.sqrt(a))  # [1.0, 1.414, 1.732, 2.0]
print(np.exp(a))   # [2.718, 7.389, 20.086, 54.598]
print(np.log(a)  ) # [0.0, 0.693, 1.099, 1.386]
print(np.abs(a)   )# absolute value
print(np.round(a / 3, 2) ) # round to 2 decimal places

print("-" * 64)
c = np.array([2,4,6,8])

print(c + 10)
print(c * 3)
print(np.sqrt(c))