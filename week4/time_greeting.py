from datetime import datetime


def main():
    print(greeting(datetime.now().hour))


def greeting(hour):
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


if __name__ == "__main__":
    main()
