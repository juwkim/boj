from math import gcd
import sys
I = sys.stdin.readline
for i in range(1, 1 + int(I())):
    N, Pd, Pg = map(int, I().split())
    if N * gcd(Pd, 100 - Pd) >= 100 and (Pd == 0 or Pg) and (Pd == 100 or Pg != 100):
        print(f'Case #{i}: Possible')
    else:
        print(f'Case #{i}: Broken')