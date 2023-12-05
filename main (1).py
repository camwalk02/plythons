import random
# enclose the statement in try block
try:
    print(random.randinteger(5, 15))
# the catch block will catch errors of type AttributeError
except AttributeError as err:
    # once caught print the below error message
    print('Double check the attributes in your code and try again.')
