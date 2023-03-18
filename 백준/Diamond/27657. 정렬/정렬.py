from collections import deque

N = int(input())
A = deque(map(int, input().split()))
B = deque()

is_merge_entered = False
def devide(size):
    global is_merge_entered
    if size <= 1:
        return
    if all(A[i] < A[i + 1] for i in range(size - 1)):
        return
    if size == 2:
        if A[0] > A[1]:
            ro0()
            pp01()
            rro0()
            pp10()
        return
    v = sorted(A[i] for i in range(size))
    small_idx = 40 * size // 100
    big_idx = 60 * size // 100
    small_pivot = v[small_idx]
    big_pivot = v[big_idx]
    
    pp_cnt, ro_A_cnt, ro_B_cnt = 0, 0, 0
    small_cnt = 0
    while pp_cnt != big_idx + 1:
        if A[0] > big_pivot:
            ro_A_cnt += ro0()
        else:
            pp_cnt += pp01()
            if small_cnt == small_idx + 1:
                continue
            elif B[0] > small_pivot:
                ro_B_cnt += ro1()
            else:
                small_cnt += 1
    if is_merge_entered == False:
        ro_A_cnt = 0;
    restore(ro_A_cnt, ro_B_cnt)
    devide(size - (big_idx + 1))
    is_merge_entered = True;
    merge(big_idx - small_idx)
    merge(small_idx + 1)

def merge(size):
    if size == 0:
        return
    if size == 1:
        pp10()
        return
    if size == 2:
        if B[0] > B[1]:
            pp10()
            pp10()
        else:
            ro1()
            pp10()
            rro1()
            pp10()
        return
    
    if all(B[i] > B[i + 1] for i in range(size - 1)):
        for i in range(size):
            pp10()
        return
    v = sorted(B[i] for i in range(size))
    small_idx = 2 * size // 5
    big_idx = 3 * size // 5
    small_pivot = v[small_idx]
    big_pivot = v[big_idx]
    
    pp_cnt, ro_A_cnt, ro_B_cnt = 0, 0, 0
    while pp_cnt != size - small_idx:
        if B[0] < small_pivot:
            ro_B_cnt += ro1()
        else:
            pp_cnt += pp10()
            if A[0] < big_pivot:
                ro_A_cnt += ro0()
    
    devide(size - big_idx)
    restore(ro_A_cnt, ro_B_cnt)
    devide(big_idx - small_idx)
    merge(small_idx)

def restore(ro_A_cnt, ro_B_cnt):
    for i in range(ro_A_cnt):
        rro0()
    if len(B) != ro_B_cnt:
        for i in range(ro_B_cnt):
            rro1()

def pp01():
    B.appendleft(A.popleft())
    buf.append("PP 0 1")
    return 1

def pp10():
    A.appendleft(B.popleft())
    buf.append("PP 1 0")
    return 1

def ro0():
    A.rotate(-1)
    buf.append("RO 0")
    return 1

def ro1():
    B.rotate(-1)
    buf.append("RO 1")
    return 1

def rro0():
    A.rotate(1)
    buf.append("RRO 0")
    return 1

def rro1():
    B.rotate(1)
    buf.append("RRO 1")
    return 1
    
buf = []
devide(N)

print(len(buf))
print(*buf)