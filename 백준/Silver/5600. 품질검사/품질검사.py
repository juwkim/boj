import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a, b, c = g()
state = [2] * (a + b + c + 1)
nums = []
for _ in range(int(input())):
    i, j, k, r = g()
    if r:
        state[i], state[j], state[k] = 1, 1, 1
    else:
        nums.append((i, j, k))
for i, j, k in nums:
    if state[i] == 1 and state[j] == 1:
        state[k] = 0
    elif state[i] == 1 and state[k] == 1:
        state[j] = 0
    elif state[j] == 1 and state[k] == 1:
        state[i] = 0
for i in range(1, a + b + c + 1):
    print(state[i])