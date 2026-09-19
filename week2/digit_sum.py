def main():
    n = int(input("Number: "))
    print("Sum of digits:", digit_sum(n))


def digit_sum(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total


if __name__ == "__main__":
    main()
