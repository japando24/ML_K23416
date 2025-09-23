import numpy as np
from itertools import combinations
from sklearn.linear_model import LogisticRegression

# ===== 1. Dữ liệu giả =====
X_train = np.array([
    [0.8, 0.2, 0.5],  # doc1 – query1
    [0.1, 0.9, 0.2],  # doc2 – query1
    [0.6, 0.5, 0.7],  # doc3 – query1
    [0.4, 0.4, 0.8],  # doc4 – query1
    [0.9, 0.1, 0.3],  # doc1 – query2
    [0.2, 0.8, 0.1],  # doc2 – query2
    [0.4, 0.3, 0.9],  # doc3 – query2
    [0.7, 0.6, 0.4],  # doc4 – query2
    [0.5, 0.7, 0.5],  # doc1 – query3
    [0.3, 0.4, 0.6],  # doc2 – query3
])

y_train = np.array([2, 0, 1, 1, 2, 1, 0, 1, 2, 0])   # mức độ liên quan
queries = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3])   # ID truy vấn

#%%
# ===== 2. Tạo dữ liệu pairwise =====
X_pairs = []
y_pairs = []

for q in np.unique(queries):
    idx = np.where(queries == q)[0]  # lấy tất cả doc của query q
    # tạo tất cả các cặp (i, j) trong cùng 1 query
    for i, j in combinations(idx, 2):
        if y_train[i] == y_train[j]:
            continue  # bỏ qua nếu điểm bằng nhau
        if y_train[i] > y_train[j]:
            diff = X_train[i] - X_train[j]
            label = 1
        else:
            diff = X_train[j] - X_train[i]
            label = 0
        X_pairs.append(diff)
        y_pairs.append(label)

X_pairs = np.vstack(X_pairs)
y_pairs = np.array(y_pairs)

print("Số cặp huấn luyện:", X_pairs.shape[0])
print("Ví dụ 1 cặp diff:", X_pairs[0], "Label:", y_pairs[0])

#%%
# ===== 3. Huấn luyện mô hình pairwise =====
model = LogisticRegression()
model.fit(X_pairs, y_pairs)

#%%
# ===== 4. Dự đoán score để xếp hạng trong từng query =====
scores = model.decision_function(X_train)

for q in np.unique(queries):
    idx = np.where(queries == q)[0]
    rank = idx[np.argsort(-scores[idx])]  # sắp xếp giảm dần
    print(f"Query {q} ranking (từ cao xuống thấp):", rank)
