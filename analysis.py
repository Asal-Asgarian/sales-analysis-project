import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_excel("international_sales.xlsx")

# Cleaning
df = df[df["Quantity"] > 0]
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()

# Metrics
total_revenue = df["Total_Revenue_USD"].sum()
avg_order = df["Total_Revenue_USD"].mean()

print("=" * 40)
print("ADVANCED ANALYSIS")
print("=" * 40)

print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Average Order: ${avg_order:,.0f}")

# Analysis
country_sales = df.groupby("Customer_Country")["Total_Revenue_USD"].sum().sort_values(ascending=False)
product_sales = df.groupby("Product")["Total_Revenue_USD"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month")["Total_Revenue_USD"].sum()

# Best values
best_country = country_sales.index[0]
best_product = product_sales.index[0]

print(f"\nTop Country: {best_country}")
print(f"Top Product: {best_product}")

# Dashboard
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
country_sales.head(5).plot(kind="bar")
plt.title("Top Countries")

plt.subplot(1, 2, 2)
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Product Share")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")

# Save cleaned data
df.to_excel("outputs/clean_data.xlsx", index=False)

print("\nAnalysis complete. Files saved in outputs/")