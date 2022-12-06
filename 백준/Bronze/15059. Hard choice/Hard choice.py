Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
print(max(Cr - Ca, 0) + max(Br - Ba, 0) + max(Pr - Pa, 0))