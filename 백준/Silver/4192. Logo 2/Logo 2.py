from math import radians, cos, sin, dist

def process(cmd, num):
	global x, y, angle
	match cmd:
		case "fd":
			x += num * cos(angle)
			y += num * sin(angle)
		case "bk":
			x -= num * cos(angle)
			y -= num * sin(angle)
		case "lt":
			angle += radians(num)
		case "rt":
			angle -= radians(num)

for tc in range(int(input())):
	x, y, angle = 0, 0, 0
	N = int(input())
	while N:
		N -= 1
		cmd, num = input().split()
		if num == '?':
			what = cmd
			break
		process(cmd, int(num))
	buf = [input().split() for _ in range(N)]
	if what in ("fd", "bk"):
		for cmd, num in buf:
			process(cmd, int(num))
		ans = round(dist((0, 0), (x, y)))
	else:
		mem_x, mem_y, mem_angle = x, y, angle
		ans, min_dist = None, float('inf')
		for dangle in range(360):
			x, y, angle = mem_x, mem_y, mem_angle + radians(dangle)
			for cmd, num in buf:
				process(cmd, int(num))
			if dist((0, 0), (x, y)) < min_dist:
				ans = dangle
				min_dist = dist((0, 0), (x, y))
		if what == 'rt':
			ans = 360 - ans
	print(ans)