def main():
    number = int(input("Enter a number: "))
    print(check(number))


def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    main()
