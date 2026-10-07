# 1. WRITING TO A FILE
# 'w' mode creates a new file or overwrites an existing one
with open("example.txt", "w") as file:
    file.write("Hello! this line is writen using the write mode.\n")
    file.write("Python makes file handling easy.\n")
print("File written successfully!\n")

# 2. APPENDING TO A FILE
# 'a' mode adds new content to the end without deleting existing text
with open("example.txt", "a") as file:
    file.write("This line was added using append mode.\n")
print("New line appended successfully!\n")

# 3. READING FROM A FILE
# 'r' mode opens the file to read its contents
print("--- Reading File Contents ---")
with open("example.txt", "r") as file:
    content = file.read()  # Reads the entire file content into a string
    print(content)



#OUTPUT:

'''
File written successfully!

New line appended successfully!

--- Reading File Contents ---
Hello! this line is writen using the write mode.
Python makes file handling easy.
This line was added using append mode.
'''
