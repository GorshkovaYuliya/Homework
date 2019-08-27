"""
The house has several entrances. Each entrance has the same number of apartments.
Apartments are numbered consecutively, starting from one.
Can a first apartment have a number x at some entrance, and the last one has number y?
"""

PERMISSIBLE_NUMBER_OF_BALLS = "YES"
INVALID_NUMBER_OF_BALLS = "NO"

def check_amount_of_balls(input_amount):
    if (input_amount % 3 == 0) or (input_amount % 5 == 0)
        return PERMISSIBLE_NUMBER_OF_BALLS
    return INVALID_NUMBER_OF_BALLS

if __name__ == "__main__":
    input_balls = input("Enter amount")
    print(check_amount_of_balls(int(input_balls)))
