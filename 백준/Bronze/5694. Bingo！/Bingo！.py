g = lambda: [*map(int, input().split())]


while sum(s:= g()):
    N, B = s
    nums = g()
    check = {nums[i] - nums[j] for i in range(B) for j in range(B)}
    if all(num in check for num in range(N+1)):
        print('Y')
    else:
        print('N')