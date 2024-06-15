import sys
input = sys.stdin.readline

card = "123456789TJQK"
for _ in range(int(input())):
    a, *l = input().split()
    z1, z2, z3 = sorted(l, key=lambda x: ("HCDS".index(x[1]), card.index(x[0])))
    i = ((), (z1, z2, z3), (z1, z3, z2), (z2, z1, z3), (z2, z3, z1), (z3, z1, z2), (z3, z2, z1)).index(tuple(l))
    print(card[(card.index(a[0]) + i) % len(card)] + a[1])