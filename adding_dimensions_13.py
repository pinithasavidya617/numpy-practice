import numpy as np

a = np.array([1, 2, 3])  # shape: (3,)

# Add dimension
row = a[np.newaxis, :]     # shape: (1, 3)  — row vector
col = a[:, np.newaxis]     # shape: (3, 1)  — column vector
row = np.expand_dims(a, axis=0)  # same as above

# Remove dimension
b = np.array([[1, 2, 3]])  # shape: (1, 3)
np.squeeze(b)               # shape: (3,)

b = np.array([5, 10, 15])

print(b.shape)
print(b)

print(b[np.newaxis, :].shape) #[[5 10 15]]
row = b[np.newaxis, :]
print(row)


print(b[:, np.newaxis].shape)
col = b[:, np.newaxis]
print(col)
