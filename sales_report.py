import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------
# Setup
# -------------------
os.makedirs("outputs", exist_ok=True)

df = pd.read_excel("international_sales.xlsx")

# -------------------
# Basic Metrics
# -------------------
total_revenue = df["Total_Revenue_USD"].sum()
avg_order = df["Total_Revenue_USD"].mean()

print("=" * 40)
print("BASIC SALES REPORT")
print("=" * 40)

print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Average Order Value: ${avg_order:,.2f}")

# -------------------
# Analysis
# -------------------
sales_by_country = df.groupby("Customer_Country")["Total_Revenue_USD"].sum().sort_values(ascending=False)
sales_by_product = df.groupby("Product")["Total_Revenue_USD"].sum().sort_values(ascending=False)

print("\nTop Countries:")
print(sales_by_country.head())

print("\nTop Products:")
print(sales_by_product.head())

# -------------------
# Business Insights
# -------------------
print("\n" + "=" * 40)
print("BUSINESS INSIGHTS")
print("=" * 40)

print(f"- Top Country: {sales_by_country.index[0]} (${sales_by_country.iloc[0]:,.0f})")
print(f"- Top Product: {sales_by_product.index[0]} (${sales_by_product.iloc[0]:,.0f})")
print("- Revenue is concentrated in a few countries and products.")

# -------------------
# Save Excel Report
# -------------------
with pd.ExcelWriter("outputs/sales_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Raw_Data", index=False)
    sales_by_country.to_excel(writer, sheet_name="Country")
    sales_by_product.to_excel(writer, sheet_name="Product")

# -------------------
# Visualization (Dashboard)
# -------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sales_by_country.head(5).plot(kind="bar")
plt.title("Top Countries by Revenue")

plt.subplot(1, 2, 2)
sales_by_product.head(5).plot(kind="bar")
plt.title("Top Products by Revenue")

plt.tight_layout()
plt.savefig("outputs/sales_chart.png")

# -------------------
# Summary
# -------------------
print("\nReport successfully generated in /outputs folder")
print("Files created:")
print("- sales_report.xlsx")
print("- sales_chart.png")
