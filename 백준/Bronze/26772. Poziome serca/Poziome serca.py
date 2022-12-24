S = [' @@@   @@@ ', '@   @ @   @', '@    @    @', '@         @', ' @       @ ', '  @     @  ', '   @   @   ', '    @ @    ', '     @     ']
N = int(input())
for line in S:
    print(' '.join([line] * N))  