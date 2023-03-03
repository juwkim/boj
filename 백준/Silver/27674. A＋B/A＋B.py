for _ in range(int(input())):
    input()
    *nums, b = sorted(map(int, input()), reverse=True)
    a = 0
    for num in nums:
        a = a * 10 + num
    print(a + b)