h = int(input().split()[1])
s = [input() for _ in range(h)]
s += [*zip(*s)]
print(sum(sum(i != j for i, j in zip(l, l[1:])) for l in s))