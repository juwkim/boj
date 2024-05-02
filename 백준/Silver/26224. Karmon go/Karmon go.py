from decimal import Decimal

name0, inc0, name1, mul1, inc1 = input().split()
inc0, inc1, mul1 = map(Decimal, (inc0, inc1, mul1))
a = (7 + 3 * inc0) * mul1
b = 7 * mul1 + 3 * inc1
if a == b:  print("Whatever")
elif a > b: print("Power up, Evolve")
else:       print("Evolve, Power up")