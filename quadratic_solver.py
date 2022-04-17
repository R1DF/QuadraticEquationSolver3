# Imports
import os
from math import sqrt
import cmath

# Defining functions
def clear():
    os.system("cls" if os.name=="nt" else "clear")

def get_int_input_with_range(prompt, options):
    while True:
            try:
                user_input = int(input(prompt))

                if user_input in options:
                    return user_input

                print("Please enter a valid option!\n")
            except ValueError:
                print("Please enter a number!\n")

def get_float_input_with_exceptions(prompt, exceptions=[]):
    while True:
        try:
            user_input = float(input(prompt))

            if not (user_input in exceptions):
                return user_input

            print("Please enter a valid number!\n")

        except ValueError:
            print("Please enter a number!\n")

def get_turning_point(coefficients):
    d = coefficients[1] / (2 * coefficients[0])
    turning_point_x = -d
    #e = -coefficients[0] * ()
    return f"({turning_point_x}, {(coefficients[0] * (turning_point_x ** 2)) + ( coefficients[1] * turning_point_x) + coefficients[2]})"

def format_equation(coefficients):
    a, b, c = [int(x) if x == int(x) else x for x in coefficients] # any whole numbers as floats get converted
    result = ""

    # Adding coefficient A
    if a == -1:
        result += "-x^2"
    elif a == 1:
        result += "x^2"
    else:
        result += f"{a}x^2"

    # Adding coefficient B
    if b > 0:
        result += f" + {b}x" if b != 1 else f" + x"
    elif b < 0:
        result += f" - {b}x" if b != 1 else f" - x"

    # Adding coefficient C
    if c > 0:
        result += f" + {c}"
    elif c < 0:
        result += f" - {-c}"

    return result + " = 0"

# Introduction and selecting result type
clear()
print("Welcome to R1DF's simplified quadratic equation solver.\n"
      "Which mode would you like to select to solve with:\n"
      "1. Simplified\n"
      "2. Full details\n")

mode = get_int_input_with_range("Select by number: ", [1, 2])
clear()

# Obtaining coefficients
print("Standard quadratic equation: \nax^2 + bx + c = 0\nPlease enter the coefficients.\n\n")
coefficients = []
for i in ["A", "B", "C"]:
    if i == "A":
        coefficients.append(get_float_input_with_exceptions(f"Please enter coefficient {i}: ", [0])) # Coefficient A cannot be 0.
    else:
        coefficients.append(get_float_input_with_exceptions(f"Please enter coefficient {i}: "))

clear()

# Solving
discriminant = (coefficients[1] ** 2) - (4 * coefficients[0] * coefficients[2])

if discriminant > 0:
    roots = [(-coefficients[1] + sqrt(discriminant)) / (2 * coefficients[0]),
             (-coefficients[1] - sqrt(discriminant)) / (2 * coefficients[0])] # 2 roots
elif discriminant == 0:
    roots = [(-coefficients[1] + sqrt(discriminant)) / (2 * coefficients[0])] # only 1 root
else:
    roots = [(-coefficients[1] + cmath.sqrt(discriminant)) / (2 * coefficients[0]),
             (-coefficients[1] - cmath.sqrt(discriminant)) / (2 * coefficients[0])] # 2 complex roots

    # Re-formatting
    for i in range(2):
        roots[i] = str(roots[i]).replace("j", "i").replace("(", "").replace(")", "").replace("1i", "i") # i > j hands down

turning_point = get_turning_point(coefficients)

# Displaying
clear()
print(f"Entered equation: {format_equation(coefficients)}\n")
if mode == 1:

    if discriminant > 0:
        print("There are two roots.\nx1 = {0}\nx2 = {1}".format(*roots))
    elif discriminant == 0:
        print(f"There is only one root.\nx = {coefficients[0]}")
    else:
        print("The discriminant is less than 0.\nThere are no real roots that satisfy the equation!")

else:
    print(f"Discriminant = {discriminant};")

    if discriminant != 0:
        print(f"There are 2 {'complex' if discriminant < 0 else 'real'} roots.\n"
              f"x1 = {roots[0]}, x2 = {roots[1]}")

    else:
        print(f"There is 1 real root.\n"
              f"x = {roots[0]}")

    print(f"\nTurning point: {turning_point}\n"
          f"Point of Y-interception: (0, {coefficients[2]})")

# Asking for exit
input("\n\nHit Enter to exit...")
clear()
