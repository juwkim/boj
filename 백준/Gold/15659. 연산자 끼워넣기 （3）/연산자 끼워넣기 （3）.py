g = lambda: [*map(int, input().split())]

N = int(input())
nums = input().split()
plus, sub, mul, div = g()

Min, Max = 1e9, -1e9
ops = []
def solve(step, p, s, m, d):
    global Min, Max
    if step == N:
        buf = []
        for num, op in zip(nums, ops):
            buf.append(num)
            buf.append(op)
        buf.append(nums[-1])
        num = eval(''.join(buf))
        Min = min(Min, num)
        Max = max(Max, num)
        return
    
    if p < plus:
        ops.append('+')
        solve(step + 1, p + 1, s, m, d)
        ops.pop()
    if s < sub:
        ops.append('-')
        solve(step + 1, p, s + 1, m, d)
        ops.pop()
    if m < mul:
        ops.append('*')
        solve(step + 1, p, s, m + 1, d)
        ops.pop()
    if d < div:
        ops.append('//')
        solve(step + 1, p, s, m, d + 1)
        ops.pop()
    
solve(1, 0, 0, 0, 0)
print(Max, Min)