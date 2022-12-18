# [Bronze II] Picture Perfect - 6904 

[문제 링크](https://www.acmicpc.net/problem/6904) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Roy has a stack of student yearbook photos. He wants to lay the pictures on a flat surface edge-to-edge to form a filled rectangle with minimum perimeter. All photos must be fully visible. Each picture is a square with dimensions 1 unit by 1 unit.</p>

<p>For example, he would place 12 photos in the following configuration, where each photo is indicated with an <code>X</code>.</p>

<pre>XXXX
XXXX
XXXX</pre>

<p>Of course, he could orient them in the other direction, such as</p>

<pre>XXX
XXX
XXX
XXX</pre>

<p>which would have the same perimeter, 14 units.</p>

<p>Your program should repeatedly read a positive integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>, the number of pictures to be laid out. For each input, it should print the smallest possible perimeter for a filled rectangle that is formed by laying all the pictures edge-to-edge. Also print the dimensions of this rectangle.</p>

<p>You may assume that there are less than <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$65\,000$</span></mjx-container> photos. An input value of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C = 0$</span></mjx-container> indicates that the program should terminate.</p>

### 입력 

 Empty

### 출력 

 Empty

