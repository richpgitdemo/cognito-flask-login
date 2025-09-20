# Step 1: Ask for the user's name and birth year
name = input("Enter your name: ")  # Prompt user for their name
birth_year = input("Enter your birth year: ")  # Prompt user for their birth year
# Step 2: Convert the birth year to an integer
birth_year = int(birth_year)  # Convert the input string to an integer
# Step 3: Calculate the user's age
current_year = 2024  # Define the current year
age = current_year - birth_year  # Calculate the age
# Step 4: Print their name and age
print(f"Hello, {name}. You are {age} years old.")  # Print a message with their name and age
# Step 5: Check if they are 18 or older and print an appropriate message
if age >= 18:
    print("You are an adult.")  # User is 18 or older
else:
    print("You are a minor.")  # User is younger than 18