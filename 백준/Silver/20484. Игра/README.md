# [Silver II] Игра - 20484 

[문제 링크](https://www.acmicpc.net/problem/20484) 

### 성능 요약

메모리: 109608 KB, 시간: 92 ms

### 분류

게임 이론, 구현

### 제출 일자

2025년 3월 11일 02:43:32

### 문제 설명

<p>На планете Шелезяка катастрофа --- запасы смазки подходят в концу. В связи с этим правительство решило организовать всепланетное соревнование, главный приз в котором --- вагон смазочных материалов.</p>

<p>Соревнование проводится в несколько этапов, каждый из которых поделен на множество раундов. В каждом раунде принимают участие два игрока. Жюри предоставляет им большое целое число~<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>. Затем игроки делают ходы по очереди. Первый ход первого игрока заключается в том, что игрок выписывает на специальном поле цифру, причем первым ходом запрещается выписывать ноль. В дальнейшем ход игрока заключается в том, что он приписывает справа к уже написанному числу произвольную цифру. Выигрывает тот, после чьего хода выписанное число больше или равно~<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>.</p>

<p>Знаменитый ученый-робот <<ЩК-33>> считает, что результат игры легко предсказуем. Для доказательства он решил предоставить программу, которая определяет, кто выигрывает, если оба игрока действуют по оптимальной стратегии. К сожалению, из-за недостатка смазки, его манипуляторы вышли из строя, поэтому он просит вас о помощи.</p>

### 입력 

 <p>Первая строка входного файла содержит целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle style="font-size: 141.4%;"><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 10^{100\,000}$</span></mjx-container>). Это число не содержит ведущих нулей.</p>

### 출력 

 <p>Выведите <<<code>First</code>>>, если при оптимальной игре выигрывает первый игрок, и <<<code>Second</code>>> в противном случае.</p>

