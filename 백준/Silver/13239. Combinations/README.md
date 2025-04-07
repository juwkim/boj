# [Silver I] Combinations - 13239 

[문제 링크](https://www.acmicpc.net/problem/13239) 

### 성능 요약

메모리: 110716 KB, 시간: 124 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학

### 제출 일자

2025년 4월 7일 09:03:10

### 문제 설명

<p>When we have a set of n elements from which we take k elements, we have a combination.</p>

<p>For example, if we have a set with the numbers from 1 to 5, we have the following different combinations:</p>

<ul>
	<li>1-combinations (1 element from the set each time): (1), (2), (3), (4), (5)</li>
	<li>2-combinations (2 elements from the set each time): (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5).</li>
	<li>3-combinations (3 elements from the set each time): (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5), </li>
	<li>4-combinations (4 elements from the set each time): (1, 2, 3, 4), (1, 3, 4, 5), (1, 2, 4, 5), (1, 2, 3, 5), (2, 3, 4, 5)</li>
	<li>5-combination (all the elements at once): (1, 2, 3, 4, 5)</li>
	<li>0-combination (no element): ()</li>
</ul>

<p>The following formula will give us the number of k-combinations of n elements:</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-texatom texclass="ORD"><mjx-mrow><mjx-texatom texclass="OPEN"><mjx-mo class="mjx-s3"><mjx-c class="mjx-c28 TEX-S3"></mjx-c></mjx-mo></mjx-texatom><mjx-mfrac><mjx-frac type="d" atop="true" delims="true" style="vertical-align: -0.686em;"><mjx-num style="padding-bottom: 0.657em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-den><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-den></mjx-frac></mjx-mfrac><mjx-texatom texclass="CLOSE"><mjx-mo class="mjx-s3"><mjx-c class="mjx-c29 TEX-S3"></mjx-c></mjx-mo></mjx-texatom></mjx-mrow></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mfrac space="4"><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-mrow></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="OPEN"><mo minsize="2.047em" maxsize="2.047em">(</mo></mrow><mfrac linethickness="0"><mi>n</mi><mi>k</mi></mfrac><mrow data-mjx-texclass="CLOSE"><mo minsize="2.047em" maxsize="2.047em">)</mo></mrow></mrow></mrow><mo>=</mo><mfrac><mrow><mi>n</mi><mo stretchy="false">(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo>⋯</mo><mo stretchy="false">(</mo><mi>n</mi><mo>−</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mrow><mi>k</mi><mo stretchy="false">(</mo><mi>k</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo>⋯</mo><mn>1</mn></mrow></mfrac></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[{n \choose k} = \frac{n (n-1)\cdots(n-k+1)}{k(k-1)\cdots 1}\]</span> </mjx-container></p>

<p>As we saw in the list before</p>

<ul>
	<li>(5 over 0) = 1</li>
	<li>(5 over 1) = 5</li>
	<li>(5 over 2) = 10</li>
	<li>(5 over 3) = 10</li>
	<li>(5 over 4) = 5</li>
	<li>(5 over 5) = 1 </li>
</ul>

<p>Your task is to compute several (n over k) operations.</p>

### 입력 

 <p>A line with an integer t. The following t lines will contain 2 integers each separated by spaces. The first value will be n and second k.</p>

<ul>
	<li>1 ≤ t ≤ 1000</li>
	<li>1 ≤ n ≤ 1000</li>
	<li>0 ≤ k ≤ n</li>
</ul>

### 출력 

 <p>For each (n k) pair. Compute the number of k-combinations of a set of size n. Compute the results modulo 1000000007 (10^9 + 7).</p>

