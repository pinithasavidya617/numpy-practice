import numpy as np

a = np.array([3, 1, 4, 1, 5, 9, 2, 6])

np.sort(a)       # [1, 1, 2, 3, 4, 5, 6, 9]  (returns sorted copy)
a.sort()         # sorts in-place

# Sort indices (argsort)
indices = np.argsort(a)  # indices that would sort the array
a[indices]               # sorted array

# Sort 2D along axis
b = np.array([[3, 1, 2],
              [6, 4, 5]])
np.sort(b, axis=0)  # sort each column
np.sort(b, axis=1)  # sort each row

# Partial sort (k smallest)
np.partition(a, 3)  # first 3 elements are the 3 smallest (unordered)

a = np.array([8, 3, 5, 1, 9, 7,4,3])

print(np.sort(a))
print(np.argsort(a))
print(np.partition(a, 2))

scores = np.array([70, 90, 80, 60, 85])
names  = np.array(["A","B","C","D","E"])

idx = np.argsort(scores)
print(idx)

print(names[idx])   # sorted by scores