import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, q = g()
roles = g()
principal = 0
while roles[principal]: principal += 1
unread = [set() for _ in range(n)]
student_to_teacher = set()
for i in range(q):
    cmd, a, *l = g()
    a -= 1
    match cmd:
        case 1:
            b = l[0] - 1
            if roles[a] == 1 and roles[b] == 2:
                unread[principal].add(i)
                unread[b].add(i)
            elif roles[a] == 2 and roles[b] == 1:
                unread[principal].add(i)
                student_to_teacher.add(i)
            else:
                unread[b].add(i)
        case 2:
            x = l[0] - 1
            if roles[a] == 1 and x in student_to_teacher:
                student_to_teacher.remove(x)
            else:
                unread[a].remove(x)
        case 3:
            ans = len(unread[a])
            if roles[a] == 1:
                ans += len(student_to_teacher)
            print(ans)