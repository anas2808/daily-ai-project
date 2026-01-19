import requests
import sys

def fetch_exchange_rates(api_url, api_key):
    """
    Fetches current exchange rates from the given API.

    :param api_url: URL of the exchange rate API
    :param api_key: API key for authentication
    :return: A dictionary containing currency exchange rates
    :raises: Exception if there is an issue with the API request
    """
    try:
        response = requests.get(api_url, headers={"apikey": api_key})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data['rates']
    except requests.RequestException as e:
        raise Exception(f"Error fetching exchange rates: {e}")

def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another using provided rates.

    :param amount: Amount of money to convert
    :param from_currency: Currency code of the source currency
    :param to_currency: Currency code of the target currency
    :param rates: A dictionary containing currency exchange rates
    :return: Converted amount in the target currency
    :raises: ValueError if currency codes are invalid
    """
    try:
        from_rate = rates[from_currency]
        to_rate = rates[to_currency]
        converted_amount = (amount / from_rate) * to_rate
        return converted_amount
    except KeyError:
        raise ValueError(f"Invalid currency code: {from_currency} or {to_currency}")

def main():
    """
    Main function to execute the currency conversion program.
    """
    # Configuration for the currency conversion API
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    api_key = "your_api_key_here"  # Replace with a valid API key

    # Fetch the latest exchange rates
    try:
        exchange_rates = fetch_exchange_rates(api_url, api_key)
    except Exception as e:
        print(e)
        sys.exit(1)

    # Get user input for conversion
    try:
        amount = float(input("Enter amount to convert: "))
        from_currency = input("Enter source currency code (e.g., USD): ").upper()
        to_currency = input("Enter target currency code (e.g., EUR): ").upper()
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    # Perform currency conversion
    try:
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()