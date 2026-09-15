def exchange (money,currency):
    EURExchangeRate=600000
    USDExchangeRate=500000
    if currency == "USD":
        return money/USDExchangeRate
    elif currency == "EUR":
        return money/EURExchangeRate
    else:
        print("Wrong currency")

x=exchange(3000000000000,"EUR")
print(x)
