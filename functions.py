# Functions help us create reusable blocks of code that we can use to repeat same logic on different input parameters

def area_of_circle(r):
    pi = 3.14
    area = pi * r * r;
    return area


output = area_of_circle(10);
print(f"Area of circle is {output}")

# We cannot call functions without it being defined first.

# When we don't return anything from a function None is returned.

def sum():
    print('Sum called')

sum_res = sum();
print(sum_res)

def message(name,age):
    greeting = f'Hello {name}'
    new_age = age + 1
    return greeting, new_age

greeting, age_next_year = message('Sashank',99)
print(greeting, age_next_year)

# Default value in functions

def add(a,b=10):
    return a + b;

res = add(5);
print(res)


