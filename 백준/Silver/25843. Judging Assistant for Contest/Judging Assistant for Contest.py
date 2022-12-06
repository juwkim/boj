def solve():
    name = input()
    l = input().split('.')
    if len(l) != 2:
        return 'Compile Error'
    filename, ext = l    
    if name != filename or ext not in ['c', 'cpp', 'java', 'py']:
        return 'Compile Error'
    r, d, e = map(int, input().split())
    if r:
        return 'Run-Time Error'
    if e > d:
        return 'Time Limit Exceeded'
    c = int(input())
    ans = iter([input() for _ in range(c)])
    t = int(input())
    if c != t or any(input() != next(ans) for _ in range(t)):
        return 'Wrong Answer'
    return 'Correct'
print(solve())