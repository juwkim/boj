# [Bronze II] Up and Down - 6795 

[문제 링크](https://www.acmicpc.net/problem/6795) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>Nikky and Byron are playing a silly game in gym class.</p>

<p>Nikky is told by his teacher to walk forward a steps (1 ≤ a ≤ 100) and then walk backward b steps (1 ≤ b ≤ 100), after which he repeats a forward, b backward, etc. Likewise, Byron is told to walk forward c steps (1 ≤ c ≤ 100) and then walk backward d steps (1 ≤ d ≤ 100), after which he repeats c forward, d backward, etc. You may assume that a ≥ b and c ≥ d.</p>

<p>Byron and Nikky have the same length of step, and they are required to take their steps simultaneously (that is, Nikky and Byron will both step forward on their first steps at the same time, and this will continue for each step).</p>

<p>Nikky and Byron start walking from one end of a soccer field. After s steps (1 ≤ s ≤ 10000), the gym teacher will blow the whistle. Your task is to figure out who has moved the farthest away from the starting position when the whistle is blown.</p>

### 입력 

 <p>The input will be the 5 integers a, b, c, d, and s, each on a separate line.</p>

### 출력 

 <p>The output of your program will be one of three possibilities: <code>Nikky</code> if Nikky is farther ahead after s steps are taken; <code>Byron</code> if Byron is farther ahead after s steps are taken; <code>Tied</code> if Byron and Nikky are at the same distance from their starting position after s steps are taken.</p>

