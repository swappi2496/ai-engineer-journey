import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line agrument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        rate = data["bpi"]["USD"]["rate_float"]
        total = bitcoins * rate
        print(f"${total:,.4f}")
    except (requests.RequestException, KeyError, ValueError):
        sys.exit("Could not fetch Bitcoin price")
if __name__ == "__main__":
    main()


