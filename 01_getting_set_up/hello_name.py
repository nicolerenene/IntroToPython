#user_name = input('Please type your name and hit Enter: ')
#print('Hello,', user_name + '!')

# New output:
# Hello CORY, your name is 4 letters long.

# What you need:
#   * ''.strip()
#   * ''.upper()
#   * len('')
user_name = input('Type your name: ')
user_name = user_name.strip()
name_count = len(user_name)
print('Hello, ' + user_name.upper() + ' your name is ' + str(name_count) + ' letters long')
