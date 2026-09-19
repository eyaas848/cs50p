def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def main():
    print(add(2, 3), subtract(5, 2), multiply(4, 3), divide(10, 2))


if __name__ == "__main__":
    main()
