"""
The house has several entrances. Each entrance has the same number of apartments.
Apartments are numbered consecutively, starting from one.
Can a first apartment have a number x at some entrance, and the last one has number y?
"""
STEP_IS_AVAILABLE = "YES"
STEP_IS_NOT_AVAILABLE = "NO"


def chess_game(first_coordinates, second_coordinates):
    if (abs(int(first_coordinates[0]) - int(second_coordinates[0])) < 2
            and abs(int(first_coordinates[1]) - int(second_coordinates[1])) < 2):
        return STEP_IS_AVAILABLE
    return STEP_IS_NOT_AVAILABLE


if __name__ == "__main__":
    input_string = input("Enter a list element separated by space ")
    first_coordinates_input = input_string.split()
    input_string = input("Enter a list element separated by space ")
    second_coordinates_input = input_string.split()
    print(chess_game(first_coordinates_input, second_coordinates_input))
