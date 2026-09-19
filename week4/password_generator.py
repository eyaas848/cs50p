import random
import string


def main():
    length = int(input("Password length: "))
    print(generate_password(length))


def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    main()
