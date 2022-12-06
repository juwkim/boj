for _ in range(int(input())):
    nums = [*map(int, input().split())]
    total, even = map(sum, [nums[1:], filter(lambda x: x%2 == 0, nums[1:])])
    print('EVEN' if 2*even > total else 'ODD' if 2*even < total else 'TIE')