import statistics


def main():
    numbers = [float(x) for x in input("Numbers (space-separated): ").split()]
    print(f"Mean: {statistics.mean(numbers):.2f}")
    print(f"Median: {statistics.median(numbers):.2f}")
    print(f"Stdev: {statistics.stdev(numbers):.2f}" if len(numbers) > 1 else "Stdev: N/A")


if __name__ == "__main__":
    main()
