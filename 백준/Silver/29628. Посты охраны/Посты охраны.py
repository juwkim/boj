u, v, w = sorted(map(int, input().split()))
print(w / (4 - max(0, (u**2 + v**2 - w**2) / (u * v))**2)**.5)