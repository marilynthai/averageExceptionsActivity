from math import floor


def calculator():
    print("This calculator will help you find a rounded-down average!")
    print("Enter integers one at a time.")
    print("When you're ready to compute an average, type 'compute'")
    
    finished = False
    numbers = []
    while not finished:
        user_input = input("Enter an integer or 'compute': ")
        if user_input == None:
            raise ValueError('You must enter at least one number before calculating an average')
        elif len(numbers) == 0:
            raise ZeroDivisionError
        #     raise ValueError('cannot compute average of an empty collection')
        elif user_input == "compute":
            print_average(numbers)
            finished = True
        else:
            try:
                number = int(user_input)
            except ValueError:
                print("Invalid input. Input must be an integer or 'compute'")
                continue

            numbers.append(number)


def print_average(numbers):
    average_value = rounded_average(numbers)
    print(f"The rounded-down average of the numbers you entered is {average_value}")


def rounded_average(numbers):
    # try:
    #     avg = sum(numbers) / len(numbers)
    #     return floor(avg)
    # except ZeroDivisionError:
    #     # raise ValueError('cannot compute average of an empty collection')
    #     raise ValueError
    try:
        avg = sum(numbers) / len(numbers)
        return floor(avg)
    except ZeroDivisionError:
        raise ValueError

