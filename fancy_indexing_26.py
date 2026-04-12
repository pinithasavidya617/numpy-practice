"""
Fancy Indexing in NumPy — Complete Reference

This file demonstrates:
1. Selecting elements using index lists
2. 2D fancy indexing (pairwise selection)
3. Row and column selection
4. Grid selection using np.ix_
"""

import numpy as np

# -------------------------------
# 1. 1D Fancy Indexing
# -------------------------------
a = np.array([10, 20, 30, 40, 50])

# Select elements at specific positions
indices = [0, 2, 4]
selected = a[indices]

print("1D Fancy Indexing:")
print("Original:", a)
print("Selected indices [0,2,4]:", selected)
# Output: [10, 30, 50]

# -------------------------------
# 2. 2D Array
# -------------------------------
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("\n2D Array:")
print(b)

# -------------------------------
# 3. Pairwise Fancy Indexing (IMPORTANT)
# -------------------------------
rows = [0, 2]
cols = [1, 2]

pairwise = b[rows, cols]

print("\nPairwise Selection:")
print("Rows:", rows)
print("Cols:", cols)
print("Result:", pairwise)
# Explanation:
# Takes elements:
# (0,1) → 2
# (2,2) → 9
# Output: [2, 9]

# -------------------------------
# 4. Select Specific Rows
# -------------------------------
selected_rows = b[[0, 2]]

print("\nSelected Rows (0 and 2):")
print(selected_rows)
# Output:
# [[1, 2, 3],
#  [7, 8, 9]]

# -------------------------------
# 5. Select Specific Columns
# -------------------------------
selected_cols = b[:, [0, 2]]

print("\nSelected Columns (0 and 2):")
print(selected_cols)
# Output:
# [[1, 3],
#  [4, 6],
#  [7, 9]]

# -------------------------------
# 6. Grid Selection using np.ix_ (VERY IMPORTANT)
# -------------------------------
grid = b[np.ix_(rows, cols)]

print("\nGrid Selection using np.ix_:")
print(grid)
# Explanation:
# Select rows [0,2] AND columns [1,2]
# Output:
# [[2, 3],
#  [8, 9]]

# -------------------------------
# 7. Key Differences Summary
# -------------------------------
print("\n--- Key Concepts ---")
print("b[rows, cols] → pairwise selection")
print("b[[0,2]] → row selection")
print("b[:, [1,2]] → column selection")
print("b[np.ix_(rows, cols)] → grid selection")

# -------------------------------
# 8. Real ML-style Example
# -------------------------------
# Imagine:
# rows = selected samples
# cols = selected features

X = np.array([[100, 200, 300],
              [400, 500, 600],
              [700, 800, 900]])

rows = [0, 2]   # select samples
cols = [1, 2]   # select features

subset = X[np.ix_(rows, cols)]

print("\nML Example (subset of data):")
print(subset)
# Output:
# [[200, 300],
#  [800, 900]]

# -------------------------------
# 9. Final Notes
# -------------------------------
"""
IMPORTANT:
- Fancy indexing uses lists/arrays of indices
- b[rows, cols] → pairwise selection
- np.ix_() → creates full grid selection
- Very useful for selecting subsets in ML datasets
"""