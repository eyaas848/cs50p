import re


def main():
    text = input("Text: ")
    print(extract(text))


def extract(text):
    return re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)


if __name__ == "__main__":
    main()
