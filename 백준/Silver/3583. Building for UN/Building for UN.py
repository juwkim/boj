def country_char(i):
    if i < 26:
        return chr(ord('A') + i)
    return chr(ord('a') + i - 26)

n = int(input())
h, w, l = n, n, 2
s = "".join(country_char(i) for i in range(n))
print(h, w, l)
for z in range(h):
    print(country_char(z) * w)
    print(s)
    print()