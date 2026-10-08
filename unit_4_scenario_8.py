import numpy as np
import pandas as pd

# Sample Grocery Inventory Data
products = ["Milk", "Bread", "Eggs", "Butter", "Apples", "Rice", "Sugar"]
quantities = [15, 8, 25, 5, 30, 4, 12]

# 1. Create a NumPy array of product prices (in ₹)
prices_array = np.array([60.00, 40.00, 75.00, 250.00, 180.00, 110.00, 45.00])

# 2. Calculate mean, median, maximum, and minimum price using NumPy
mean_price = np.mean(prices_array)
median_price = np.median(prices_array)
max_price = np.max(prices_array)
min_price = np.min(prices_array)

print("--- PRICE STATISTICS ---")
print(f"Mean Price   : ₹{mean_price:,.2f}")
print(f"Median Price : ₹{median_price:,.2f}")
print(f"Maximum Price: ₹{max_price:,.2f}")
print(f"Minimum Price: ₹{min_price:,.2f}\n")

# 3. Create a Pandas DataFrame
df = pd.DataFrame({
    'Product Name': products,
    'Price (₹)': prices_array,
    'Quantity': quantities
})

print("--- ALL GROCERY ITEMS ---")
print(df.to_string(index=False))
print("\n" + "="*40 + "\n")

# 4. Display grocery items having quantity less than 10 (Low Stock Alert)
low_stock_items = df[df['Quantity'] < 10]

print("--- LOW STOCK ITEMS (Quantity < 10) ---")
print(low_stock_items.to_string(index=False))




#OUTPUT:



'''--- PRICE STATISTICS ---
Mean Price   : ₹108.57
Median Price : ₹75.00
Maximum Price: ₹250.00
Minimum Price: ₹40.00

--- ALL GROCERY ITEMS ---
Product Name  Price (₹)  Quantity
        Milk       60.0        15
       Bread       40.0         8
        Eggs       75.0        25
      Butter      250.0         5
      Apples      180.0        30
        Rice      110.0         4
       Sugar       45.0        12

========================================

--- LOW STOCK ITEMS (Quantity < 10) ---
Product Name  Price (₹)  Quantity
       Bread       40.0         8
      Butter      250.0         5
        Rice      110.0         4
'''