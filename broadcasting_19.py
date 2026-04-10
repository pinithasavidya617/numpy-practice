import numpy as np

# 1. Scalar + Array
a = np.array([1, 2, 3])
print("Scalar + Array:", a + 10)

# 2. 1D + 2D broadcasting
a = np.array([1, 2, 3])           # (3,)
b = np.array([[10], [20], [30]])  # (3,1)

print("\n1D + 2D Broadcasting:")
print(a + b)

# 3. Using newaxis
a = np.array([1, 2, 3])
row = a[np.newaxis, :]   # (1,3)
col = a[:, np.newaxis] # (3,1)
print("row ")
print(row)
print("col ")
print( col)

print("\nRow + Column (outer addition):")
print(row + col)

# 4. Broadcasting with different shapes
x = np.array([[1, 2, 3],
              [4, 5, 6]])   # (2,3)

y = np.array([10, 20, 30])  # (3,)

print("\n2D + 1D Broadcasting:")
print(x + y)

# 5. Broadcasting in math functions
a = np.array([-2, 1, 4, 7])

print("\nMax with scalar (ReLU-like):")
print(np.maximum(a, 0))

print("\nClipping:")
print(np.clip(a, 0, 5))

# 6. Broadcasting error example
try:
    a = np.array([1,2,3])
    b = np.array([1,2])
    print(a + b)
except Exception as e:
    print("\nError example:", e)