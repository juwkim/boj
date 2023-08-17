# [Bronze III] Звуки в подвале - 28722 

[문제 링크](https://www.acmicpc.net/problem/28722) 

### 성능 요약

메모리: 113112 KB, 시간: 128 ms

### 분류

게임 이론, 구현

### 문제 설명

<p>Билл и Ричи услышали странные звуки, доносящиеся из подвала, и теперь решают, кому из них придется пойти и проверить его. Они решили, что будет разумно сыграть в какую-нибудь игру, и отправить проигравшего.</p>

<p>Ребята выбрали игру, которая проходит по следующим правилам:</p>

<ul>
	<li>Изначально у ребят есть клетчатая полоска, каждая клетка которой покрашена в красный или синий цвет.</li>
	<li>На очередном ходу можно выбрать любую полоску, у которой цвета первой и последней клеток не совпадают, и произвольно разрезать ее на две полоски с целой положительной длиной.</li>
	<li>Мальчик, у которого не будет хода, проигрывает.</li>
</ul>

<p>Ребята уже выбрали полоску, и Билл будет ходить первым. Помогите Биллу определить, может ли он выиграть при оптимальной игре обоих ребят.</p>

### 입력 

 <p>В первой строке дана строка <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>, состоящая из символов <<<code>R</code>>> и <<<code>B</code>>>, описывающая выбранную ребятами полоску (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>s</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le |s| \le 100\,000$</span></mjx-container>). Символ <<<code>R</code>>> соответствует красной клетке, а <<<code>B</code>>>  --- синей.</p>

### 출력 

 <p>В единственной строке выведите <<<code>Win</code>>>, если Билл выиграет, и <<<code>Lose</code>>>, если Билл проиграет, при оптимальной игре обоих мальчиков.</p>

