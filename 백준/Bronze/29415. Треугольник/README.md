# [Bronze II] Треугольник - 29415 

[문제 링크](https://www.acmicpc.net/problem/29415) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

수학

### 제출 일자

2025년 5월 18일 05:23:35

### 문제 설명

<p>Отдыхая на даче у Петиной бабушки, Петя и Вася решили построить секретный штаб для своей шпионской организации. Для размещения всей шпионской техники им необходимо помещение площадью ровно <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container> квадратных метров. Стены штаба приходится строить из подручного материала, найденного у бабушки в сарае. Этим материалом оказались деревянные доски, каждая из которых имела длину ровно один метр. Выбирая форму штаба, Вася вспомнил последний урок геометрии, на котором они проходили прямоугольные треугольники, и предложил построить штаб в форме этой фигуры. Тем более, тогда они легко смогут посчитать его площадь и убедиться, что она равна требуемой.</p>

<p>Но тут оказалось, что пилы нет и поэтому доски никак не распилить. Васе с Петей придется строить штаб в форме прямоугольного треугольника, все стороны которого выражаются целым числом метров. Им стало интересно, сколько таких треугольников существует. При этом треугольники, имеющие одинаковые длины сторон, но отличающиеся их порядком, считаются одинаковыми.</p>

### 입력 

 <p>Входной файл содержит единственное целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>S</mi><mo>≤</mo><mn>10</mn><mo>,</mo><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le S \le 10,000$</span></mjx-container>) --- требуемая площадь штаба.</p>

### 출력 

 <p>В выходной файл выведите одно целое число --- количество возможных планов постройки штаба, площадь которого <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container> квадратных метров.</p>

