graph = ((), (2, 9), (1, 3), (2, 4, 11), (3, 5), (4, 6, 13), (5, 7), (6, 15), (9, 18), (1, 8, 10), (9, 11, 20), (3, 10, 12), (11, 13, 22), (5, 12, 14), (13, 15, 24), (7, 14, 16), (15, 26), (18, 28), (8, 17, 19), (18, 20, 30), (10, 19, 21), (20, 22, 32), (12, 21, 23), (22, 24, 34), (14, 23, 25), (24, 26, 36), (16, 25, 27), (26, 38), (17, 29), (28, 30, 39), (19, 29, 31), (30, 32, 41), (21, 31, 33), (32, 34, 43), (23, 33, 35), (34, 36, 45), (25, 35, 37), (36, 38, 47), (27, 37), (29, 40), (39, 41, 48), (31, 40, 42), (41, 43, 50), (33, 42, 44), (43, 45, 52), (35, 44, 46), (45, 47, 54), (37, 46), (40, 49), (48, 50), (42, 49, 51), (50, 52), (44, 51, 53), (52, 54), (46, 53))

tc = 1
while (s:=input()) != '0':
    nums = [*map(int, s.split())]
    first, second = nums[:6], nums[6:]
    occupied = set(nums)
    ans = "FREE"
    for x in first:
        for nx in graph[x]:
            if nx in occupied:
                continue
            occupied.add(nx)
            occupied.remove(x)
            for y in second:
                if all(num in occupied for num in graph[y]):
                    ans = "TRAPPED"
                    break
            else:
                occupied.remove(nx)
                occupied.add(x)
                continue
            break
        else:
            continue
        break
    print(f"{tc}. {ans}")
    tc += 1