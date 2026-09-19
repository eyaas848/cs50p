def main():
    names = input("Names (comma-separated): ").split(",")
    write_names(names)
    print("Saved names:", read_names())


def write_names(names):
    with open("names.txt", "w") as f:
        for name in names:
            f.write(name.strip() + "\n")


def read_names():
    with open("names.txt", "r") as f:
        return [line.strip() for line in f]


if __name__ == "__main__":
    main()
