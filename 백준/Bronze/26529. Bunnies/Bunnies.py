d = [1, 1]
for _ in range(44):
    d.append(d[-2] + d[-1])
for _ in range(int(input())):
    print(d[int(input())])