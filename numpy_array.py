import numpy as np

# 1. Create array (1 to 10)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original Array: ", arr)

# 2. Slicing (first 5 elements)
print("First 5 elements arr[:5]:", arr[:5])

# 3. Range slicing (index 2 to 6, which are values 3 through 7)
print("Range slicing arr[2:7]:  ", arr[2:7])

# 4. Step slicing (every second element)
print("Step slicing arr[::2]:   ", arr[::2])

# 5. Summary statistics
print("\n--- Summary Statistics ---")
print("Sum (np.sum): ", np.sum(arr))
print("Mean (np.mean): ", np.mean(arr))
print("Max (np.max): ", np.max(arr))
print("Min (np.min): ", np.min(arr))

# 6. Broadcasting (adds 5 to every element)
arr_plus_5 = arr + 5
print("\n--- Broadcasting ---")
print("Array + 5: ", arr_plus_5)


#OUTPUT:

'''
Original Array:  [ 1  2  3  4  5  6  7  8  9 10]
First 5 elements arr[:5]: [1 2 3 4 5]
Range slicing arr[2:7]:   [3 4 5 6 7]
Step slicing arr[::2]:    [1 3 5 7 9]

--- Summary Statistics ---
Sum (np.sum):  55
Mean (np.mean):  5.5
Max (np.max):  10
Min (np.min):  1

--- Broadcasting ---
Array + 5:  [ 6  7  8  9 10 11 12 13 14 15]
'''