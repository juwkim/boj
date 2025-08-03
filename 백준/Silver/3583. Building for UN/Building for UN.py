def country(i):
    if i < 26:
        return chr(ord('A') + i)
    return chr(ord('a') + i - 26)

n = int(input())
s = "".join(country(i) for i in range(n))
print(n, n, 2)
for z in range(n):
    print(country(z) * n, s, '', sep='\n')