import util
import sys
r1, r2, r3 = util.currency_rates(sys.argv[1])
print("Курс валюты({}) на {}: {}".format(r1, r2, r3))
