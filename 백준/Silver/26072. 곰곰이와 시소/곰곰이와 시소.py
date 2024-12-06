g=lambda:[*map(int, input().split())]
(N,L),x,w=g(),g(),g()
print(sum(x[i]*w[i]for i in range(N))/sum(w))