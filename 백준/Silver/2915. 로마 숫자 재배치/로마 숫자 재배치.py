from itertools import permutations

d = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC"}
for i in range(11, 99):
    if i not in d:
        d[i] = d[i//10*10] + d[i%10]
p = {v: k for k, v in d.items()}
print(d[min(p.get("".join(l), 1e9) for l in permutations(input()))])