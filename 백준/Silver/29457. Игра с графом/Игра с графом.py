n, m = map(int, input().split())
if n == 1:
    print("Draw")
elif (n - m) & 1:
    print("Alice")
else:
    print("Bob")