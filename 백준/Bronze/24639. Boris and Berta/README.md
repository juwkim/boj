# [Bronze I] Boris and Berta - 24639 

[문제 링크](https://www.acmicpc.net/problem/24639) 

### 성능 요약

메모리: 114328 KB, 시간: 116 ms

### 분류

수학(math)

### 문제 설명

<p>Boris is making a quest for his sister Berta. One of the tasks is to find a point on the map that is $n$ meters to the north from their house. But it's too easy if $n$ is specified directly. Boris decided to use miles and cables to specify the distance.</p>

<p>He found out that there are a lot of different miles: from a $500$-meter Chinese mile (called <em>li</em>) up to a $11\,299$-meter Norwegian mile (called <em>mil</em>). And a cable length can be anywhere from $169$ to $220$ meters.</p>

<p>Boris decided to use an $m$-meter mile and a $c$-meter cable. Now he wants to represent the $n$-meter distance as "$M$ miles and $C$ cables" with non-negative integers $M$ and $C$ as precisely as possible --- that is, he wants to minimize $|M\cdot m+C\cdot c-n|$. Help him!</p>

### 입력 

 <p>Three lines contain an integer each: $n$ --- the distance to represent, $m$ --- the chosen length of a mile, and $c$ --- the chosen length of a cable ($1 \le n \le 10^9$; $500 \le m \le 11\,299$; $169 \le c \le 220$). All values are given in meters.</p>

### 출력 

 <p>Print two non-negative integers $M$ and $C$ --- the best approximation for the distance of $n$ meters using the chosen mile and cable lengths. If there are multiple best approximations, print any of them.</p>

