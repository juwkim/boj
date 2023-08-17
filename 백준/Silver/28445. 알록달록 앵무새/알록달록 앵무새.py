colors = sorted(set(input().split() + input().split()))
for i in range(len(colors)):
    for j in range(len(colors)):
        print(colors[i], colors[j])