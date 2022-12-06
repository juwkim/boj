N = int(input())
trees = sorted([*map(int, input().split())], reverse=True)
for i in range(N):
    trees[i] += i + 2
print(max(trees))