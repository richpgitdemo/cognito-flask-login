# Step 1: Define the age variable
age = 15  # Assign a numeric value to represent someone's age
# Step 2: Use if-elif-else to determine the life stage
if age < 13:
    # If age is less than 13, classify as a child
    print("You are a child.")
elif 13 <= age <= 19:
    # If age is between 13 and 19 (inclusive), classify as a teenager
    print("You are a teenager.")
else:
    # If age is 20 or older, classify as an adult
    print("You are an adult.")