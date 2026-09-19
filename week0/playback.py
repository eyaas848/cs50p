def main():
    text = input("Input: ")
    words = text.split()
    slow_text = "...".join(words)
    print("Output:", slow_text)


if __name__ == "__main__":
    main()
