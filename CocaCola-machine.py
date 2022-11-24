# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
amountDue = 50

while amountDue > 0:
    cents = input('Insert Coin: ')
    while (cents != '25') and ((cents != '10') and (cents != '5')):
        print("That's not a coin :)")
        cents = input('Insert Coin: ')
    amountDue -= int(cents)
    if amountDue > 0:
        print('Amount due: ' + str(amountDue))
    else:
        print('Change owed: ' + str(-amountDue))