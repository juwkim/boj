# [Bronze II] Game Night - 33253 

[문제 링크](https://www.acmicpc.net/problem/33253) 

### 성능 요약

메모리: 116444 KB, 시간: 212 ms

### 분류

구현, 문자열

### 제출 일자

2025년 2월 7일 01:14:37

### 문제 설명

<p>Every Saturday, Geronimo is organizing a game night for all his friends. One after the other, his friends keep asking him for his Wi-Fi password. Because Geronimo has many friends and does not want to be continuously disturbed just to share his password, he decides to grab an old box of fridge magnets that have the shape of letters, and spells out the password on the fridge.</p>

<p>Since Geronimo cares about the security of his Wi-Fi network, he wants to change the Wi-Fi password after the game night, to make sure that his password is not shared with strangers who will then use his network. However, that means he also has to update the password displayed on the fridge. The box with fridge magnets is a complete mess, so Geronimo does not want to spend too much time searching through the box for the right letters, especially when a new password contains some letters that were also in the old password.</p>

<p>Given Geronimo's old and new Wi-Fi password, can you calculate how many letters he has to search for in the box to spell out the new password on the fridge?</p>

### 입력 

 <ul>
	<li>One line with one integer: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq n \leq 10^6$</span></mjx-container>, the length of the passwords. Both passwords have the same length.</li>
	<li>Two lines with each one password of length <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>. The passwords only contain lowercase letters ('<code>a</code>' through '<code>z</code>').</li>
</ul>

### 출력 

 <p>One line, containing one integer: the number of letters that cannot be re-used between the two passwords.</p>

