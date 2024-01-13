# [Silver III] 트리플 소트 - 20309 

[문제 링크](https://www.acmicpc.net/problem/20309) 

### 성능 요약

메모리: 148760 KB, 시간: 180 ms

### 분류

애드 혹, 수학, 정렬

### 제출 일자

2024년 1월 13일 21:33:49

### 문제 설명

<p>알고리즘 수업을 듣고 감명받은 윤이는 자신만의 정렬 알고리즘을 만들기로 했다. 윤이가 만든 정렬 알고리즘 "트리플 소트"는 다음과 같이 동작한다.</p>

<ul>
	<li>배열에서 <strong>연속한 위치</strong>에 있는 세 원소를 임의로 고른다.</li>
	<li>세 원소의 순서를 뒤집는다. 예를 들어 세 원소가 순서대로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a, b, c$</span></mjx-container>이면 뒤집은 뒤에는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$c,b,a$</span></mjx-container>가 된다.</li>
	<li>배열이 오름차순으로 정렬될 때까지 위 과정을 반복한다.</li>
</ul>

<p>하지만 윤이는 트리플 소트로 모든 배열을 정렬할 수 없다는 사실을 깨닫고 실망했다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>까지의 정수가 한 번씩 등장하는 배열이 주어졌을 때, 트리플 소트로 정렬할 수 있는지 판별하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 배열의 크기를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄에 배열의 원소가 공백을 사이에 두고 순서대로 주어진다.</p>

### 출력 

 <p>트리플 소트로 주어진 배열을 오름차순으로 정렬할 수 있으면 <samp>YES</samp>, 그렇지 않으면 <samp>NO</samp>를 출력한다.</p>

