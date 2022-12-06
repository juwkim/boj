# [Bronze III] Math Homework - 24807 

[문제 링크](https://www.acmicpc.net/problem/24807) 

### 성능 요약

메모리: 30840 KB, 시간: 104 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Since entering 2nd grade Theta has daily math homework sheets. The problems on her worksheet usually go like this:</p>

<blockquote>
<p>There is a certain number of birds, dogs, and cats on a farm.  Together they have $14$ legs.  How many birds, dogs, and cats could there be? Write down as many answers as you can!</p>
</blockquote>

<p>It is always the same problem, just written in different ways: sometimes with horses, cows, sheep, goats, chickens, beetles, or even spiders (but never with snakes or fishes!)</p>

<p>Can you write a program to double-check Theta's answers?</p>

### 입력 

 <p>Input consists of a single line with $4$ integers: $b$, $d$, $c$, and $l$, with $b$, $d$, and $c$ representing the numbers of legs the first, second, and third type of animal has. You are given that $0 < b, c, d \le 100$ because some farm animals in these math problems may be centipedes. The total number of legs is given by $l$ ($0 \le l \le 250$).</p>

### 출력 

 <p>Output all possible answers, each on a separate line, in lexicographical order so that they are sorted by the number of the first animal, ties broken by the second and third animal, respectively.  Separate the number of the first, second, and third animal with spaces. If there are no possible solutions, output <code>impossible</code> on a single line!</p>

