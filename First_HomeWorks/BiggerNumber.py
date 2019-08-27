"""
This is the first homework.
Given two integers entered by the user. The program should output the number "1"
if the first number is greater than the second, the number "2", if the second is greater than the first,
or the number "0" if they are equal.
"""

FIRST_NUMBER_BIGGER = 1
SECOND_NUMBER_BIGGER = 2


def compare_input_numbers(first_number, second_number):
    print(first_number)
    print(second_number)
    if int(first_number) > int(second_number):
        return FIRST_NUMBER_BIGGER
    else:
        return SECOND_NUMBER_BIGGER


if __name__ == "__main__":
    first_number_input = input("Enter first number:")
    second_number_input = input("Enter second number")
    compare_input_numbers(first_number_input, second_number_input)
