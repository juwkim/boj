# [Bronze I] ЧАСОВНИК - 31213 

[문제 링크](https://www.acmicpc.net/problem/31213) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

수학

### 제출 일자

2024년 7월 22일 23:24:50

### 문제 설명

<p>Стандартен часовник със стрелки показва точно <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container> часа и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> минути. Означенията на циферблата са целите числа от 1 до 12 за часовете на часовата стрелка и от 0 до 59 за минутите, които показва минутната стрелка. Стрелките се движат равномерно. Отбелязваме с чертичка точното място, където е стрелката за минутите. Какво ще покажат стрелките на часовника в първия следващ момент, когато стрелката за часовете застане точно на отбелязаната чертичка?</p>

<p>Напишете програма clock, която отговаря на този въпрос.</p>

### 입력 

 <p>От първия ред на стандартния вход се въвеждат две цели числа за стойностите на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container>, разделени с интервал.</p>

### 출력 

 <p>На първия ред на стандартния изход програмата трябва да изведе търсените показания на часовника, като две цели числа, разделени с един интервал – съответно за стойностите на часовете и минутите.</p>

<p>На втория ред програмата трябва да изведе изведе времето (две цели числа, разделени с един интервал – съответно за стойностите на часовете и минутите), изминало между началния момент и момента, когато часовата стрелка е застанала точно на отбелязаната чертичка.</p>

