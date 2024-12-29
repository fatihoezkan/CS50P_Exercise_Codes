amount = 50
print(f"Amount Due: {amount}")

while 0 < amount <=50:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5 :
        amount = amount - coin
        if amount  > 0:
            print(f"Amount Due: {amount}")

        else:
            print(f"Change Owed: {amount* (-1)}")
    else:
        print(f"Amount Due: {amount}")