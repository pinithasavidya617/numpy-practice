"""
Correlation vs Covariance — NumPy Reference

This script demonstrates:
1. Covariance → how two variables vary together
2. Correlation → strength + direction of relationship (normalized)

"""

import numpy as np

# -------------------------------
# 1. Sample Data
# -------------------------------
# x and y have a positive relationship
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

print("x:", x)
print("y:", y)

# -------------------------------
# 2. Covariance
# -------------------------------
"""
Covariance measures how two variables change together.

Matrix form:
[ var(x)     cov(x,y) ]
[ cov(y,x)   var(y)   ]
"""

cov_matrix = np.cov(x, y)

print("\nCovariance Matrix:")
print(cov_matrix)

# Extract covariance value between x and y
cov_xy = cov_matrix[0, 1]
print("Covariance (x, y):", cov_xy)

"""
Interpretation:
+ value → x and y increase together
- value → x increases, y decreases
0 → no relationship
"""

# -------------------------------
# 3. Correlation
# -------------------------------
"""
Correlation = normalized covariance
Range: -1 to +1

Matrix form:
[ 1         corr(x,y) ]
[ corr(y,x) 1         ]
"""

corr_matrix = np.corrcoef(x, y)

print("\nCorrelation Matrix:")
print(corr_matrix)

# Extract correlation value
corr_xy = corr_matrix[0, 1]
print("Correlation (x, y):", corr_xy)

"""
Interpretation:
+1   → perfect positive relationship
0    → no relationship
-1   → perfect negative relationship
"""

# -------------------------------
# 4. Manual Understanding (optional)
# -------------------------------
"""
Correlation formula:
corr(x,y) = cov(x,y) / (std(x) * std(y))
"""

std_x = np.std(x, ddof=1)  # sample std (important for matching np.cov)
std_y = np.std(y, ddof=1)

manual_corr = cov_xy / (std_x * std_y)

print("\nManual Correlation Calculation:")
print(manual_corr)

# -------------------------------
# 5. Example: Perfect correlation
# -------------------------------
x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([10, 20, 30, 40, 50])  # perfectly linear

print("\nPerfect Correlation Example:")
print(np.corrcoef(x2, y2))

# -------------------------------
# 6. Key Takeaways
# -------------------------------
"""
Covariance:
- Shows direction of relationship
- Depends on scale (not normalized)

Correlation:
- Shows strength + direction
- Always between -1 and 1
- Easier to interpret

Important:
Correlation ≠ causation
"""