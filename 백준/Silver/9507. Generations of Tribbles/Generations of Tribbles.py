res = [0, 1, 1, 2, 4]
for i in range(64):
    res.append(2 * res[-1] - res[-5])
for i in range(int(input())):
    print(res[1 + int(input())])