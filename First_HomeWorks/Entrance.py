"""
The house has several entrances. Each entrance has the same number of apartments.
Apartments are numbered consecutively, starting from one.
Can a first apartment have a number x at some entrance, and the last one has number y?
"""

ENTRANCE_AMOUNT = 3
FLATS_PER_ENTRANCE = 20
FLATS_ARE_ON_THE_SAME_ENTRANCE = "YES"
FLATS_ARE_NOT_ON_THE_SAME_ENTRANCE = "NO"


def if_input_flats_be_on_the_same_entrance(first_flat, second_flat):
    if ((first_flat < 20 and second_flat < 20) or
            (40 > first_flat > 20 and 40 > second_flat > 20) or
            (60 > first_flat > 40 and 60 > second_flat > 40)):
        return FLATS_ARE_ON_THE_SAME_ENTRANCE
    return FLATS_ARE_NOT_ON_THE_SAME_ENTRANCE


if __name__ == "__main__":
    first_number_input = int(input("There are 3 entrances and 20 flats in each one. Enter first flat:"))
    second_number_input = int(input("Enter second flat:"))
    print(if_input_flats_be_on_the_same_entrance(first_number_input, second_number_input))
