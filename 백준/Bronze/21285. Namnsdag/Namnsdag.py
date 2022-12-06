name = input()
n, count = len(name), 0
input()
while True:
    count += 1
    s = input()
    if len(s) == n and sum(i != j for i, j in zip(s, name)) < 2:
        print(count)
        break