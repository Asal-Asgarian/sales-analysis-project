import pandas as pd
from datetime import datetime, timedelta
import random

random.seed(42)

data = {
    "Order_ID": [],
    "Date": [],
    "Customer_Country": [],
    "Product": [],
    "Quantity": [],
    "Unit_Price_USD": []
}

products = ["iPhone 15", "MacBook Pro", "AirPods", "iPad", "Apple Watch"]
countries = ["USA", "Canada", "UK", "Germany", "France", "Japan"]

prices = {
    "iPhone 15": 999,
    "MacBook Pro": 1999,
    "AirPods": 199,
    "iPad": 799,
    "Apple Watch": 429
}

start_date = datetime(2024, 1, 1)

for i in range(200):
    order_id = f"ORD-{i+1:04d}"
    random_date = start_date + timedelta(days=random.randint(0, 90))
    country = random.choice(countries)
    product = random.choice(products)
    quantity = random.randint(1, 5)
    price = prices[product]

    data["Order_ID"].append(order_id)
    data["Date"].append(random_date)
    data["Customer_Country"].append(country)
    data["Product"].append(product)
    data["Quantity"].append(quantity)
    data["Unit_Price_USD"].append(price)

df = pd.DataFrame(data)
df["Total_Revenue_USD"] = df["Quantity"] * df["Unit_Price_USD"]

df.to_excel("international_sales.xlsx", index=False)

print("Dataset created: international_sales.xlsx")