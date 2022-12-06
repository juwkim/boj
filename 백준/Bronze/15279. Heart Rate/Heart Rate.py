for _ in range(int(input())):
    b, p = map(float, input().split())
    BPM = map(lambda x: x*60/p, [b-1, b, b+1])
    print(*BPM)