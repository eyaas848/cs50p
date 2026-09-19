import csv


def main():
    print(f"Average grade: {average_grade('students.csv'):.2f}")


def average_grade(filename):
    total, count = 0, 0
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["grade"])
            count += 1
    return total / count if count else 0


if __name__ == "__main__":
    main()
