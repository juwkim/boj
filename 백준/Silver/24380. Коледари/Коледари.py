k, n, *a = map(int, open(0).read().split())

mod_index = {0: -1}
prefix = 0

for i in range(n):
    prefix += a[i]
    mod = prefix % k

    if mod in mod_index:
        start = mod_index[mod] + 1
        end = i + 1
        print(' '.join(str(idx + 1) for idx in range(start, end)))
        break
    else:
        mod_index[mod] = i
else:
    print("no kravaiche")