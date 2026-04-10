import numpy as np

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(b[0, 0])       # 1      (row 0, col 0)
print(b[1, 2]  )     # 6      (row 1, col 2)
print(b[0] )         # [1, 2, 3]  (entire row 0)
print(b[:, 1]  )     # [2, 5, 8]  (entire column 1)
print(b[0:2, 1:3] )  # [[2, 3], [5, 6]]  (sub-matrix) Take rows:    0 → 1Take columns:    1 → 2
print(b[-1, :])

print(b[:, 0]) #first row

print("-" * 45)
c = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(c[:, 2])     # last column
print(c[1:, :2])   # bottom-left part
print(c[::-1])     # reverse rows