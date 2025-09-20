"""
The Python program below prompts a user to input integers. When the user enters 'quit',
the program displays statistics about the numbers the user has entered.
Modify the code below so that it also displays the sum, minimum, maximum, and average of
the user input.
"""
# Initialize variables
value = ""
my_sum = 0
count = 0

# Accept user input until the user types 'quit'
while value != "quit":
    value = input("Enter a number [or 'quit' to finish]: ")
    # If the user does not enter 'quit', process the number.
    if value != "quit":
        if value.isnumeric():
            count += 1 # count of numbers entered
            number = int(value) # cast input as int
            my_sum += number # add current number to running total
        else:
            print("You must enter a number. Please try again.")
            continue # continue with the next iteration of the loop

# Print summary of results
print(f"You entered {count} integers.")
