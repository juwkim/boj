check = [[] for _ in range(5)]
a, b = input(), input()
for i in range(5):
    u, l = chr(65 + i), chr(97 + i)
    if u in a[2*i:2*i+2] or u in b[2*i:2*i+2]:
        check[i].append(u)
    if l in a[2*i:2*i+2] and l in b[2*i:2*i+2]:
        check[i].append(l)

for _ in range(int(input())):
    if all(c in check[idx] for idx, c in enumerate(input())):
        print("Possible baby.")
    else:
        print("Not their baby!")