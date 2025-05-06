for l in [*open(0)][:-1]:
    l = l.rstrip()
    def solve():
        buf = []
        for i in range(1, int(len(l)**.5) + 1):
            q, r = divmod(len(l), i)
            if r:
                continue
            buf.append(q)
            pattern = l[:i]
            if all(l[j:j+i] == pattern for j in range(i, len(l), i)):
                return q
        while buf:
            i = buf.pop()
            pattern = l[:i]
            if all(l[j:j+i] == pattern for j in range(i, len(l), i)):
                return len(l) // i
    print(solve())