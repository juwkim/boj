input()
nums = input().split()
Y = sum(map(lambda x: 10 * (1 + int(x)//30), nums))
M = sum(map(lambda x: 15 * (1 + int(x)//60), nums))
if Y == M:
    print('Y M', Y)
elif Y > M:
    print('M', M)
else:
    print('Y', Y)