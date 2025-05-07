N, *nums = map(int, open(0))
ans, st = 0, []
for num in nums:
    if not st:
        st.append([num, 1])
    else:
        while st:
            prv, cnt = st[-1]
            if prv > num:
                ans += 1
                st.append([num, 1])
                break
            if prv == num:
                ans += cnt + (len(st) >= 2)
                st[-1][1] += 1
                break
            ans += cnt
            st.pop()
        else:
            st.append([num, 1])
print(ans)