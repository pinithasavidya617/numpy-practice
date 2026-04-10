import numpy as np

a = np.array([1, 2, 3], dtype=np.float32)
b = np.zeros((3, 3), dtype=np.int64)
c = np.array([True, False, True], dtype=np.bool_)

# Common dtypes:
# np.int32, np.int64, np.float32, np.float64
# np.bool_, np.complex128, np.str_

print(a.dtype)
print(b.dtype)
print(c.dtype)

a = a.astype(np.int32) #Converts array type

print(a.dtype)

x = np.array([1, 2, 3], dtype=np.int32)
y = np.array([1, 2, 3], dtype=np.float32)

print(x.dtype, y.dtype)