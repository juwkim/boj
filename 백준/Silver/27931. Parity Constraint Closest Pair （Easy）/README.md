# [Silver III] Parity Constraint Closest Pair (Easy) - 27931 

[문제 링크](https://www.acmicpc.net/problem/27931) 

### 성능 요약

메모리: 196720 KB, 시간: 340 ms

### 분류

그리디 알고리즘, 정렬, 두 포인터

### 제출 일자

2024년 1월 19일 01:07:00

### 문제 설명

<p>수직선상에 좌푯값이 서로 다른 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 격자점이 있다. 서로 다른 두 점의 거리 중 짝수인 최솟값과 서로 다른 두 점의 거리 중 홀수인 최솟값을 각각 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 점의 개수를 나타내는 양의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄에는 각 점의 좌표를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개가 공백으로 구분되어 주어진다. </p>

### 출력 

 <p>첫 번째 줄에 서로 다른 두 점의 거리 중 짝수인 최솟값과 서로 다른 두 점의 거리 중 홀수인 최솟값을 공백으로 구분하여 출력한다. 단, 해당하는 거리가 없는 경우 <span style="color:#e74c3c;"><code>-1</code></span>을 출력한다.</p>

