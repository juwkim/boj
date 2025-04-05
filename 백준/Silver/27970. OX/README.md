# [Silver I] OX - 27970 

[문제 링크](https://www.acmicpc.net/problem/27970) 

### 성능 요약

메모리: 110768 KB, 시간: 124 ms

### 분류

애드 혹, 수학

### 제출 일자

2025년 4월 5일 21:21:58

### 문제 설명

<p><span style="color:#e74c3c;"><code>O</code></span>와 <span style="color:#e74c3c;"><code>X</code></span>로 이루어진 문자열이 주어진다. 모든 문자를 <span style="color:#e74c3c;"><code>X</code></span>로 만들 때까지 다음 연산을 반복할 때, 시행하는 연산의 횟수를 구하시오.</p>

<ul>
	<li>문자열의 가장 왼쪽에 있는 <span style="color:#e74c3c;"><code>O</code></span>를 <span style="color:#e74c3c;"><code>X</code></span>로 바꾸고, 그보다 왼쪽에 있는 <span style="color:#e74c3c;"><code>X</code></span>를 전부 <span style="color:#e74c3c;"><code>O</code></span>로 바꾼다.</li>
</ul>

### 입력 

 <p>첫째 줄에 <span style="color:#e74c3c;"><code>O</code></span>와 <span style="color:#e74c3c;"><code>X</code></span>로 이루어진 문자열이 주어진다. 문자열의 길이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100\,000$</span></mjx-container> 이하이다.</p>

### 출력 

 <p>첫째 줄에 연산의 횟수를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup><mo>+</mo><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^9 + 7$</span></mjx-container>로 나눈 나머지를 출력한다.</p>

