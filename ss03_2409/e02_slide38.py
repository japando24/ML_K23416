import pandas as pd


def find_orders_within_range(df, minValue, maxValue, sortType=True):
    # Tính tổng trị giá mỗi OrderID
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='Sum')

    # Lọc trong khoảng [minValue, maxValue]
    filtered_orders = order_totals[
        (order_totals['Sum'] >= minValue) & (order_totals['Sum'] <= maxValue)
        ]

    # Sắp xếp theo sortType (True = ascending, False = descending)
    filtered_orders = filtered_orders.sort_values(
        by='Sum', ascending=sortType
    ).reset_index(drop=True)

    return filtered_orders


# Ví dụ sử dụng
df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')

minValue = float(input('Enter the minimum value: '))
maxValue = float(input('Enter the maximum value: '))
sortType = input('Sort ascending? (Y/N): ').lower() == 'Y'

result = find_orders_within_range(df, minValue, maxValue, sortType)
print(result)
