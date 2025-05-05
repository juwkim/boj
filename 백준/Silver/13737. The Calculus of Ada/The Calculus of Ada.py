n, *v = map(int, input().split())
d, val = 0, v[-1]
while any(x != v[0] for x in v):
    d += 1
    v = [v[i+1] - v[i] for i in range(len(v)-1)]
    val += v[-1]
print(d, val)