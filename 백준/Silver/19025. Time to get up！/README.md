# [Silver IV] Time to get up! - 19025 

[문제 링크](https://www.acmicpc.net/problem/19025) 

### 성능 요약

메모리: 116248 KB, 시간: 372 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Little Q's alarm is ringing! It's time to get up now! However, after reading the time on the clock, Little Q lies down and starts sleeping again. Well, he has five alarms, and it's just the first one, he can continue sleeping for a while.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 320px; height: 48px;"></p>

<p>Little Q's clock uses a standard 7-segment LCD display for all digits, plus two small segments for the "<code>:</code>", and shows all times in 24-hour format. The "<code>:</code>" segments are on at all times.</p>

<p>Your job is to help Little Q read the time shown on his clock.</p>

### 입력 

 <p>The first line of the input contains an integer $T$: the number of test cases ($1 \leq T \leq 1440$).</p>

<p>Each test case is given on seven lines as a $7 \times 21$ ASCII image of the clock screen.</p>

<p>Each digit segment is represented by two characters, and each colon segment is represented by one character. Character "<code>X</code>" indicates a lit segment, character "<code>.</code>" indicates a dark segment or empty space. See the sample input for details.</p>

### 출력 

 <p>For each test case, print a single line containing a string $t$ formatted as "<code>HH:MM</code>": the time shown on the clock ($\texttt{00:00} \leq t \leq \texttt{23:59}$).</p>

