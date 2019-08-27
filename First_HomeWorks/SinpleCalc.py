def calculator(choice, first_number, second_number) :
    if choice == '1':
        print(first_number, "+", second_number, "=", first_number + second_number)
    elif choice == '2':
        print(first_number, "-", second_number, "=", first_number - second_number)
    elif choice == '3':
        print(first_number, "*", second_number, "=", first_number * second_number)
    elif choice == '4':
        print(first_number, "/", second_number, "=", first_number / second_number)
    else :
        print("Invalid input")


if __name__ == "__main__" :
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    # Take input from the user
    choice_input = input("Enter choice(1/2/3/4): ")
    number_one = int(input("Enter first number: "))
    number_two = int(input("Enter second number: "))
    calculator(choice_input, number_one, number_two)
