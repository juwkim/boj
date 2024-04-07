# [Silver III] Dice - 3510 

[문제 링크](https://www.acmicpc.net/problem/3510) 

### 성능 요약

메모리: 111312 KB, 시간: 140 ms

### 분류

수학, 확률론, 정렬

### 제출 일자

2024년 4월 7일 22:55:18

### 문제 설명

<p>Along with other things, Feadagor is fond of playing tabletop role playing games. He has just discovered a new game and he’d like to play it with his friends. Unluckily, he cannot call his friends right now, as the game requires quite an unusual set of dice. The description of the game says that there must be n dice, and i-th die must have a<sub>i</sub> faces. Each die must be shaped so its faces fall equiprobably.</p>

<p>According to the game manual, the numbers from 1 to m, where m = ∑a<sub>i</sub> (1 ≤ i ≤ n), must be written on the faces, and each number from the interval must be used exactly once. The numbers arrangement must be chosen so that if you throw all the dice simultaneously, then the mathematical expectation E of the total value in such experiment will be maximal.</p>

<p>The manual says that only Maiar have enough wisdom to arrange the numbers properly (and therefore your only choice is to buy the dice just for 133 dollars, telepathy is quite expensive now). But maybe there is a simpler way to make the proper arrangement?</p>

### 입력 

 <p>The first line of the input file contains a single integer number n (1 ≤ n ≤ 1000). The following line contains n integer numbers a<sub>1</sub>, a<sub>2</sub> ..., a<sub>n</sub> (1 ≤ a<sub>i</sub> ≤ 100).</p>

### 출력 

 <p>The first line of the output file must contain maximal possible expectation E — a floating-point number precise up to 5 digits after the decimal point.</p>

<p>The following n lines must contain the numbers arrangement: i-th line must contain a<sub>i</sub> integer numbers — the numbers to be written on the faces of i-th die.</p>

