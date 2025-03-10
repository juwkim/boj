while True:
    N, *l, cnt = input().split()
    N, cnt = int(N), int(cnt)
    if N < 0:
        break
    nums = [0] * (N + 1)
    for _ in range(cnt):
        m, r = input().split()
        nums[int(m)] = 1 - float(r)
    for i in range(1, N + 1):
        if not nums[i]:
            nums[i] = nums[i - 1]
    first, loan = map(float, l)
    car = (loan + first) * nums[0]
    monthly = loan / N
    i = 0
    while car <= loan:
        i += 1
        loan -= monthly
        car *= nums[i]
    if i == 1:
        print(f"{i} month")
    else:
        print(f"{i} months")