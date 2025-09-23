import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# --- 1. Dữ liệu giả định ---
# Giả sử chúng ta có 10 cặp (query, document) với 3 features mỗi cặp.
# X là ma trận đặc trưng, mỗi hàng là một tài liệu.
X_train = np.array([
    [0.8, 0.2, 0.5],  # doc1 cho query1
    [0.1, 0.9, 0.2],  # doc2 cho query1
    [0.6, 0.5, 0.7],  # doc3 cho query1
    [0.9, 0.1, 0.3],  # doc1 cho query2
    [0.2, 0.8, 0.1],  # doc2 cho query2
    [0.4, 0.3, 0.9],  # doc3 cho query2
    [0.7, 0.6, 0.4],  # doc4 cho query2
])

# y là điểm relevancy tương ứng.
# Ví dụ: 0=không liên quan, 1=liên quan, 2=rất liên quan
# Mỗi giá trị tại đây ứng với mức độ liên quan của các doc với KQ tìm kiếm
y_train = np.array([2, 0, 1, 2, 1, 0, 1])

#%%
# --- 2. Huấn luyện mô hình ---
# Cách tiếp cận Pointwise coi mỗi hàng là một điểm dữ liệu độc lập.
# Chúng ta có thể dùng bất kỳ mô hình hồi quy nào. Ở đây ta dùng Linear Regression (Hôi quy tuyến tính).
pointwise_model = LinearRegression()

# Huấn luyện mô hình để học cách ánh xạ từ X sang y
pointwise_model.fit(X_train, y_train)

print("Trained Pointwise Model.")

#%%
# --- 3. Dự đoán và Xếp hạng ---
# Giả sử có dữ liệu test cho một truy vấn mới gồm 3 tài liệu.
X_test_query = np.array([
    [0.7, 0.3, 0.6],  # doc_A
    [0.1, 0.8, 0.3],  # doc_B
    [0.9, 0.2, 0.4]   # doc_C
])

# Dự đoán điểm relevancy cho từng tài liệu
predicted_scores = pointwise_model.predict(X_test_query)

print("\n--- Dự đoán cho truy vấn mới ---")
print(f"Features của các tài liệu:\n{X_test_query}")
print(f"Điểm số dự đoán: {predicted_scores}")

# Xếp hạng các tài liệu dựa trên điểm số dự đoán (cao hơn là tốt hơn)
# argsort() trả về chỉ số của các phần tử sau khi đã sắp xếp.
# [::-1] để đảo ngược lại thành thứ tự giảm dần.
ranking_indices = np.argsort(predicted_scores)[::-1]

# In ra thứ hạng
doc_names = ['doc_A', 'doc_B', 'doc_C']
ranked_docs = [doc_names[i] for i in ranking_indices]

print(f"Thứ hạng các tài liệu (từ cao đến thấp): {ranked_docs}")

# Ví dụ về đánh giá mô hình
y_pred_train = pointwise_model.predict(X_train)
mse = mean_squared_error(y_train, y_pred_train)
print(f"\nMean Squared Error trên tập huấn luyện: MSE = {mse:.4f}")
