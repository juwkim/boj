ans = [input()]
t1, t2 = [*ans[0]], [*input()]
order = 4, 3, 1, 0
if t1[0] == '2' and t2[0] != '2': order = 4, 3, 0, 1
for i in order:
    t1[i], t2[i] = int(t1[i]), int(t2[i])
    if i in (1, 4):
        while t1[i] != t2[i]:
            t1[i] = (t1[i] + (-1, 1)[(t2[i] - t1[i]) % 10 < 5]) % 10
            ans.append("".join(map(str, t1)))
    else:
        while t1[i] != t2[i]:
            t1[i] += (-1, 1)[t1[i] < t2[i]]
            ans.append("".join(map(str, t1)))
print(len(ans))
for l in ans: print(*l, sep='')