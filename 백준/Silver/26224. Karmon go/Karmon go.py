from decimal import Decimal

_, inc0, _, mul1, inc1 = input().split()
a = int(inc0) * Decimal(mul1)
b = int(inc1)
print(("Whatever", "Power up, Evolve", "Evolve, Power up")[(a > b) - (a < b)])