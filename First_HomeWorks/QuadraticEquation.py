# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath


def calculator(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print("No solutions")
    else:
        first_solution = (-b - cmath.sqrt(d)) / (2 * a)
        second_solution = (-b + cmath.sqrt(d)) / (2 * a)
        print(first_solution, second_solution)


if __name__ == "__main__":
    a_input = float(input('Enter a: '))
    b_input = float(input('Enter b: '))
    c_input = float(input('Enter c: '))
    calculator(a_input, b_input, c_input)
