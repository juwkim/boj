M, N, R = input().split()
ax, ay, bx, by = map(int, input().split())
print(min(ay + by, abs(ay - by) + min(ay, by) * abs(ax - bx) * 3.141592 / int(M)) * float(R) / int(N))