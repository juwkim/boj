pics = [input() for _ in range(int(input()))]
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a - 1, b):
        print(pics[i])