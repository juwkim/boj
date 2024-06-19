# [Silver III] Налеее-во! - 29573 

[문제 링크](https://www.acmicpc.net/problem/29573) 

### 성능 요약

메모리: 110992 KB, 시간: 104 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 6월 19일 19:42:58

### 문제 설명

<p>Прошло около двух недель, и разведчик Смит снова получил срочное и ответственное задание. Наскоро попрощавшись с десятком новоиспеченных подруг и наспех отдав распоряжения своему дворецкому, в три часа ночи он уже находился в аэропорту.</p>

<p>И вот он, все тот же плац. Моросит мелкий дождик, грязи где по колено, а где --- по грудь, но это не смущает ни бравого сержанта, бодрым голосом отдающего команды, ни солдата Перетеркина, их беспрекословно выполняющего. Вчера, занимаясь подметанием плаца, рядовой Перетеркин один лом сломал, а второй потерял. В качестве воспитательной меры ему было назначено три часа строевых тренировок, и первый час этого достойного занятия уже подходил к концу.</p>

<p>Задание разведчика Смита состоит в том, чтобы выяснить, насколько точно выполняет строевые приемы среднестатистический рядовой армии потенциального противника. Для этого он через равные промежутки времени фотографирует плац из укрытия, а команды записывает на портативный шпионский диктофон с направленным микрофоном. Поначалу Смит думал, что задание будет легким, но когда число снимков перевалило за третью сотню, до него постепенно стало доходить, что он так легко не отделается.</p>

<p>Немного поразмыслив, Смит --- а он парень умный --- понял, что стоящую перед ним задачу он может свести к следующей: даны начальное положения солдата на плацу и последовательность команд, которые солдат исполняет, требуется найти положение солдата, которое он займет после исполнения всех этих команд. Но как же решать эту задачу? И тут Смита осенило, и, как только сержант сделал паузу, достал из-за пазухи телефон и стал набирать знакомый номер...</p>

<p>Известно, что на строевой тренировке отрабатывались следующие команды: <<налево>>, <<направо>>, <<кругом>> и <<шаг вперед>>. Представим плац прямоугольным полем размера <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c22C5"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>⋅</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \cdot M$</span></mjx-container>, а солдата на нем --- фигурой, занимающей три идущие подряд смежные клетки. Далее проиллюстрировано выполнение команд.</p>

<pre>Команда <<налево>>
.......  .......
.......  ...\...
..\-/..  ...|...
.......  .../...
.......  .......</pre>

<pre>Команда <<направо>>
.......   .......
.......   .../...
..\-/..   ...|...
.......   ...\...
.......   .......</pre>

<pre>Команда <<кругом>>
.......  .......
..\-/..  ../-\..
.......  .......</pre>

<pre>Команда <<шаг вперед>>
.......      .......
.......      ..\-/..
..\-/..      .......
.......      .......
</pre>

<p>Иными словами, по команде <<налево>> солдат поворачивается на 90 градусов против часовой стрелки, по команде <<направо>> солдат поворачивается на 90 градусов по часовой стрелке, по команде <<кругом>> солдат разворачивается на 180 градусов, по команде <<шаг вперед>> солдат перемещается на одну клетку в ту сторону, куда он смотрит.</p>

### 입력 

 <p>В первой строке входного файла содержатся три целых числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>,</mo><mi>K</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N, M, K \le 100$</span></mjx-container>). Далее следуют <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> строк по <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> символов каждая --- описание исходного положения солдата на плаце.</p>

<p>Следующие <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container> строк содержат команды, отданные солдату. По причине того, что разведчик Смит отчитывается перед начальством на английском языке, команды будут также даны на английском языке. В таблице приведены переводы используемых команд.</p>

<table class="table table-bordered th-center td-center table-center-40">
	<tbody>
		<tr>
			<td>Налево</td>
			<td>Left turn</td>
		</tr>
		<tr>
			<td>Направо</td>
			<td>Right turn</td>
		</tr>
		<tr>
			<td>Кругом</td>
			<td>About turn</td>
		</tr>
		<tr>
			<td>Шаг вперед</td>
			<td>Forward step</td>
		</tr>
	</tbody>
</table>

<p>Гарантируется, что при выполнении команд солдат остается в пределах границ плаца.</p>

### 출력 

 <p>В выходной файл выведите <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> строк по <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> символов каждая --- описание положения солдата на плаце после выполнения команд.</p>

