import sys
input = lambda: sys.stdin.readline().rstrip()

while (line:=input()) != "0 0":
    n, l = map(int, line.split())
    ants = [[] for _ in range(l)]
    for i in range(1, n + 1):
        d, p = input().split()
        ants[int(p)].append((d, i))
    def solve(n, ants):
        time = 0
        while n:
            time += 1
            new_ants = [[] for _ in range(l)]
            for pos in range(l - 1, 0, -1):
                for j in range(len(ants[pos])):
                    d, i = ants[pos][j]
                    if d == "L":
                        if pos == 1:
                            n -= 1
                            if n == 0:
                                return time, i
                        else:
                            new_ants[pos - 1].append([d, i])
                    elif pos == l - 1:
                        n -= 1
                        if n == 0:
                            return time, i
                    else:
                        new_ants[pos + 1].append([d, i])
            for pos in range(1, l):
                if len(new_ants[pos]) != 2:
                    continue
                for j in range(2):
                    if new_ants[pos][j][0] == "L":
                        new_ants[pos][j][0] = "R"
                    else:
                        new_ants[pos][j][0] = "L"
            ants = new_ants
    print(*solve(n, ants))