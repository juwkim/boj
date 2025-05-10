# [Bronze II] Ножницы - 28720 

[문제 링크](https://www.acmicpc.net/problem/28720) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

수학

### 제출 일자

2025년 5월 10일 18:42:14

### 문제 설명

<p>В октябре 1988 года в дождливое утро городка Дерри заикающийся подросток Билл Денбро делает своему семилетнему брату Джорджи бумажный кораблик.</p>

<p>Для того, чтобы сделать отличный кораблик Биллу нужно вырезать идеальный квадрат из бумаги и для этого ему понадобятся хорошие ножницы. Мальчик нашел какие-то ножницы у себя в ящике и хочет проверить, как они режут. </p>

<p>Для этого у него давно заготовлен следующий тест: Билл берет ножницы и листок клетчатой бумаги размера <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> клеток. Далее он вырезает из этого листка клетчатую спираль, которая закручивается вправо. При этом все разрезы происходят только по линиям сетки. Формально:</p>

<ul>
	<li>Билл отступает 1 клетку от левого края</li>
	<li>Затем режет прямую линию в направлении <strong>вверх</strong> по одной клетке за раз до тех пор, пока при следующем разрезании получившаяся фигура не распадется на две части.</li>
	<li>Затем Билл продолжит резать прямую в направлении <strong>вправо</strong> по аналогичным правилам, а затем снова изменит направление и будет резать вниз и так далее \dots</li>
	<li>Билл продолжает вырезать до тех пор, пока при смене направления не случится ситуация, при которой резать уже нечего</li>
</ul>

<p>Пример получившейся спирали показан на рисунке. Красным цветом обозначена линия разреза.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/267bcb50-4a77-47d4-8aea-ac2d53c61d7b/-/preview/" style="width: 150px; height: 113px;"></p>

<p>Джоржи не терпится, как можно быстрее поиграть с корабликом, поэтому ему очень важно знать суммарную длину разрезов, которые должен будет сделать Билл, чтобы понимать, когда тот закончит. Помогите Джоржи с подсчетом этой величины!</p>

### 입력 

 <p>В единственной строке даны два натуральных числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> --- размеры листка, из которого Билл будет вырезать спираль (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le n, m \le 10^9$</span></mjx-container>). </p>

### 출력 

 <p>Выведите одно число --- суммарную длину разрезов, которые должен будет сделать Билл для получения спирали.</p>

