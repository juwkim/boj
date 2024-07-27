# [Silver V] Побег - 29211 

[문제 링크](https://www.acmicpc.net/problem/29211) 

### 성능 요약

메모리: 13684 KB, 시간: 12 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 7월 27일 16:35:19

### 문제 설명

<p>Это интерактивная задача.</p>

<p>Шрам хочет остаться единственным претендентом на титул короля Саванны. Ради этого он коварно расправился с Муфасой, после чего приказал своим приспешникам-гиенам уничтожить Симбу. К счастью, Симбе улыбнулась удача, и ему предоставился шанс спастись от стаи разъяренных гиен.</p>

<p>Гиены преследуют Симбу на квадратном клетчатом поле, длина и ширина которого равны <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> клеткам. Как столбцы, так и строки этого поля пронумерованы числами от одного до <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>. Симба находится в одной из клеток поля, находящейся в первой строке. Стая гиен находится в некоторой клетке поля, не совпадающей с той, в которой находится Симба.</p>

<p>Симба и стая по очереди перемещаются по полю. За один ход Симба должен перебежать в одну из клеток, соседних по вертикали, горизонтали, или диагонали с той, в которой он находится. После этого гиены могут переместиться в любую клетку, расстояние до которой по горизонтали совпадает с расстоянием по вертикали. Проще говоря, гиены могут переместиться в любую клетку, находящуюся на одной диагонали с той, в которой они располагаются в данный момент.</p>

<p>Если после чьего-либо хода гиены оказываются в одной клетке с Симбой, будущий король погибает в неравной схватке. Если же после очередного ходя львенка он оказывается в любой из клеток <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>-й строки, в которой нет гиен, он благополучно пересекает поле и скрывается в джунглях. Помогите Симбе сбежать от своих преследователей.</p>

### 입력 

 Empty

### 출력 

 Empty

