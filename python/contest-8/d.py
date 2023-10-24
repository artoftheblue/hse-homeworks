import sys
import pandas as pd

def cheque(data, **kwargs):
    actual_cheque = {"product": [],
                     "price": [],
                     "number": []}
    
    for item in kwargs:
        actual_cheque["product"].append(item)
        actual_cheque["price"].append(data[item])
        actual_cheque["number"].append(kwargs[item])

    df = pd.DataFrame(actual_cheque)
    df["cost"] = df["price"] * df["number"]
    df = df.sort_values("product")
    df.index = range(len(df))
    return df

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
