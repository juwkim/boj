N, V, Z, T = map(int, input().split())
done, r = divmod(T, V)
ans = 0
for i in range(1, N + 1):
    if done < i:
        ans += V - r
        done += 1
        r = 0
    q, r = divmod(Z + r, V)
    done += q
print(ans)