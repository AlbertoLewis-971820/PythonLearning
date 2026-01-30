# ### Reading Files in Python
# 
# #To read a file, use the `open()` function with mode `'r'` (read mode). Always close the file after use to free resources, or use a `with` statement for automatic handling.
# 
# #Basic reading**: Opens the file and reads the entire content as a string.
#   #python
#   #with open('filename.txt', 'r') as file: 
#       content = file.read()
#       print(content)
#   ```
# 
# - **Reading line by line**: Use `readline()` for one line or `readlines()` for all lines as a list.
#   ```python
#   with open('filename.txt', 'r') as file:
#       for line in file:
#           print(line.strip())  # strip() removes newline characters
#   ```
# 
# - **Reading all lines at once**:
#   ```python
#   with open('filename.txt', 'r') as file:
#       lines = file.readlines()
#       for line in lines:
#           print(line.strip())
#   ```
# 
# Handle potential errors like file not found with try-except blocks.
# 
# ### Writing Files in Python
# 
# To write to a file, use `open()` with mode `'w'` (write mode, overwrites existing content) or `'a'` (append mode, adds to existing content).
# 
# - **Basic writing**: Writes a string to the file.
#   ```python
#   with open('filename.txt', 'w') as file:
#       file.write("Hello, World!\n")
#   ```
# 
# - **Writing multiple lines**: Use `writelines()` with a list of strings.
#   ```python
#   lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
#   with open('filename.txt', 'w') as file:
#       file.writelines(lines)
#   ```
# 
# - **Appending to a file**:
#   ```python
#   with open('filename.txt', 'a') as file:
#       file.write("This is appended.\n")
#   ```
# 
# Use the `with` statement to ensure files are properly closed. For binary files, add `'b'` to the mode (e.g., `'rb'`, `'wb'`). Always handle exceptions for file operations.
