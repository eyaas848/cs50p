def main():
    age = get_age()
    print(f"Your age is: {age}")


def get_age():
    while True:
        try:
            age = int(input("Age: "))
            if age < 0 or age > 120:
                raise ValueError
            return age
        except ValueError:
            print("Invalid age, try again.")


if __name__ == "__main__":
    main()
