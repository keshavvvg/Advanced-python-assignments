import csv
import sys

# 1. Check if the CSV filename was provided as a command-line argument
if len(sys.argv) < 2:
    print("Error: Missing filename.")
    print("Usage: python sports_inventory.py sports.csv")
    sys.exit()

filename = sys.argv[1]

# 2. Read sports equipment records from CSV file
equipment_list = []
try:
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            equipment_list.append(row)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Make sure it's in the same folder!")
    sys.exit()

# 3. Display all sports equipment details
print("\n================ ALL SPORTS EQUIPMENT ================")
for item in equipment_list:
    print(f"ID: {item['Equipment_ID']} | Name: {item['Equipment_Name']} | Sport: {item['Sport']} | Quantity: {item['Quantity']} | Price: ₹{item['Price']}")
print("======================================================\n")

# 4. Search for equipment using Equipment ID
search_id = input("Enter Equipment ID to search: ").strip()

found = False
for item in equipment_list:
    if item['Equipment_ID'].strip().lower() == search_id.lower():
        print(f"\n✓ Equipment Found:")
        print(f"  • ID       : {item['Equipment_ID']}")
        print(f"  • Name     : {item['Equipment_Name']}")
        print(f"  • Sport    : {item['Sport']}")
        print(f"  • Quantity : {item['Quantity']}")
        print(f"  • Price    : ₹{item['Price']}")
        found = True
        break

if not found:
    print(f"\n✗ No equipment found with Equipment ID '{search_id}'.")