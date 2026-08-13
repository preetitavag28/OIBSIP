def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("❌ Please enter a value greater than 0.")
                continue

            return value

        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 45)
    print("           BMI CALCULATOR")
    print("=" * 45)

    weight = get_positive_number("Enter your weight (kg): ")
    height = get_positive_number("Enter your height (m): ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("\n📊 BMI Result")
    print("-" * 45)
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("-" * 45)


if __name__ == "__main__":
    main()