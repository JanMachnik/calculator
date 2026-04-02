from logic import add, subtract, multiply, divide, percentage


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("To nie jest poprawna liczba, spróbuj ponownie.")


def calculator():
    print("=== PROSTY KALKULATOR ===")

    while True:
        a = get_number("Podaj pierwszą liczbę: ")
        operation = input("Wybierz działanie (*, /, +, -, %, q - wyjście): ")

        if operation == "q":
            print("Koniec programu 👋")
            break

        if operation in ["+", "-", "*", "/"]:
            b = get_number("Podaj drugą liczbę: ")

            if operation == "+":
                result = add(a, b)
            elif operation == "-":
                result = subtract(a, b)
            elif operation == "*":
                result = multiply(a, b)
            elif operation == "/":
                result = divide(a, b)

            if result is None:
                print("Nie można dzielić przez zero!")
            else:
                print(f"Wynik = {result:.2f}")

        elif operation == "%":
            percent = get_number("Podaj wartość procentową: ")
            result = percentage(a, percent)
            print(f"{percent}% z liczby {a} = {result:.2f}")

        else:
            print("Niepoprawny operator!")


if __name__ == "__main__":
    calculator()
