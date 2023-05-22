def collect_number():
    """
    This function prompts the user to enter a number and returns it.
    """
    number = float(input("Enter a number: "))
    return number


def add_and_multiply():
    number = float(input("Enter a number: "))
    result = number + 3
    multiplied_result = result * 3
    print("Initial Result:", result)
    print("Multiplied Result:", multiplied_result)
    return result

add_and_multiply()

