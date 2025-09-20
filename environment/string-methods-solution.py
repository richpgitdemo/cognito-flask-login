# Define the original string with the typo and extra white space
original_string = " Jjonathan Smith"
# Step 1: Remove the leading white space using the strip() method
trimmed_string = original_string.strip()  # strip() removes spaces from the left and right sides of the string
# Step 2: Replace "Jjonathan" with "Jonathan" using the replace() method
corrected_string = trimmed_string.replace("Jjonathan", "Jonathan")
# Print the corrected string
print(corrected_string)  # Expected output: Jonathan Smith