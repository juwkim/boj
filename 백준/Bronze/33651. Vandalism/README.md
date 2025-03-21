# [Bronze IV] Vandalism - 33651 

[문제 링크](https://www.acmicpc.net/problem/33651) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 문자열

### 제출 일자

2025년 3월 21일 19:46:35

### 문제 설명

<p>In recent weeks, the United Association against Property Crime (UAPC) sign has been repeatedly vandalized. Vandals remove some of the letters from <code>UAPC</code> to form an acronym of their choosing. For example, last month, the Unauthorized Art Collective (UAC) removed the letter <code>P</code>.</p>

<p>The UAPC is tired of manually determining which letters have been lost and need replacement. They have tasked you with creating an algorithm to automatically identify the missing letters.</p>

### 입력 

 <p>The first line of input contains a string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> of length at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>. It is guaranteed that <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> is non-empty and can be obtained by removing some characters from <code>UAPC</code>, while preserving the order of the remaining letters. It is guaranteed that at least one character has been removed.</p>

### 출력 

 <p>Output a string consisting of the characters removed from <code>UAPC</code> to obtain <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>, listed in the order they appear in <code>UAPC</code>.</p>

