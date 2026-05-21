amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    coins = int(input("Insert Coins: "))
    if coins in [25, 10, 5]:
        amount = amount - coins

change = -amount
print(f"Change Owed: {change}")
