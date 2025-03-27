# [Silver II] The first day of school - 31384 

[문제 링크](https://www.acmicpc.net/problem/31384) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 3월 28일 05:15:13

### 문제 설명

<p>Vasya is a young and very promising android. Today is his first day at University. Vasya has very carefully studied the list of all courses on the wall near the Dean's office and has chosen the ones to attend. Now he wants to write down his own week timetable. Help him do this.</p>

### 입력 

 <p>The first line contains an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- the number of courses Vasya is going to attend (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>12</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 12$</span></mjx-container>). After that the courses are listed, each is described in two lines.</p>

<p>The first line of a course description contains its name. The name of the course may consist of up to five words, which are divided by exactly one space (there are no spaces before the first word and after the last one). The words consist of capital and lowercase Latin letters. The length of every word is within the range from 1 to 10.</p>

<p>The second line of a course description contains the day of week and the number of a lesson, when it takes place. The day of week may take one of the three values: <code>Tuesday</code>, <code>Thursday</code> и <code>Saturday</code>. The number of a lesson --- is an integer from 1 to 4. There are no two courses, Vasya has chosen, taking place at the same time.</p>

### 출력 

 <p>Output the timetable as a table of the size <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>×</mo><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4\times3$</span></mjx-container>. The columns of the table should correspond to the three academic days: the first column --- to Tuesday, the second --- to Thursday, the third --- to Saturday. The rows should correspond to the four classes. The width of each column should be equal to 10 characters. The height of the row of the table equals to the height of the highest of its cells. If all the cells in the row are empty then the height of the row should be equal 1 character. If some word doesn't find room in the current line, it should be placed in the next line. The text in the cell should be aligned to top and left borders. Make the table itself using characters <code>-</code> (ASCII 45), <code>+</code> (ASCII 43) and <code>|</code> (ASCII 124).</p>

