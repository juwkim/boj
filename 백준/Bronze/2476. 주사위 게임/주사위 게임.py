import sys
N = int(input())
array = [sorted(map(int, input().split())) for _ in range(N)]
check_1 = [dice for dice in array if len(set(dice)) == 1]
check_2 = [dice for dice in array if len(set(dice)) == 2]
check_3 = [dice for dice in array if len(set(dice)) == 3]
if check_1:
    print(10000 + 1000 * max([dice[1] for dice in check_1]))
elif check_2:
    print(1000 + 100 * max([dice[1] for dice in check_2]))
else:
    print(100 * max([dice[2] for dice in check_3]))