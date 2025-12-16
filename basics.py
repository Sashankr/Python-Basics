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
