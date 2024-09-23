N = int(input())
if N == 0:
    print("*")
elif N == 1:
    print("**")
    print("*")
else:
    a = ["****", "* * ", "**  ", "*   "]
    for _ in range(N - 2):
        for i in range(len(a)):
            a.append(a[i] + " " * len(a[i]))
            a[i] += a[i]
    for l in a:
        print(l.rstrip())