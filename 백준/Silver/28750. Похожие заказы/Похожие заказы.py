n = int(input())
t, s = [ord(c) - 97 for c in input()], input() * 2
ans = "Impossible"
for d in range(26):
    k = s.find("".join(chr((c + d) % 26 + 97) for c in t))
    if k != -1:
        ans = f"Success\n{k} {d}"
        break
print(ans)