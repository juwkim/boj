import sys
input = sys.stdin.readline

while d:=int(input()):
    cad, usd = 100000, 0
    for _ in range(d):
        rate = float(input())
        cad, usd = max(cad, usd * rate * 97 // 100), max(usd, cad / rate * 97 // 100)
    print(f"{cad / 100:.2f}")