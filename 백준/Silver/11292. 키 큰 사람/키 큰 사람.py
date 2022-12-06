while N:= int(input()):
    names = []
    heights = []
    for _ in range(N):
        name, height = input().split()
        height = float(height)
        names.append(name)
        heights.append(height)
    Max = max(heights)
    ans = [names[i] for i in range(N) if heights[i] == Max]
    print(*ans)