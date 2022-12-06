res = [1, 1, 1]
for i in range(int(input())-3):
    res.append(res[-1] + res[-3])
print(res[-1])