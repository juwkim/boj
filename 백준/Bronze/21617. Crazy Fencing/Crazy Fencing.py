N = int(input())
heights = [*map(int, input().split())]
widths = [*map(int, input().split())]
print(sum(sum(heights[i:i+2]) * widths[i] for i in range(N)) / 2)