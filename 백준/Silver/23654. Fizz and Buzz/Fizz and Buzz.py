n, *a = map(int, open(0).read().split())
for num in a:
    if num % 5 == 0:
        print("B", end="")
    else:
        print("F", end="")