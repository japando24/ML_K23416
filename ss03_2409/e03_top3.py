import pandas as pd


def top3_products(df):
    # Tính tổng giá trị bán ra mỗi sản phẩm
    product_sales = df.groupby('ProductID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='TotalSales')

    # Sắp xếp giảm dần theo giá trị bán
    top3 = product_sales.sort_values(by='TotalSales', ascending=False).head(3).reset_index(drop=True)

    return top3


# Ví dụ sử dụng
df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')
result = top3_products(df)
print("Top 3 sản phẩm có giá trị bán ra lớn nhất:")
print(result)
