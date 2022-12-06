num = input()
diff = [0] + [int(j) - int(i) for i, j in zip(num, num[1:])] + [0]
count = 0
for i in range(len(diff) - 3):
    if diff[i] != 1 and diff[i+3] != 1 and diff[i+1] == 1 and diff[i+2] == 1:
        count += 1
print(count)