buf = []
if input() == 'L':
    d = "RIGHT"
else:
    d = "LEFT"
buf.append(f"Turn {d} into your HOME.")

while True:
    street = input()
    if street == "SCHOOL":
        break
    if input() == 'L':
        d = "RIGHT"
    else:
        d = "LEFT"
    buf.append(f"Turn {d} onto {street} street.")

for line in reversed(buf):
    print(line)   