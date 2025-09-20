# Define the string
my_string = "Python is awesome!"  # This is the string we'll practice slicing with
# Task 1: Extract "awesome"
# Start slicing from index 10 to the end of the string (index 17)
awesome_slice = my_string[10:17]
print(awesome_slice)  # Expected output: awesome
# Task 2: Extract "Python is"
# Slice from the beginning of the string to index 9
python_is_slice = my_string[:9]
print(python_is_slice)  # Expected output: Python is
# Task 3: Extract "is awesome!"
# Start slicing from index 7 to the end of the string
is_awesome_slice = my_string[7:]
print(is_awesome_slice)  # Expected output: is awesome!
# Task 4 (Bonus): Reverse the entire string
# Use slicing with a step of -1 to reverse the string
reversed_string = my_string[::-1]
print(reversed_string)  # Expected output: !emosewa si nohtyP
# Comments for learners:
# - Slicing syntax: string[start:end] extracts characters from start index to end index (end not included).
# - Omitting start: string[:end] slices from the start to end-1.
# - Omitting end: string[start:] slices from start to the end of the string.
# - Adding a step: string[start:end:step] specifies how many characters to skip (e.g., -1 reverses the string).