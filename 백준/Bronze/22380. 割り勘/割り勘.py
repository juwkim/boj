while (s:= input()) != '0 0':
    N, M = map(int, s.split())
    print(sum(min(i, M//N) for i in map(int, input().split())))