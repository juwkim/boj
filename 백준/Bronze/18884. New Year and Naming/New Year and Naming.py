n, m = map(int, input().split())
front, rear = input().split(), input().split()
for _ in range(int(input())):
    s = int(input()) - 1
    print(front[s%n] + rear[s%m])