import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print(a.ndim)       # 2          (number of dimensions)
print(a.shape)      # (3, 4)     (rows, columns)
print(a.size)       # 12         (total elements)
print(a.dtype)      # int64      (data type)
print(a.itemsize )  # 8          (bytes per element)
print(a.nbytes )   # 96         (total bytes = size × itemsize)
