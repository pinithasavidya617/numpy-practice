import numpy as np

data = np.arange(100).reshape(20, 5)  # 20 samples, 5 features
labels = np.random.randint(0, 2, 20)

rng = np.random.default_rng(42)

# Create random indices
indices = rng.permutation(len(data))
split = int(0.8 * len(data))

train_idx = indices[:split]
test_idx = indices[split:]

X_train, X_test = data[train_idx], data[test_idx]
y_train, y_test = labels[train_idx], labels[test_idx]

print(f"Train: {X_train.shape}, Test: {X_test.shape}")
# Train: (16, 5), Test: (4, 5)

print(train_idx)
print(test_idx)

print(X_train[:2])
print(y_train[:2])