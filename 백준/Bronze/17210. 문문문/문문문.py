N = int(input())
if N > 5:
    print("Love is open door")
else:
    first = int(input())
    for _ in range(N - 1):
        print(1 - first)
        first = 1 - first