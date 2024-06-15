w, h = sorted(map(int, input().split()))
print(w**2 + min(h - w, w)**2)