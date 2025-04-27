# [Silver I] Jane’s First Words - 9779 

[문제 링크](https://www.acmicpc.net/problem/9779) 

### 성능 요약

메모리: 112584 KB, 시간: 160 ms

### 분류

정규 표현식, 문자열

### 제출 일자

2025년 4월 27일 16:53:42

### 문제 설명

<p>Jane (my ~2 years-old baby daughter) has started speaking some simple words now. "Daddy" and "Mommy" are the two common first words. Hearing those words for the first time are indeed beautiful and memorable.</p>

<p>Last year, Steven really wanted to record when his baby called him for the first time. So, Steven put a microphone and sound capture program near Jane's baby cot (baby's bed). This microphone captured Jane's sounds and the program transmitted the list of words captured to Steven. He wrote a program to detect the moment when Jane's first call him: "daddy" (or its variants). This time, you will also write similar program.</p>

### 입력 

 <p>You are given one word per line. These are the list of captured sounds. Each line contains only lowercase alphabet without any whitespaces and at most 20 characters. Input is terminated with an EOF.</p>

### 출력 

 <p>For each word/line, output "She called me!!!" in one line if that word matches this regular expression below. Otherwise, output "Cooing" in one line (to say that this is just some baby soft murmuring sound).</p>

<p>Note: Quotes are only for clarity.</p>

<p>The regular expression (regex): "da+dd?(i|y)".</p>

<p>If you are not familiar with regex, let me explain:</p>

<ul>
	<li>'+' means one or more of the preceding element.</li>
	<li>'?' means zero or one of the preceding element.</li>
	<li>A vertical bar '|' separates alternatives.</li>
	<li>Parentheses are used to define the scope and precedence of the operators.</li>
</ul>

