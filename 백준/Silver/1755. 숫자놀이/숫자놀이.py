g = lambda: [*map(int, input().split())]
nums = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

M, N = g()
ans = sorted(range(M, N + 1), key=lambda x: ' '.join(nums[i] for i in str(x)))
for i in range(0, len(ans), 10):
    print(*ans[i:i+10])