import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dic = {
    "063": "0",
    "010": "1",
    "093": "2",
    "079": "3",
    "106": "4",
    "103": "5",
    "119": "6",
    "011": "7",
    "127": "8",
    "107": "9"
}
redic = {v: k for k, v in dic.items()}
while (s:=input()) != "BYE":
    i = s.index("+")
    A, B = s[:i], s[i+1:-1]
    a = "".join(dic[A[i:i+3]] for i in range(0, len(A), 3))
    b = "".join(dic[B[i:i+3]] for i in range(0, len(B), 3))
    c = str(int(a) + int(b))
    ans = "".join(redic[i] for i in c)
    print(f"{s}{ans}")