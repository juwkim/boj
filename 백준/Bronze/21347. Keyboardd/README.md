# [Bronze I] Keyboardd - 21347 

[문제 링크](https://www.acmicpc.net/problem/21347) 

### 성능 요약

메모리: 31996 KB, 시간: 88 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Oh no! Joanna just spilled some syrup on her keyboard and now some of the keys are sticky. This causes her considerable frustration, as every time she presses one of the sticky keys, the corresponding character gets entered twice on her computer.</p>

<p>This could not have happened at a more inconvenient time; it is the start of the contest and she was just about to type in the solution to the first problem! Joanna does not have time to remove and clean every key on her keyboard, so she wonders if there is a way to quickly identify the sticky keys. Starting to panic, she quickly types some text on her keyboard and stares at the resulting text displayed on her screen.</p>

<p>Given the line of text that Joanna typed on her keyboard and the resulting text displayed on her screen, help her determine which keys must be sticky.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line containing a string $s$ ($1 \leq \mathrm{length}(s) \leq 1\,000$), the text that Joanna typed on her keyboard.</li>
	<li>One line containing a string $t$ ($1 \leq \mathrm{length}(t) \leq 1\,000$), the text displayed on Joanna's screen as a result.</li>
</ul>

<p>Both $s$ and $t$ consist only of lower-case letters (`<code>a</code>'--`<code>z</code>') and spaces (`<code> </code>'), and start and end with a letter.</p>

<p>It is guaranteed that $t$ is the result of doubling each character in $s$ that corresponds to a sticky key. At least one character in $s$ corresponds to a sticky key (i.e.\ $s \neq t$).</p>

### 출력 

 <p>Output all characters (letters and space) corresponding to keys that must be sticky, in any order.</p>

