# [Bronze I] Osobna - 32532 

[문제 링크](https://www.acmicpc.net/problem/32532) 

### 성능 요약

메모리: 108080 KB, 시간: 92 ms

### 분류

문자열

### 제출 일자

2024년 10월 29일 16:52:25

### 문제 설명

<p>Toni, the new chairperson of COCI (in Croatian: <em>HONI</em>), loves HONI so much that he decided to change his last name to match the competition’s name. From now on, his name is Toni Honi! Excited about the change, Toni eagerly awaited his new personal ID card. When it finally arrived, he couldn’t stop staring at it. He was especially fascinated by the three lines of characters on the back of the card.</p>

<p>It didn’t take him long to realize that these lines contain some of his personal details: his first name, last name, birth date, and personal identification number (PIN). He copied the lines from his ID onto a piece of paper and identified the details he could recognize:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/5d6c8a57-533b-460f-96d6-5995ca1a880e/-/preview/" style="width: 453px; height: 122px;"></p>

<p>In the first line, which consists of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> letters, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$21$</span></mjx-container> digits, and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container> '<code><</code>' characters, Toni discovered his PIN — the last <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$11$</span></mjx-container> digits of the line.</p>

<p>In the second line, he identified his birth date. The first two digits represent the year, the next two the month, and the final two digits the day of birth. If the two-digit year is less than or equal to <code>24</code>, it means the person was born in the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$21$</span></mjx-container>st century (so the full year starts with <code>20</code>). Otherwise, the person was born in the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container>th century (so the full year starts with <code>19</code>).</p>

<p>In the third line, Toni found his first name, followed by two '<code><</code>' characters, and then his last name. The rest of the line was padded with '<code><</code>' characters.</p>

<p>Toni found these discoveries fascinating and now wants you to join the fun — for the three lines on the back of the ID card, extract and print the person’s first name, last name, birth date, and personal identification number (PIN).</p>

### 입력 

 <p>The input consists of three lines of characters, each of length <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$30$</span></mjx-container>. The characters that can appear are uppercase English letters, digits, and the character '<code><</code>'. The first name and last name will each consist of exactly one word and will be in uppercase English letters. Both names will fit entirely into the third line.</p>

### 출력 

 <p>Output four lines:</p>

<ul>
	<li>In the first line, print '<code>Ime: </code>' followed by the person’s first name, capitalized (only the first letter should be uppercase).</li>
	<li>In the second line, print '<code>Prezime: </code>' followed by the person’s last name, capitalized (only the first letter should be uppercase).</li>
	<li>In the third line, print '<code>Datum rodjenja: </code>' followed by the birth date in the format <code>DD-MM-YYYY</code>.</li>
	<li>In the fourth line, print '<code>OIB: </code>' followed by the person’s personal identification number (PIN).</li>
</ul>

<p>Side note: "Ime" stands for name, "Prezime" for surname, and "Datum rodjenja" for birth date when translated from Croatian.</p>

