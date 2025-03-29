tones = "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
dic = {t: i for i, t in enumerate(tones)}

def parse_tone(tone):
    i = 1 + (tone[1] == "#")
    return int(tone[i:]) * 12 + dic[tone[:i]]

n = int(input())
low, high = map(parse_tone, input().split())
cnt = [0] * 12
Min, Max = float('inf'), float('-inf')
for tone in map(parse_tone, input().split()):
    cnt[tone % 12] += 1
    Min, Max = min(Min, tone), max(Max, tone)

l = [float("inf")] * 12
for k in range(low - Min, min(low - Min + 12, high - Max + 1)):
    num = sum(cnt[i] for i in range(12) if (i + k) % 12 in (1, 3, 6, 8, 10))
    l[k % 12] = num

q, r = divmod(high - Max + 1 - low + Min, 12)
check = [num % 12 for num in range((low - Min) % 12, (low - Min) % 12 + r)]
num = min(l)
ans = sum(q + (i in check) for i in range(12) if l[i] == num)
print(num, ans)