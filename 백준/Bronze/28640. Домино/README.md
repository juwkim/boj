# [Bronze III] Домино - 28640 

[문제 링크](https://www.acmicpc.net/problem/28640) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2023년 11월 14일 10:55:20

### 문제 설명

<p>Вы с друзьями договорились сыграть в <<Among Us>>. В назначенное время все зашли в игру. Все, кроме Арсения, который как всегда опаздывает. Находясь в комнате ожидания, вы решили поиграть в виртуальное домино, которое как раз в экспериментальном режиме было добавлено в последнем обновлении игры.</p>

<p>Так как режим еще экспериментальный, игра максимально примитивна: на столе лежит две доминошки. Каждая доминошка представляет собой прямоугольник, разделенный на две половины. В каждой половине доминошки нарисовано от нуля до шести точек. Игрокам нужно определить, можно ли совместить эти две доминошки. Доминошки можно совместить тогда и только тогда, когда существует такое целое неотрицательное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>, что на хотя бы одной из половинок каждой доминошки нарисовано ровно <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> точек.</p>

<p>Эта игра показалась вам чересчур примитивной, поэтому вы решили написать программу, которая будет автоматически в нее выигрывать. Сделайте это!</p>

### 입력 

 <p>Входные данные содержат две строки, каждая из которых содержит описание доминошки. Описание доминошки состоит из нескольких точек (символ <<<code>.</code>>>, ASCII-код <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>46</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$46$</span></mjx-container>) и ровно одной вертикальной черты (символ <<<code>|</code>>>, ASCII-код 124). Точки по одну сторону от вертикальной черты лежат в одной половине доминошки, а по другую --- во второй половине.</p>

<p>Гарантируется, что каждая половина каждой доминошки содержит от <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> до <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$6$</span></mjx-container> точек.</p>

### 출력 

 <p>Выведите <<<code>Yes</code>>>, если доминошки можно совместить, и <<<code>No</code>>> в противном случае.</p>

