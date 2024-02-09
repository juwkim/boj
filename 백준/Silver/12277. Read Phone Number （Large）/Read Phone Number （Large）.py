import sys
input = sys.stdin.readline

dic = {
    2: 'double', 3: 'triple', 4: 'quadruple', 5: 'quintuple',
    6: 'sextuple', 7: 'septuple', 8: 'octuple', 9: 'nonuple', 10: 'decuple'
}
number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for tc in range(1, 1 + int(input())):
    N, F = input().split()
    ans, i = [], 0
    for num in map(int, F.split('-')):
        prev, *s = map(int, N[i:i+num])
        cnt = 1
        for c in s + ['-']:
            if c == prev:
                cnt += 1
            else:
                if cnt == 1:
                    ans.append(number[prev])
                elif cnt <= 10:
                    ans.extend([dic[cnt], number[prev]])
                else:
                    ans.extend([number[prev]] * cnt)
                prev, cnt = c, 1
        i += num
    print(f"Case #{tc}:", *ans)