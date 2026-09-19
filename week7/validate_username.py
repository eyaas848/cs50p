import re


def main():
    username = input("Username: ")
    print("Valid" if is_valid(username) else "Invalid")


def is_valid(username):
    return bool(re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_]{2,15}", username))


if __name__ == "__main__":
    main()
