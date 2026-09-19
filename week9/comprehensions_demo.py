def main():
    numbers = list(range(1, 11))
    squares = [n**2 for n in numbers]
    evens = [n for n in numbers if n % 2 == 0]
    pairs = {n: n**2 for n in numbers}

    print("Squares:", squares)
    print("Evens:", evens)
    print("Pairs:", pairs)


if __name__ == "__main__":
    main()
