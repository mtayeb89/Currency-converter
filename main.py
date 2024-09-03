def currency_converter():
    rates = {
        "USD": {"EUR": 0.85, "GBP": 0.75, "JPY": 110.0, "EGP": 30.90},
        "EUR": {"USD": 1.18, "GBP": 0.88, "JPY": 129.0, "EGP": 36.35},
        "GBP": {"USD": 1.33, "EUR": 1.14, "JPY": 146.0, "EGP": 41.20},
        "JPY": {"USD": 0.0091, "EUR": 0.0078, "GBP": 0.0068, "EGP": 0.28},
        "EGP": {"USD": 0.032, "EUR": 0.027, "GBP": 0.024, "JPY": 3.57},
    }

    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount you want to convert: "))
    from_currency = input("Enter the currency you are converting from (e.g., USD, EUR, GBP, JPY, EGP): ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()

    if from_currency in rates and to_currency in rates[from_currency]:
        converted_amount = amount * rates[from_currency][to_currency]
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Currency conversion not supported.")

if __name__ == "__main__":
    currency_converter()
