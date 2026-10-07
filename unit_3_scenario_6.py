import csv
import sys

# 1. Check if the user provided the CSV file argument
if len(sys.argv) < 2:
    print("Usage: python grocery.py grocery.csv")
    sys.exit()

filename = sys.argv[1]

# 2. Read grocery records from CSV
grocery_items = []
try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            grocery_items.append(row)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit()

# 3. Display all grocery items
print("\n--- ALL GROCERY ITEMS ---")
for item in grocery_items:
    print(f"ID: {item['Item_ID']} | Name: {item['Item_Name']} | Category: {item['Category']} | Price: ₹{item['Price']}")

# 4. Search for an item using Item ID
search_id = input("\nEnter Item ID to search: ").strip()

found = False
for item in grocery_items:
    if item['Item_ID'].lower() == search_id.lower():
        print(f"\nItem Found:")
        print(f"Name: {item['Item_Name']}")
        print(f"Category: {item['Category']}")
        print(f"Price: ₹{item['Price']}")
        found = True
        break

if not found:
    print(f"No item found with ID '{search_id}'.")