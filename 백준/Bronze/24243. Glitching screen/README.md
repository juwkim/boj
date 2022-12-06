# [Bronze I] Glitching screen - 24243 

[문제 링크](https://www.acmicpc.net/problem/24243) 

### 성능 요약

메모리: 30840 KB, 시간: 468 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Petter is taking the local train in a new city for the first time. He is well prepared and have memorized the names of all the stops. However, some of the pixels on the monitor that displays the upcoming stop are broken. Can you help him decide what the next stop is?</p>

### 입력 

 <p>The first line of input consists of three integers $1 \leq h \leq 100$, $1 \leq w \leq 100$ and $1 \leq n \leq 100$, the height and width of the screen in pixels and the number of train stops, respectively. Then there are $h \cdot n$ lines, where line $i\cdot h$ to $i\cdot h + h - 1$ shows how train stop $i$ is rendered on a fully functioning screen (for stops $i \in \{0, 1, 2, \ldots, n-1\}$). The input ends with $h$ more lines that shows the current screen. Pixels on the screen that are turned on are denoted by <code>x</code> and pixels that are turned off are denoted by a period (<code>.</code>). If a screen is broken, it means that one or more of the pixels are always off.</p>

### 출력 

 <p>Output <code>yes</code> if you can tell him what the next stop is, and <code>no</code> otherwise.</p>

