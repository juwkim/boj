import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(1, 1 + int(input())):
    a = int(input())
    a_set = set([input().split() for _ in range(4)][a-1])
    
    b = int(input())
    b_set = set([input().split() for _ in range(4)][b-1])
    
    c_set = a_set & b_set
    if len(c_set) == 1:
        ans = c_set.pop()
    elif len(c_set) > 1:
        ans = 'Bad magician!'
    else:
        ans = 'Volunteer cheated!'
    print(f'Case #{_}:', ans)