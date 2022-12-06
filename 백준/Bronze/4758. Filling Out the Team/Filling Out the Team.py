while True:
    a, b, c = map(float, input().split())
    position = ''
    if (a, b, c) == (0, 0, 0):
        break
    if a <= 4.5 and b >= 150 and c >= 200:
        position += 'Wide Receiver '
    if a <= 6.0 and b >= 300 and c >= 500:
        position += 'Lineman '
    if a <= 5.0 and b >= 200 and c >= 300:
        position += 'Quarterback '
    print(position if len(position) else 'No positions')