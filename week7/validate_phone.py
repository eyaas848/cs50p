import re


def main():
    phone = input("Phone: ")
    print("Valid" if is_valid(phone) else "Invalid")


def is_valid(phone):
    return bool(re.fullmatch(r"0[67]\d{8}", phone))


if __name__ == "__main__":
    main()
