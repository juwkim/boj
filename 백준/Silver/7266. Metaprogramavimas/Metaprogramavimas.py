import sys
input = sys.stdin.readline

N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
if N == 1:
    a, b = nums[0]
    if a == b:
        print(f"1\nprint")
    elif b >= a:
        print(f"2\nadd {b - a}\nprint")
    else:
        print(f"3\nmultiply 0\nadd {b}\nprint")
else:
    (x1, y1), (x2, y2) = nums[:2]
    if any((x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1) for x3, y3 in nums[2:]):
        print(-1)
    else:
        num1 = (y2 - y1) // (x2 - x1)
        assert (y2 - y1) % (x2 - x1) == 0
        num2 = y1 - num1 * x1
        if num1 < 0 or num2 < 0:
            print(-1)
        elif num2:
            print(f"3\nmultiply {num1}\nadd {num2}\nprint")
        else:
            print(f"2\nmultiply {num1}\nprint")