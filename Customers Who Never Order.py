import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    c = customers.where(~customers["id"].isin(orders.customerId)).dropna()[["name"]].rename({"name":"Customers"}, axis=1)
    return c