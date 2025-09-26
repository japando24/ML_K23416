import pandas as pd

def find_orders_within_range(df, minValue, maxValue):
    # Total Value per Order
    order_totals = df.groupby ('OrderID').apply(lambda x: (x['UnitPrice']* x['Quantity'] * (1-x['Discount'])).sum())
    #Filter Orders to Range
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
    #List off OrderID not trùng nhau
    unique_orders = df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()

    return unique_orders

df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')

minValue = float(input('Enter the minimum value:'))
maxValue = float(input('Enter the maximum value:'))
result = find_orders_within_range(df, minValue, maxValue)
print('List of Invoices in range from',minValue,'to',maxValue,':',result)
