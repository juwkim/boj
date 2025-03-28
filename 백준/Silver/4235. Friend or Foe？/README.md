# [Silver III] Friend or Foe? - 4235 

[문제 링크](https://www.acmicpc.net/problem/4235) 

### 성능 요약

메모리: 1120 KB, 시간: 0 ms

### 분류

애드 혹, 구현, 수학, 수치해석, 무작위화

### 제출 일자

2025년 3월 29일 02:54:14

### 문제 설명

<p>Luke has a bit of trouble telling the difference between star systems in the Rebel Alliance and those in the Empire. He has a list of the x,y,z coordinates of each system in the Empire and each in the Alliance, but at warp speed he simply has insufficient time to look up systems in his lists.</p>

<p>After destroying the friendly planet Endor, Luke has had to admit he needs the help of his targeting computer. His computer, being an early model, can only compute the truth value of the inequality</p>

<pre style="text-align: center;">ax + by + cz + d > 0
</pre>

<p>Where x,y,z are the coordinates of the system, and a,b,c,d are real-valued coefficients. You are to compute a,b,c,d so that the inequality holds for all systems in the Empire, and for no systems in the Alliance.</p>

### 입력 

 <p>Input consists of several test cases followed by -1 -1. Each test case first gives the number of Alliance systems, followed by a line for each system giving the integer coordinates <i>-100 ≤ x,y,z ≤ 100</i> of the system in 3-dimensional space. The number of Empire systems, and the coordinates of each, follow. The Empire and Alliance combined have at least one and no more than 200 systems. All systems have distinct coordinates.</p>

### 출력 

 <p>For each test case, output a single line containing a,b,c,d as real numbers separated by spaces. Use enough precision to ensure that your solution is correct. You may assume that a solution exists; if there is more than one solution, any one will do.</p>

