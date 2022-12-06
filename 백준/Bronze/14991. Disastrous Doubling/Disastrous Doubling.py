N = int(input())
bacteria = [*map(int, input().split())]
total, p = 1, 10**9 + 7
for exp in bacteria:
    total = total * 2 - exp
    if total < 0:
        break
print(total < 0 and 'error' or total % p)