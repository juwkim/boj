# [Silver I] Сумасшедшее домино - 28730 

[문제 링크](https://www.acmicpc.net/problem/28730) 

### 성능 요약

메모리: 111200 KB, 시간: 104 ms

### 분류

애드 혹, 해 구성하기, 홀짝성

### 제출 일자

2025년 8월 2일 03:31:52

### 문제 설명

<p>Джокеру, сидящему в лечебнице Аркхем, часто бывает скучно, ведь у пациентов не так много развлечений --- одни шашки да домино. Сегодня он сидел и бездумно перекладывал доминошки на шахматной доске, когда ему в голову пришла идея головоломки, которая может его развлечь. Он взял шахматную доску, которую можно представить как клетчатый квадрат размера <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>×</mo><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \times n$</span></mjx-container>, и набор доминошек. По приятному совпадению, одна доминошка по размеру равна двум клеткам доски, соседним по стороне. Теперь Джокер хочет расставить на доске несколько шашек, чтобы:</p>

<ul>
	<li>Суммарное количество поставленных шашек не превышало <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span> </mjx-container></li>
	<li>Все клетки, не содержащие шашки, можно было целиком замостить доминошками. Причем, каждая доминошка должна покрывать две соседние по стороне клетки, никакие две доминошки не должны покрывать одну и ту же клетку, и каждая клетка должна быть покрыта доминошкой</li>
	<li>Такое замощение свободных клеток доминошками единственно</li>
</ul>

<p>Джокер уже нашел искомый способ расставить шашки, и теперь предложил решить эту задачу вам.</p>

### 입력 

 <p>В единственной строке дано одно целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le n \le 100$</span></mjx-container>).</p>

### 출력 

 <p>Выведите <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк по <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> символов в каждой --- описание искомой расстановки шашек. Свободные клетки обозначаются символом <<<code>.</code>>>, а клетки, занятые шашками, символом <<<code>#</code>>>.</p>

<p>Если существует несколько подходящих расстановок, выведите любую из них. Гарантируется, что хотя бы одна подходящая расстановка существует --- ведь Джокер какую-то нашел!</p>

