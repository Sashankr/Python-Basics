print("Greetings, adventurer")
print(10+20)
# Syntax is rules for valid code.
# When we run code with invalid syntax, the Python interpreter throws an error message and execution stops.
player_health = 1000
print(player_health)

# Python has basic math, add, subtract, divide and multiply.
armor_multiplier = 2
armored_health = player_health * armor_multiplier
print('Armored Health',armored_health)

# Basic Data types
"""
    Strings : A sequence of characters.
    Boolean : True or False.
    Integer : A number without a decimal.
    Float   : A number with a decimal.
"""

# f-string, it can be used to interpolate variables into a string. Let's see with an example below.

name = 'Sashank'
age = 99
race = 'Indian'

print(f"{name} is a {race} who is {age} years old")

# None, it is a special value in Python that represents absence of a value.

current_balance = None
print(f"Current Balance is {current_balance}")

""" 
    Python is dynamically typed language, meaning we can change the type of value that was initially stored in a variable
    and then later assign a different type of value

    Ex:
    speed = 50
    speed = "50"; ---> This is allowed in Python.
    
    But in a statically typed language like Go or Typescript, this won't be allowed.

"""

# When we add strings with a plus operator, a concatenation is performed.

firstName = 'Sashank '
lastName = 'R'
print(firstName + lastName)
