# [Bronze I] Alarm Clock - 10372 

[문제 링크](https://www.acmicpc.net/problem/10372) 

### 성능 요약

메모리: 121220 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Alice likes her digital alarm clock. She sets them up every evening. Last night Alice had a dream about her clock. Unfortunately, the only thing she is able to remember is the number of highlighted segments of the clock. Alice wonders what time was set on the clock in her dream.</p>

<p>Alice’s clock have four digits: two for hours and two for minutes. For example, the clock below shows 9:30 (note the leading zero).</p>

<p style="text-align:center"><img alt="" src="" style="height:69px; width:149px"></p>

<p>The clock uses following digit representation.</p>

<p style="text-align:center"><img alt="" src="" style="height:69px; width:395px"></p>

### 입력 

 <p>The only line of the input file contains single integer n — the number of highlighted segments of the clock in Alice’s dream (0 ≤ n ≤ 30).</p>

### 출력 

 <p>Output five characters in “hh:mm” format — the time shown on the clock in Alice’s dream. The time must be correct: 0 ≤ hh < 24 and 0 ≤ mm < 60. If there are many possible correct times, output any of them. If there is none, output “Impossible”.</p>

