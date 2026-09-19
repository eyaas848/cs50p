def main():
    fruits = ["apple", "banana", "cherry"]
    index = int(input("Index: "))
    print(get_item(fruits, index))


def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: index out of range"


if __name__ == "__main__":
    main()
