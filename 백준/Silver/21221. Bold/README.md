# [Silver V] Bold - 21221 

[문제 링크](https://www.acmicpc.net/problem/21221) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation)

### 문제 설명

<p>In addition to the usual age-related health problems such as first signs of RSI<sup>1</sup> and physical injuries that accumulate faster than they heal, Daniel’s eyesight has suddenly worsened.</p>

<p>Paula wrote him a letter, but he can’t read it without glasses. She needs to <strong>bold</strong> the text, so Daniel can read it.</p>

<p>The letter can be represented as a matrix consisting of characters '<code>.</code>' and '<code>#</code>'. To bold it, Paula will replace each '<code>#</code>' in the original letter with a 2 × 2 square of '<code>#</code>' in the down-right direction.</p>

<p><sup>1</sup>Repetitive strain injury. Never ignore the pain caused by typing. Ergonomic aids and chairs are generally always worth it. Sit straight. “A gram of prevention is worth a kilo of cure.”</p>

### 입력 

 <p>The first line contains integers n and m (2 ≤ n, m ≤ 100), the dimensions of the letter.</p>

<p>Each of the following n lines contains m characters '<code>.</code>' and '<code>#</code>' that represent Paula’s letter.</p>

<p>The last row and column won’t contain any '<code>#</code>'.</p>

### 출력 

 <p>Output n lines containing m characters '<code>.</code>' and '<code>#</code>', representing the bold letter.</p>

