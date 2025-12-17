# Functions help us create reusable blocks of code that we can use to repeat same logic on different input parameters

def area_of_circle(r):
    pi = 3.14
    area = pi * r * r;
    return area


output = area_of_circle(10);
print(f"Area of circle is {output}")
