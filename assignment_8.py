input_filename = "input.txt"
output_filename = "extracted_output.txt"

# 1. Read the input file and count lines
with open(input_filename, "r") as file:
    lines = file.readlines()  # Reads all lines into a list

total_lines = len(lines)
print(f"Total line count in '{input_filename}': {total_lines}")

# 2. Extract the first two lines
first_two_lines = lines[:2]

# 3. Write the extracted lines to a new file
with open(output_filename, "w") as file:
    file.writelines(first_two_lines)

print(f"Successfully wrote the first 2 lines to '{output_filename}'.")


#OUTPUT:

'''
Total line count in 'input.txt': 4
Successfully wrote the first 2 lines to 'extracted_output.txt'.
'''
