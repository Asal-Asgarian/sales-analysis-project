import pandas as pd
from datetime import datetime, timedelta
import random

random.seed(42)

# -------------------
# Base structure
# -------------------
data = {
    "Order_ID": [],
    "Date": [],
    "Customer_Country": [],
    "Product": [],
    "Quantity": [],
    "Unit_Price_USD": []
}

# -------------------
# Products & Prices
# -------------------
products = ["iPhone 15", "MacBook Pro", "AirPods", "iPad", "Apple Watch"]

prices = {
    "iPhone 15": 999,
    "MacBook Pro": 1999,
    "AirPods": 199,
    "iPad": 799,
    "Apple Watch": 429
}

# -------------------
# Country weights (more realistic distribution)
# -------------------
country_weights = {
    "USA": 0.35,
    "UK": 0.15,
    "Germany": 0.15,
    "Canada": 0.15,
    "France": 0.1,
    "Japan": 0.1
}

countries = list(country_weights.keys())
weights = list(country_weights.values())

# -------------------
# Date range
# -------------------
start_date = datetime(2024, 1, 1)

# -------------------
# Generate data
# -------------------
for i in range(200):
    order_id = f"ORD-{i+1:04d}"

    random_date = start_date + timedelta(days=random.randint(0, 90))

    country = random.choices(countries, weights=weights)[0]
    product = random.choice(products)

    # realistic quantity logic
    if product == "MacBook Pro":
        quantity = random.randint(1, 2)
    elif product == "iPhone 15":
        quantity = random.randint(1, 3)
    else:
        quantity = random.randint(1, 5)

    price = prices[product]

    data["Order_ID"].append(order_id)
    data["Date"].append(random_date)
    data["Customer_Country"].append(country)
    data["Product"].append(product)
    data["Quantity"].append(quantity)
    data["Unit_Price_USD"].append(price)

# -------------------
# Create DataFrame
# -------------------
df = pd.DataFrame(data)

df["Total_Revenue_USD"] = df["Quantity"] * df["Unit_Price_USD"]

# -------------------
# Save file
# -------------------
df.to_excel("international_sales.xlsx", index=False)

print("Dataset created successfully: international_sales.xlsx")
