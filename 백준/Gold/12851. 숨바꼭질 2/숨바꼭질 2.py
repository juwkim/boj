g = lambda: [*map(int, input().split())]


N, K = g()
if K > N:
    visited = bytearray(100001)
    visited[N] = 1
    dic = {N: 1}
    
    ans = 0
    end = False
    while True:
        new_dic = {}
        for num in dic:
            if num == K:
                print(ans, dic[num])
                end = True
                break

            for pos in (num + 1, num - 1, num * 2):
                if 0 <= pos < 100001:
                    if visited[pos] == 0:
                        visited[pos] = 1
                        new_dic[pos] = dic[num]
                    elif new_dic.get(pos):
                        new_dic[pos] += dic[num]
        if end:
            break
        dic = new_dic
        ans += 1
else:
    print(N - K, 1)