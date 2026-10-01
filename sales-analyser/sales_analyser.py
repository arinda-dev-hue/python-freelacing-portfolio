import pandas as pd

# Read the sales data
sales = pd.read_csv("sales.csv")

# Calculate Total
sales["Total"] = sales["Quantity"] * sales["Price"]

# Calculate Profit if Cost exists
if "Cost" in sales.columns:
    sales["Profit"] = sales["Quantity"] * (sales["Price"] - sales["Cost"])

# Display all products
print("--- ALL PRODUCTS ---")
print(sales.to_string(index=False))

# Analyzer
print("\n--- ANALYSER ---")

print(f"Total Revenue: ${sales['Total'].sum():,.2f}")

print(f"Total Quantity Sold: {sales['Quantity'].sum()}")

print("\nSales by Category:")
print(sales.groupby("Category")["Total"].sum())

print(
    f"\nMost Expensive Product: "
    f"{sales.loc[sales['Price'].idxmax(), 'Product']}"
)

print(
    f"Best Seller (Quantity): "
    f"{sales.loc[sales['Quantity'].idxmax(), 'Product']}"
)
