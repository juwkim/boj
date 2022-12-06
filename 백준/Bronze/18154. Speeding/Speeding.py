t, d = zip(*[map(int, input().split()) for _ in range(int(input()))])
print(int(max((d[i+1]-d[i])/(t[i+1]-t[i]) for i in range(len(t)-1))))