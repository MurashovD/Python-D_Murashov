import util
llist = ["USD", "EUR", "GBP"]
for i in llist:
    r1, r2, r3 = util.currency_rates(i)
    print("Курс валюты({}) на {}: {}".format(r1, r2, r3))
