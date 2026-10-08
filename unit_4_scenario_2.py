import numpy as np
import pandas as pd

# 1. Sample Employee Data
names = ["Aarav", "Ananya", "Rohan", "Priya", "Vikram", "Neha", "Siddharth"]
departments = ["IT", "HR", "Finance", "IT", "Marketing", "Finance", "IT"]

# Create a NumPy array of employee salaries (in ₹)
salaries_array = np.array([55000, 62000, 48000, 75000, 59000, 80000, 64000])

# 2. Calculate average, maximum, and minimum salary using NumPy
avg_salary = np.mean(salaries_array)
max_salary = np.max(salaries_array)
min_salary = np.min(salaries_array)

print("--- SALARY STATISTICS ---")
print(f"Average Salary : ₹{avg_salary:,.2f}")
print(f"Maximum Salary : ₹{max_salary:,.2f}")
print(f"Minimum Salary : ₹{min_salary:,.2f}\n")

# 3. Create a Pandas DataFrame
df = pd.DataFrame({
    'Employee Name': names,
    'Department': departments,
    'Salary (₹)': salaries_array
})

print("--- ALL EMPLOYEES ---")
print(df.to_string(index=False))
print("\n" + "="*40 + "\n")

# 4. Display employees earning more than ₹60,000
high_earners = df[df['Salary (₹)'] > 60000]

print("--- EMPLOYEES EARNING MORE THAN ₹60,000 ---")
print(high_earners.to_string(index=False))




#OUTPUT:



'''
--- SALARY STATISTICS ---
Average Salary : ₹63,285.71
Maximum Salary : ₹80,000.00
Minimum Salary : ₹48,000.00

--- ALL EMPLOYEES ---
Employee Name Department  Salary (₹)
        Aarav         IT       55000
       Ananya         HR       62000
        Rohan    Finance       48000
        Priya         IT       75000
       Vikram  Marketing       59000
         Neha    Finance       80000
    Siddharth         IT       64000

========================================

--- EMPLOYEES EARNING MORE THAN ₹60,000 ---
Employee Name Department  Salary (₹)
       Ananya         HR       62000
        Priya         IT       75000
         Neha    Finance       80000
    Siddharth         IT       64000
'''