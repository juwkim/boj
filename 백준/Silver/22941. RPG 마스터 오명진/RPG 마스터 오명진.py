HP1, ATK1, HP2, ATK2, P, S = map(int, open(0).read().split())
q = (HP2 - P + ATK1 - 1) // ATK1
if HP2 - q * ATK1 >= 1:
    HP2 += S - q * ATK1
    q += (HP2 + ATK1 - 1) // ATK1
if q <= (HP1 + ATK2 - 1) // ATK2:
    print("Victory!")
else:
    print("gg")