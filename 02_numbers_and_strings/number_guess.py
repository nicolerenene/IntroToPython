# Code in a hidden number as a variable
# Prompt user to enter a number
# Sanitize user input
# Convert user input to numeric type (float is best)
# Find out whether user number >, <, == hidden number
# Print the result of equality check

hidden_number = 222
user_number = input('Try to guess the hidden number: ')
user_number = float(user_number.strip())
if user_number > hidden_number:
    print(str(user_number) + ' is greater than the hidden number')
elif user_number < hidden_number:
    print(str(user_number) + ' is less than the hidden number')
else:
    print(str(user_number) + ' is the hidden number!')
