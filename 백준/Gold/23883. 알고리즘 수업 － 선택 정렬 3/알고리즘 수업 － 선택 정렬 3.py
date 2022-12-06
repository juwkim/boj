g = lambda: [*map(int, input().split())]
def selection_sort():
    cnt = 0
    for last in range(N-1, 0, -1):
        num = B[last-N][0]
        i = dic[num]
        if num != A[last]:

            dic[A[i]] = last
            dic[A[last]] = i
            A[last], A[i] = A[i], A[last]
            cnt += 1
            if cnt == K:
                print(A[i], A[last])
                return
    print(-1)
    return
        
N, K = map(int, input().split())
A = g()
B = sorted((num, idx) for idx, num in enumerate(A))
dic = dict(B)
selection_sort()