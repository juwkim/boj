ans = set(("keys", "phone", "wallet"))
for _ in range(int(input())):
    ans.discard(input())
if ans:
    print(*sorted(ans), sep="\n")
else:
    print("ready")