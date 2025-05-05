# [Silver I] <code>git mv</code> - 23370 

[문제 링크](https://www.acmicpc.net/problem/23370) 

### 성능 요약

메모리: 122724 KB, 시간: 116 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 5월 6일 02:15:06

### 문제 설명

<p>During development, you recently moved a file from one location to another. To keep your development team up to date with the change you made, you want to send them a short description of the change, without making use of any versioning software.</p>

<p>Both the source location and destination are valid Unix path names, that is, a nonempty string consisting of lowercase letters and "<code>/</code>" such that no "<code>/</code>" occurs at the begin or the end, nor does it contain two consecutive forward slashes.</p>

<p>You need to find the shortest string of the form "<code>A{B => C}D</code>" such that:</p>

<ul>
	<li>The source location is "<code>ABD</code>" and the destination is "<code>ACD</code>", where double forward slashes should be read as one forward slash. For example, if a file is moved from "<code>a/c</code>" to "<code>a/b/c</code>", we can describe this movement by "<code>a/{ => b}/c</code>", meaning the source location was "<code>a/c</code>" and not "<code>a//c</code>".</li>
	<li>The string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A$</span></mjx-container> is empty or ends with a forward slash, and similarly <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$D$</span></mjx-container> is empty or starts with a forward slash.</li>
	<li>Both <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$B$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container> do not start or end with a forward slash.</li>
</ul>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line containing the source location.</li>
	<li>One line containing the destination location.</li>
</ul>

<p>Both lines will contain at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^6$</span></mjx-container> characters, will not begin or end with a forward slash and will not contain any directory name twice. The two strings are guaranteed to be different.</p>

### 출력 

 <p>Output the shortest replacement string that transforms the source location to the destination, satisfying the above constraints.</p>

