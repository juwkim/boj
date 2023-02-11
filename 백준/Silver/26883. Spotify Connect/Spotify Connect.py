import sys
import itertools

def solve(lines):
    def resolve_device(line):
        if line[1] == 'mobile':
            return (line[0] + 100, line[2])
        else:
            return (line[0], line[2])
    time_actions = sorted(map(resolve_device, lines))
    result = 0
    play_time = -1
    pause_time = 0
    for (time, action) in time_actions:
        if play_time > pause_time:
            result += time - play_time
        if action == 'play':
            play_time = time
        else:
            pause_time = time
    return result

if __name__ == '__main__':
    # N,M = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    raw_lines = sys.stdin.readlines()
    def parse_line(line):
        segs = line.split(' ')
        segs[0] = int(segs[0])
        segs[2] = segs[2].rstrip()
        return segs
    lines = map(parse_line, raw_lines)
    print(solve(lines))