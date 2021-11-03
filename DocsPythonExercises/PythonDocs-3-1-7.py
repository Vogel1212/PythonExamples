# 4.6. match Statements
# https://docs.python.org/3/tutorial/controlflow.html

# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
# This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), 
# but it can also extract components (sequence elements or object attributes) from the value into variables.

# The simplest form compares a subject value against one or more literals:

class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")