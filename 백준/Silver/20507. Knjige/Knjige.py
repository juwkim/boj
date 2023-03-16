def get(hand, shelf):
    global l, r
    if hand == 'L':
        if shelf == 'L':
            l = A.pop()
        else:
            l = B.pop()
    else:
        if shelf == 'L':
            r = A.pop()
        else:
            r = B.pop()
    ans.append(f'UZMI {hand} {shelf}')

def put(hand, shelf):
    global l, r
    if hand == 'L':
        if shelf == 'L':
            A.append(l)
            l = None
        else:
            B.append(l)
            l = None
    else:
        if shelf == 'L':
            A.append(r)
            r = None
        else:
            B.append(r)
            r = None
    ans.append(f'STAVI {hand} {shelf}')

N = int(input())
A, B = [*map(int, input().split())][::-1], []

l, r = None, None
ans = []

for _ in range(N):
    get('L', 'L')
    put('L', 'D')

for _ in range(N):
    idx = max(range(len(B)), key=lambda x: (B[x], x))
    cnt = len(B) - (idx + 1)
    for i in range(cnt):
        get('L', 'D')
        put('L', 'L')
    get('D', 'D')
    for i in range(cnt):
        get('L', 'L')
        put('L', 'D')
    put('D', 'L')
print(len(ans))
for op in ans:
    print(op)