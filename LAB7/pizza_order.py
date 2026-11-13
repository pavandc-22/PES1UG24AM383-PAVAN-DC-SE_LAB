
TOPPINGS = {"cheese": 40, "olives": 30, "onion": 20, "paneer": 50}
SIZES = {"S": 8, "M": 10, "L": 12}


def toppings_price(toppings_csv):
    if not isinstance(toppings_csv, str):
        raise ValueError("Toppings must be provided as text")

    toppings_csv = toppings_csv.strip()

    if not toppings_csv:
        raise ValueError("At least one topping must be provided")

    total = 0

    for t in toppings_csv.split(','):
        topping = t.strip().lower()

        if not topping:
            raise ValueError("Empty topping is not allowed")

        if topping not in TOPPINGS:
            raise ValueError(f"Unknown topping: {topping}")

        total += TOPPINGS[topping]

    return total


def pizza_inches(size):
    if not isinstance(size, str):
        raise ValueError("Pizza size must be text")

    size = size.strip().upper()

    if size not in SIZES:
        raise ValueError("Invalid pizza size. Choose S, M, or L")

    return SIZES[size]


def split_bill(text):
    if not isinstance(text, str):
        raise ValueError("Bill input must be text")

    parts = text.split('/')

    if len(parts) != 2:
        raise ValueError("Enter bill in total/people format")

    total_text, people_text = parts

    try:
        total = int(total_text.strip())
        people = int(people_text.strip())
    except ValueError:
        raise ValueError("Total and people must be integers") from None

    if total < 0:
        raise ValueError("Total cannot be negative")

    if people <= 0:
        raise ValueError("Number of people must be positive")

    return round(total / people, 2)


def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")
    result = toppings_price(user_input)
    print("Toppings Price:", result)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")
    result = pizza_inches(user_input)
    print("Size in Inches:", result)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")
    result = split_bill(user_input)
    print("Per Person:", result)


if __name__ == "__main__":
    main()
