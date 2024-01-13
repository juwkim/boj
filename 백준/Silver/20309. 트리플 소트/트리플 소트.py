input()
if all((i ^ n) & 1 for i, n in enumerate(map(int, input().split()))):
    print("YES")
else:
    print("NO")