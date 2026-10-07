import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# 1. Create a Series with 10 random floating-point numbers (0 to 9 default index)
series = pd.Series(np.random.uniform(1, 100, 10))

print("--- Original Series ---")
print(series.round(2))
print()

# 2. Indexing
print("--- Indexing ---")
print("First element (series[0]): ", round(series[0], 2))
print("Slice (indices 2 to 5):")
print(series[2:6].round(2))
print()

# 3. Filtering
print("--- Filtering ---")
print("Values > 50:")
print(series[series > 50].round(2))
print()

# 4. Statistical Operations
print("--- Statistics ---")
print(f"Mean   : {series.mean():.2f}")
print(f"Median : {series.median():.2f}")
print(f"Min    : {series.min():.2f}")
print(f"Max    : {series.max():.2f}")


#OUTPUT:
'''
--- Original Series ---
0    38.08
1    95.12
2    73.47
3    60.27
4    16.45
5    16.44
6     6.75
7    86.75
8    60.51
9    71.10
dtype: float64

--- Indexing ---
First element (series[0]):  38.08
Slice (indices 2 to 5):
2    73.47
3    60.27
4    16.45
5    16.44
dtype: float64

--- Filtering ---
Values > 50:
1    95.12
2    73.47
3    60.27
7    86.75
8    60.51
9    71.10
dtype: float64

--- Statistics ---
Mean   : 52.49
Median : 60.39
Min    : 6.75
Max    : 95.12
'''