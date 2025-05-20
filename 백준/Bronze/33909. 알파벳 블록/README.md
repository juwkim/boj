# [Bronze III] 알파벳 블록 - 33909 

[문제 링크](https://www.acmicpc.net/problem/33909) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 5월 20일 10:13:53

### 문제 설명

<p>S, C, O, N 4종류의 알파벳 블록을 가지고 놀던 도현이는 두 가지 사실을 알아냈다.</p>

<ul>
	<li>알파벳 O 블록 1개를 반으로 자르면 알파벳 C 블록 2개로 사용할 수 있다. 알파벳 C 블록 2개를 합쳐서 알파벳 O 블록 1개로 사용하는 것도 가능하다.</li>
	<li>알파벳 S 블록 1개를 뒤집으면 알파벳 N 블록 1개로 사용할 수 있다. 알파벳 N 블록 1개를 뒤집어서 알파벳 S 블록 1개로 사용하는 것도 가능하다.</li>
</ul>

<p>도현이는 교내 대회 홍보를 위해 문자열 “SCON”과 “SCCC”가 하나씩 들어있는 상자를 사람들에게 나눠주기로 했다. 도현이는 가지고 있던 블록들로 문자열을 만들어 최대한 많은 사람들에게 상자를 나눠주려 한다. 각 알파벳 블록의 개수가 주어졌을 때, 도현이가 나눠줄 수 있는 상자 개수의 최댓값을 구해보자.</p>

### 입력 

 <p>첫째 줄에 S, C, O, N 알파벳 블록의 개수를 의미하는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>S</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b_S$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>C</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b_C$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D442 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>O</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b_O$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>N</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b_N$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>도현이가 나눠줄 수 있는 상자 개수의 최댓값을 출력한다.</p>

