# Currency Converter Project (Fresher Student Version)

# Hardcoded exchange rates relative to USD.
# This dictionary stores how many USD 1 unit of a given currency is worth.
# These rates are illustrative and not real-time.
EXCHANGE_RATES = {
    'USD': 1.0,   # US Dollar
    'EUR': 1.08,  # Euro
    'GBP': 1.27,  # British Pound
    'JPY': 0.0067, # Japanese Yen (1 JPY = 0.0067 USD approx)
    'AUD': 0.66,  # Australian Dollar
    'CAD': 0.73,  # Canadian Dollar
    'CHF': 1.12,  # Swiss Franc
    'CNY': 0.14,  # Chinese Yuan
    'INR': 0.012, # Indian Rupee (1 INR = 0.012 USD approx)
    'BRL': 0.20,  # Brazilian Real
}

def get_currency_input(prompt):
    """Gets and validates currency code from user input."""
    while True:
        currency = input(prompt).upper() # Convert input to uppercase for case-insensitivity
        if currency in EXCHANGE_RATES:
            return currency
        else:
            print(f"Error: Currency '{currency}' not supported. Please choose from: {', '.join(EXCHANGE_RATES.keys())}")

def get_amount_input():
    """Gets and validates the amount to convert from user input."""
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount > 0:
                return amount
            else:
                print("Error: Amount must be a positive number.")
        except ValueError:
            print("Error: Invalid amount. Please enter a numerical value.")

def convert_currency(amount, from_currency, to_currency):
    """Converts an amount from one currency to another using predefined rates."""
    try:
        # Step 1: Convert the 'from' currency amount to USD (our base currency)
        # Formula: amount_in_usd = amount_to_convert * (USD value of 1 unit of from_currency)
        amount_in_usd = amount * EXCHANGE_RATES[from_currency]

        # Step 2: Convert the USD amount to the 'to' currency
        # Formula: converted_amount = amount_in_usd / (USD value of 1 unit of to_currency)
        converted_amount = amount_in_usd / EXCHANGE_RATES[to_currency]
        
        return converted_amount
    except KeyError as e:
        # This error should ideally be caught by get_currency_input validation,
        # but it's included here as a fallback for robustness.
        print(f"An internal error occurred: Currency rate not found for {e}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during conversion: {e}")
        return None

def main():
    print("Welcome to the Simple Currency Converter!")
    print(f"Supported Currencies: {', '.join(EXCHANGE_RATES.keys())}")
    print("-" * 30)

    while True:
        amount_to_convert = get_amount_input()
        from_currency = get_currency_input("Enter the currency you are converting FROM (e.g., USD, EUR): ")
        to_currency = get_currency_input("Enter the currency you want to convert TO (e.g., GBP, JPY): ")

        if from_currency == to_currency:
            print(f"{amount_to_convert:.2f} {from_currency} is still {amount_to_convert:.2f} {to_currency}.")
            print("-" * 30)
            another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
            if another_conversion != 'yes':
                print("Thank you for using the Currency Converter!")
                break
            else:
                continue # Allow user to try again with different currencies

        result = convert_currency(amount_to_convert, from_currency, to_currency)

        if result is not None:
            print("-" * 30)
            print(f"{amount_to_convert:.2f} {from_currency} is equal to {result:.2f} {to_currency}")
            print("-" * 30)
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            print("Thank you for using the Currency Converter!")
            break

if __name__ == "__main__":
    main()