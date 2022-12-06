g = lambda: [*map(int, input().split())]
cnt = 0
def selection_sort(A):
    global cnt
    for last in range(N-1, 0, -1):
        i = A.index(max(A[:last+1]))
        if last != i:
            A[last], A[i] = A[i], A[last]
            cnt += 1
            if cnt == K:
                print(A[i], A[last])
                return
    print(-1)
        
        
N, K = map(int, input().split())
nums = g()
selection_sort(nums)