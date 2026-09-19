def main():
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.1f} — {category(bmi)}")


def category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    main()
