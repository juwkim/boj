# [Silver IV] Surmising a Sprinter’s Speed - 19607 

[문제 링크](https://www.acmicpc.net/problem/19607) 

### 성능 요약

메모리: 132088 KB, 시간: 584 ms

### 분류

정렬(sorting)

### 문제 설명

<p>Trick E. Dingo is trying, as usual, to catch his nemesis the Street Sprinter. His past attempts using magnets, traps and explosives have failed miserably, so he’s catching his breath to gather observational data and learn more about how fast Street Sprinter is.</p>

<p>Trick E. Dingo and Street Sprinter both inhabit a single straight west-east road with a particularly famous rock on it known affectionately as The Origin. Positions on this straight road are measured numerically according to the distance from The Origin, and using negative numbers for positions west of The Origin and positive numbers for positions east of The Origin.</p>

<p>The observations by Trick E. Dingo each contain two numbers: a time, and the value of Street Sprinter’s position on the road at that time. Given this information, what speed must Street Sprinter must be capable of?</p>

### 입력 

 <p>The first line contains a number 2 ≤ N ≤ 100 000, the number of observations that follow. The next N lines each contain an integer 0 ≤ T ≤ 1 000 000 000 indicating the time, in seconds, of when a measurement was made, and an integer −1 000 000 000 ≤ X ≤ 1 000 000 000 indicating the position, in metres, of the Street Sprinter at that time. No two lines will have the same value of T.</p>

### 출력 

 <p>Output a single number X, such that we can conclude that Street Sprinter’s speed was at least X metres/second at some point in time, and such that X is as large as possible. If the correct answer is C, the grader will view X as correct if |X − C|/C < 10<sup>−5</sup>.</p>

