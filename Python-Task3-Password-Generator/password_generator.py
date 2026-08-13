import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("❌ Password length must be at least 8 characters.")
            else:
                return length

        except ValueError:
            print("❌ Please enter a valid number.")


def get_character_types():
    while True:
        print("\nChoose character types to include:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter your choices (example: 1234): ")

        selected = set(choices)

        valid_choices = {"1", "2", "3", "4"}
        selected = selected.intersection(valid_choices)

        if len(selected) < 2:
            print("❌ Please select at least 2 character types.")
            continue

        return selected


def generate_password(length, selected):
    character_sets = []

    if "1" in selected:
        character_sets.append(string.ascii_uppercase)

    if "2" in selected:
        character_sets.append(string.ascii_lowercase)

    if "3" in selected:
        character_sets.append(string.digits)

    if "4" in selected:
        character_sets.append(string.punctuation)

    # Guarantee at least one character from every selected type
    password_characters = [
        random.choice(character_set)
        for character_set in character_sets
    ]

    all_characters = "".join(character_sets)

    remaining_length = length - len(password_characters)

    password_characters.extend(
        random.choice(all_characters)
        for _ in range(remaining_length)
    )

    random.shuffle(password_characters)

    return "".join(password_characters)


def main():
    print("=" * 50)
    print("        RANDOM PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        length = get_password_length()
        selected = get_character_types()

        password = generate_password(length, selected)

        print("\n🔐 Generated Password:")
        print(password)

        print("\nWould you like to generate another password?")
        choice = input("Enter Y for yes or N for no: ").strip().lower()

        if choice != "y":
            print("\nThank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()