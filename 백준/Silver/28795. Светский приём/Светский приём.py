q, p = map(int, input().split())
if p == q: print("2\n0 0\n0 1")
else: print(f"4\n0 0\n{2 * q} 0\n{2 * q} {p - q}\n{2 * q} 0\n")