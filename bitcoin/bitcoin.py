import requests
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])

    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rjson = r.json()
    price = rjson["bpi"]["USD"]["rate_float"]
    result = price * value
    print(f"${result:,.4f}")
except requests.RequestException:
    print("request error")
    sys.exit(1)

#postpone it, from beach in albania
