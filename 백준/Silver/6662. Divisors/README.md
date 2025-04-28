# [Silver I] Divisors - 6662 

[문제 링크](https://www.acmicpc.net/problem/6662) 

### 성능 요약

메모리: 121224 KB, 시간: 1256 ms

### 분류

수학, 정수론, 소수 판정

### 제출 일자

2025년 4월 28일 18:54:58

### 문제 설명

<p>Your task in this problem is to determine the number of divisors of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-texatom texclass="OPEN"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c28 TEX-S1"></mjx-c></mjx-mo></mjx-texatom><mjx-mfrac><mjx-frac atop="true" delims="true" style="vertical-align: -0.345em;"><mjx-num style="padding-bottom: 0.29em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-den><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-den></mjx-frac></mjx-mfrac><mjx-texatom texclass="CLOSE"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c29 TEX-S1"></mjx-c></mjx-mo></mjx-texatom></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="OPEN"><mo minsize="1.2em" maxsize="1.2em">(</mo></mrow><mfrac linethickness="0"><mi>n</mi><mi>k</mi></mfrac><mrow data-mjx-texclass="CLOSE"><mo minsize="1.2em" maxsize="1.2em">)</mo></mrow></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \choose k$</span></mjx-container>. Just for fun -- or do you need any special reason for such a useful computation?</p>

### 입력 

 <p>The input consists of several instances. Each instance consists of a single line containing two integers <em>n</em> and <em>k</em> (0 ≤ <em>k</em> ≤ <em>n</em> ≤ 431), separated by a single space.</p>

### 출력 

 <p>For each instance, output a line containing exactly one integer -- the number of distinct divisors of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-texatom texclass="OPEN"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c28 TEX-S1"></mjx-c></mjx-mo></mjx-texatom><mjx-mfrac><mjx-frac atop="true" delims="true" style="vertical-align: -0.345em;"><mjx-num style="padding-bottom: 0.29em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-den><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-den></mjx-frac></mjx-mfrac><mjx-texatom texclass="CLOSE"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c29 TEX-S1"></mjx-c></mjx-mo></mjx-texatom></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="OPEN"><mo minsize="1.2em" maxsize="1.2em">(</mo></mrow><mfrac linethickness="0"><mi>n</mi><mi>k</mi></mfrac><mrow data-mjx-texclass="CLOSE"><mo minsize="1.2em" maxsize="1.2em">)</mo></mrow></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \choose k$</span></mjx-container>. For the input instances, this number does not exceed 2<sup>63</sup> - 1.</p>

