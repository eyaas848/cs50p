def main():
    a = get_number("First number: ")
    b = get_number("Second number: ")
    print(divide(a, b))


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"


if __name__ == "__main__":
    main()
