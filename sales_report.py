import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_excel("international_sales.xlsx")

total_revenue = df["Total_Revenue_USD"].sum()
avg_order = df["Total_Revenue_USD"].mean()

print("=" * 40)
print("BASIC SALES REPORT")
print("=" * 40)

print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Average Order: ${avg_order:,.0f}")

# Country analysis
sales_by_country = df.groupby("Customer_Country")["Total_Revenue_USD"].sum().sort_values(ascending=False)

print("\nTop Countries:")
print(sales_by_country.head())

# Product analysis
sales_by_product = df.groupby("Product")["Total_Revenue_USD"].sum().sort_values(ascending=False)

print("\nTop Products:")
print(sales_by_product.head())

# Save Excel report
with pd.ExcelWriter("outputs/sales_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Raw_Data", index=False)
    sales_by_country.to_excel(writer, sheet_name="Country")
    sales_by_product.to_excel(writer, sheet_name="Product")

# Plot
plt.figure(figsize=(10, 5))
sales_by_country.head(5).plot(kind="bar")

plt.title("Top 5 Countries by Revenue")
plt.ylabel("Revenue (USD)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outputs/sales_chart.png")

print("\nReport saved in outputs/")