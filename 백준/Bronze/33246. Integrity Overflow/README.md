# [Bronze II] Integrity Overflow - 33246 

[문제 링크](https://www.acmicpc.net/problem/33246) 

### 성능 요약

메모리: 110576 KB, 시간: 104 ms

### 분류

구현, 문자열

### 제출 일자

2025년 1월 26일 13:08:30

### 문제 설명

<p>The Fortune Protection Corporation (FPC) is a company specialized in securely storing the money of their clients. The money safe is sealed with a 50 cm thick steel door that can only open after correctly entering the secret password in a terminal next to the door. The FPC takes the integrity of this system very serious, and wants to be sure that the door never opens when somebody enters an incorrect password. Since some of the employees of the FPC have dyslexia, the safe will also open when the password contains one incorrect character (it must have the correct length, though).</p>

<p>Given an audit log containing all access attempts to the safe, can you tell whether the integrity of the safe is compromised?</p>

### 입력 

 <ul>
	<li>One line with one integer: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq n \leq 1000$</span></mjx-container>, the number of lines in the audit log.</li>
	<li>One line containing the correct password.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines with two words each, separated with a single space:
	<ul>
		<li>The first word is the entered password.</li>
		<li>The second word is either "<code>ALLOWED</code>" or "<code>DENIED</code>", depending on whether the password was correct or incorrect, respectively.</li>
	</ul>
	</li>
</ul>

<p>All passwords are at most 32 characters in length and only contain letters from the English alphabet (<code>A-Z</code> and <code>a-z</code>) and numbers (<code>0-9</code>).</p>

### 출력 

 <p>One line, containing "<code>SYSTEM SECURE</code>" if the audit log contains no suspicious access attempts, or "<code>INTEGRITY OVERFLOW</code>" if the security of the system has been compromised.</p>

