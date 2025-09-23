import numpy as np
import lightgbm as lgb

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

# LightGBM yêu cầu 'group' = số tài liệu trong từng query
group = [np.sum(queries == q) for q in np.unique(queries)]

# ===== 2. Tạo Dataset cho LightGBM =====
train_data = lgb.Dataset(X_train, label=y_train, group=group)

# ===== 3. Tham số mô hình listwise (LambdaRank) =====
params = {
    'objective': 'lambdarank',    # listwise objective
    'metric': 'ndcg',             # đánh giá theo NDCG
    'ndcg_eval_at': [1, 3],       # tính NDCG tại k=1 và k=3
    'learning_rate': 0.1,
    'num_leaves': 31,
    'min_data_in_leaf': 1,
    'verbose': -1
}
#%%
# ===== 4. Huấn luyện mô hình =====
model = lgb.train(params, train_data, num_boost_round=50)

#%%
# ===== 5. Dự đoán & xếp hạng =====
scores = model.predict(X_train)

for q in np.unique(queries):
    idx = np.where(queries == q)[0]
    ranking = idx[np.argsort(-scores[idx])]  # giảm dần theo score
    print(f"Query {q} ranking (cao → thấp):", ranking)
