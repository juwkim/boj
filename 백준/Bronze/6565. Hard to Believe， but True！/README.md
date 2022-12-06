# [Bronze II] Hard to Believe, but True! - 6565 

[문제 링크](https://www.acmicpc.net/problem/6565) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>The fight goes on, whether to store numbers starting with their most significant digit or their least significant digit. Sometimes this is also called the "Endian War". The battleground dates far back into the early days of computer science. Joe Stoy, in his (by the way excellent) book "Denotational Semantics", tells following story:</p>

<blockquote>"The decision which way round the digits run is, of course, mathematically trivial. Indeed, one early British computer had numbers running from right to left (because the spot on an oscilloscope tube runs from left to right, but in serial logic the least significant digits are dealt with first). Turing used to mystify audiences at public lectures when, quite by accident, he would slip into this mode even for decimal arithmetic, and write things like <code>73+42=16</code>. The next version of the machine was made more conventional simply by crossing the <em>x</em>-deflection wires: this, however, worried the engineers, whose waveforms were all backwards. That problem was in turn solved by providing a little window so that the engineers (who tended to be behind the computer anyway) could view the oscilloscope screen from the back.

<p> </p>

<p>[C. Strachey - private communication.]"</p>
</blockquote>

<p>You will play the role of the audience and judge on the truth value of Turing's equations.</p>

### 입력 

 <p>The input contains several test cases. Each specifies on a single line a Turing equation. A Turing equation has the form <code>"</code><em>a</em><code>+</code><em>b</em><code>=</code><em>c</em><code>"</code>, where <em>a, b, c</em> are numbers made up of the digits <em>0,...,9</em>. Each number will consist of at most <em>7</em> digits. This includes possible leading or trailing zeros. The equation <code>"0+0=0"</code> will finish the input and has to be processed, too. The equations will not contain any spaces.</p>

### 출력 

 <p>For each test case generate a line containing the word <code>"True"</code> or the word <code>"False"</code>, if the equation is true or false, respectively, in Turing's interpretation, i.e. the numbers being read backwards.</p>

