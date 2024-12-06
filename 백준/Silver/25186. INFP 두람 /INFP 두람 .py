N, *d = map(int, open(0).read().split())
if 2 * max(d) <= sum(d) or max(d) == 1:
    print("Happy")
else:
    print("Unhappy")