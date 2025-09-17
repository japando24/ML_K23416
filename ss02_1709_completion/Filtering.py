from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1.,6.5,3.],
                    [1.,NA,NA],
                    [NA,NA,NA],
                    [NA,6.5,3.]])
print(data)
print("-"*10)
cleaned = data.dropna() # Loại bỏ những dòng có ít nhất một giá trị NaN. Nghĩa là chỉ giữ lại những dòng không có NaN nào cả.
print(cleaned)
cleaned2 = data.dropna(how='all') #chỉ xóa dòng nếu tất cả các cột đều NaN.
print("-"*10)
print(cleaned2)

#Delete negative value:
