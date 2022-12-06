g = lambda: [*map(int, input().split())]
for i in range(1, 1 + int(input())):
    nums = g()
    M = 0
    for j in range(5):
        if j == 3:
            M = 18 * M + nums[j]
        else:
            M = 20 * M + nums[j]
    J = int(input())
    diff = J - M + 13*20*20*18*20 - 2456054
    if diff < 0:
        msg = "It's a hoax!\n"
    elif diff == 0:
        msg = "Panic!\n"
    else:
        msg = f"{diff}\n"
    print(f'Data Set {i}:')
    print(msg)