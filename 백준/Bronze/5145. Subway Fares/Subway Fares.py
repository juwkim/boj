for cnt in range(1, 1 + int(input())):
    n = int(input())
    cost = [int(input()) for _ in range(n - 1)]
    station = {input(): i for i in range(n)}

    start = input()
    end = input()
    ans = cost[abs(station[start] - station[end]) - 1]
    print(f'Data Set {cnt}:\n{ans}\n')