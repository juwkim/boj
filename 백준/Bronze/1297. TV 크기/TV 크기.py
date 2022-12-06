d, h, w = map(int, input().split())
a = d * (h**2 + w**2)**-.5
print(int(a * h), int(a * w)) 