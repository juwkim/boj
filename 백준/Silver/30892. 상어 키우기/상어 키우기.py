N, K, T, *A = map(int, open(0).read().split())
A.sort()
j = 0
st = []
for i in range(K):
    while j < N and A[j] < T:
        st.append(A[j])
        j += 1
    if not st:
        break
    T += st.pop()
print(T)