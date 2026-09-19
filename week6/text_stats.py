def main():
    filename = input("Filename: ")
    with open(filename) as f:
        text = f.read()
    print(f"Lines: {text.count(chr(10))}")
    print(f"Words: {len(text.split())}")
    print(f"Characters: {len(text)}")


if __name__ == "__main__":
    main()
