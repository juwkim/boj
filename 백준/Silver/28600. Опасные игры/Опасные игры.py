n = int(input())
top, bottom = 1, n
left, right = 1, n
while True:
    x = top + bottom >> 1
    y = left + right >> 1
    print(x, y, flush=True)
    response = input()
    if response == "OK":
        break
    if response[0] == 'N':
        bottom = x - 1
    elif response[0] == 'S':
        top = x + 1
    if "W" in response:
        right = y - 1
    elif "E" in response:
        left = y + 1