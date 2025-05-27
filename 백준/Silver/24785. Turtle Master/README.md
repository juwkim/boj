# [Silver I] Turtle Master - 24785 

[문제 링크](https://www.acmicpc.net/problem/24785) 

### 성능 요약

메모리: 108384 KB, 시간: 112 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 27일 10:10:36

### 문제 설명

<p>Robot Turtles is one of Theta's favorite games. In this game, kindergarteners learn how to "code" by creating programs that move a turtle from a starting field to a diamond. Robot Turtles is reportedly the most successful game funded by the Kickstarter incubator.</p>

<p>In the actual board game, an adult plays the role of the "turtle master," which is the person that plays the role of a CPU to execute the program. As you can imagine, this is a pretty boring task that cries out for automation: in this problem, you are asked to write a program that automates the task of the turtle master.</p>

<p>Robot Turtles is played on an <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>×</mo><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8 \times 8$</span></mjx-container> board. There is one turtle (marked with the letter <code>T</code>), which always starts out at the bottom-left field, facing right.  The board contains empty squares (marked as <code>.</code>), castles made out of rock (<code>C</code>), and castles made out of ice (<code>I</code>). The diamond is marked with a <code>D</code>. The turtle may move only onto empty squares and the square on which the diamond is located.</p>

<p>A turtle program contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container> kinds of instructions, marked by a single letter.</p>

<ul>
	<li><code>F</code> The turtle moves one field forward in the direction it is facing. If the turtle faces a castle or the border of the board, a program error occurs.</li>
	<li><code>R</code> The turtle turns <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$90$</span></mjx-container> degrees to the right (the turtle will just turn and stay on the same field).</li>
	<li><code>L</code> The turtle turns <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$90$</span></mjx-container> degrees to the left (the turtle will just turn and stay on the same field).</li>
	<li><code>X</code> The turtle fires a laser in the direction it is facing. If the square it is facing contains an ice castle, the ice castle will melt and the square will turn into an empty square. Otherwise, a program error occurs. The turtle will not move or change direction. It is a program error to fire the laser at empty squares, rock castles  or outside the board.</li>
</ul>

### 입력 

 <p>The input consists of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container> lines. The first <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container> lines contains the board, each line representing the squares in a row of the board. The turtle will always be at the bottom-left. There will be exactly <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> diamond. The <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.363em;"><mjx-texatom size="s" texclass="ORD"><mjx-mtext class="mjx-n"><mjx-c class="mjx-c74"></mjx-c><mjx-c class="mjx-c68"></mjx-c></mjx-mtext></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mrow data-mjx-texclass="ORD"><mtext>th</mtext></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9^{\text{th}}$</span></mjx-container> line contains the program the turtle master is asked to execute.</p>

### 출력 

 <p>Output <code>Diamond!</code> if the entire program can be executed without program error and if the turtle is on the diamond square after the program has been executed. Output <code>Bug!</code> if a program error occurred, or if the turtle does not end up on the diamond square!</p>

