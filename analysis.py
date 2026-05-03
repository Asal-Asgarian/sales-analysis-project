import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

# Load data
df = pd.read_excel("international_sales.xlsx")

# -------------------
# Data Cleaning
# -------------------
df = df[df["Quantity"] > 0]
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

# -------------------
# Metrics
# -------------------
total_revenue = df["Total_Revenue_USD"].sum()
avg_order = df["Total_Revenue_USD"].mean()

print("=" * 40)
print("SALES ANALYSIS REPORT")
print("=" * 40)

print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Average Order Value: ${avg_order:,.2f}")

# -------------------
# Group Analysis
# -------------------
country_sales = df.groupby("Customer_Country")["Total_Revenue_USD"].sum().sort_values(ascending=False)
product_sales = df.groupby("Product")["Total_Revenue_USD"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month")["Total_Revenue_USD"].sum()

# -------------------
# Insights
# -------------------
best_country = country_sales.index[0]
best_product = product_sales.index[0]
best_month = monthly_sales.idxmax()

print("\n" + "=" * 40)
print("BUSINESS INSIGHTS")
print("=" * 40)

print(f"- Top Country: {best_country}")
print(f"- Top Product: {best_product}")
print(f"- Highest Sales Month: {best_month}")
print("- Sales show variation across countries, products, and months.")

# -------------------
# Dashboard
# -------------------
plt.figure(figsize=(12, 8))

# Top Countries
plt.subplot(2, 2, 1)
country_sales.head(5).plot(kind="bar")
plt.title("Top Countries by Revenue")

# Top Products
plt.subplot(2, 2, 2)
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Product Share")

# Monthly Trend
plt.subplot(2, 2, 3)
monthly_sales.sort_index().plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")

# -------------------
# Save Clean Data
# -------------------
df.to_excel("outputs/clean_data.xlsx", index=False)

print("\nAnalysis complete. Files saved in outputs/")
