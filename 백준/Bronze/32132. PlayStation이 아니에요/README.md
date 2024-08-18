# [Bronze I] PlayStation이 아니에요 - 32132 

[문제 링크](https://www.acmicpc.net/problem/32132) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

구현, 문자열

### 제출 일자

2024년 8월 18일 21:04:42

### 문제 설명

<p>오늘도 피돌이는 백준에서 PS를 하고 있다. 하지만 PS라는 이름의 특성상 PlayStation으로 오해를 받고는 한다.</p>

<p>게시판에 글을 작성하던 중, 문득 피돌이는 문자열에 <code>"PS4"</code> 혹은 <code>"PS5"</code>를 부분 문자열로 포함하면 사람들이 PlayStation에 대한 얘기로 오해한다는 것을 깨달았다. 피돌이는 이러한 오해를 받지 않기 위해 자신이 작성하던 문자열에서 <code>"PS4"</code> 혹은 <code>"PS5"</code>가 보인다면 <code>"PS4"</code> 혹은 <code>"PS5"</code>가 나타나지 않을 때까지 <strong>숫자를 지워</strong> 문자열을 변경하기로 했다.</p>

<p>문자열이 주어졌을 때, <code>"PS4"</code> 혹은 <code>"PS5"</code>가 나오지 않을 때까지 문자열에서 숫자를 지워 출력하여라. 만약 만족하는 문자열이 여러 개라면, 그중 가장 긴 문자열을 출력한다.</p>

### 입력 

 <p>첫째 줄에 문자열의 길이를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 50$</span></mjx-container>)</p>

<p>둘째 줄에 문자열이 주어진다. 문자열은 영문 대문자와 숫자로만 이루어져 있다.</p>

### 출력 

 <p>첫째 줄에 피돌이가 문자열을 고치고 난 뒤의 문자열을 출력한다. 만약 만족하는 문자열이 여러 개라면, 그중 가장 긴 문자열을 출력한다.</p>

<p>가능한 모든 입력에 대해 가장 긴 문자열이 존재하며 유일함을 증명할 수 있다.</p>

