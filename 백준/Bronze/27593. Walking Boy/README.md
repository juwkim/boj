# [Bronze II] Walking Boy - 27593 

[문제 링크](https://www.acmicpc.net/problem/27593) 

### 성능 요약

메모리: 114328 KB, 시간: 136 ms

### 분류

구현(implementation)

### 문제 설명

<p>One of the SWERC judges has a dog named Boy. Besides being a good competitive programmer, Boy loves fresh air, so she wants to be walked at least twice a day. Walking Boy requires $120$ <strong>consecutive</strong> minutes. Two walks cannot overlap, but one can start as soon as the previous one has finished.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 350px; height: 229px;"></p>

<p style="text-align: center;">Boy before and after getting ACCEPTED on this problem.</p>

<p>Today, the judge sent $n$ messages to the SWERC Discord server. The $i$-th message was sent $a_i$ minutes after midnight. You know that, when walking Boy, the judge does not send any messages, but he can send a message right before or right after a walk. Is it possible that the judge walked Boy at least twice today?</p>

<p>Note that a day has $1440$ minutes, and a walk is considered to happen <em>today</em> if it starts at a minute $s ≥ 0$ and ends right before a minute $e ≤ 1440$. In that case, it must hold that $e - s = 120$ and, for every $i = 1, 2, \dots , n$, either $a_i ≤ $s or $a_i ≥ e$.</p>

<p> </p>

### 입력 

 <p>Each test contains multiple test cases. The first line contains an integer $t$ ($1 ≤ t ≤ 100$) — the number of test cases. The descriptions of the $t$ test cases follow.</p>

<p>The first line of each test case contains an integer $n$ ($1 ≤ n ≤ 100$) — the number of messages sent by the judge.</p>

<p>The second line of each test case contains $n$ integers $a1_, a_2, \dots , a_n$ ($0 ≤ a_1 < a_2 < \cdots < a_n < 1440$) — the times at which the messages have been sent (in minutes elapsed from midnight).</p>

### 출력 

 <p>For each test case, output one line containing <code>YES</code> if it is possible that Boy has been walked at least twice, and <code>NO</code> otherwise.</p>

