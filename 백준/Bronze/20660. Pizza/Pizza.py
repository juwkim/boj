_, *t = map(int, input().split())
print(sum(all(s not in t for s in map(int, input().split()[1:])) for _ in range(int(input()))))