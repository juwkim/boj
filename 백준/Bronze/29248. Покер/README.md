# [Bronze I] Покер - 29248 

[문제 링크](https://www.acmicpc.net/problem/29248) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

수학

### 제출 일자

2024년 12월 10일 20:03:51

### 문제 설명

<p>Локи --- очень коварный и хитрый бог. Но и у него бывают промашки: Тор догадался, кто остриг наголо его жену, и теперь требует от него компенсации. И Локи предложил ему такую сделку: в финале по асгардскому покеру он будет пасовать при каждой возможности, и таким образом Тор выиграет.</p>

<p>Каждый раунд в асгардском покере выкладывают на стол три карты, а затем после каждой фазы кладут на стол еще по одной карте. Всего фаз четыре. Перед каждым раундом игрок ставит либо малый блайнд, либо большой блайнд, который в два раза больше малого. После каждого раунда тип блайнда у игроков меняется на противоположный. Если денег у игрока меньше, чем размер блайнда, он ставит их все. После каждой фазы у игрока есть возможность удвоить ставку, если у него есть достаточное количество денег, либо отказаться дальше играть. Если какой-либо игрок спасовал, все деньги, которые были поставлены, переходят к другому игроку; игрок, который спасовал, теряет все свои поставленные деньги. В конце раунда игроки вскрывают карты. Рука составляется из любых пяти карт игрока и карт на столе. Игрок, чья рука сильнее, побеждает и забирает все деньги, которые были поставлены в этом раунде.</p>

<p>Локи очень скучно смотреть, как Тор выигрывает, поэтому ему очень хочется знать, сколько раундов всего будет в игре.</p>

### 입력 

 <p>В первой строке даны числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>x</mi><mo>,</mo><mi>b</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le x, b \le 10^9$</span></mjx-container>) --- количество денег у Локи перед началом игры и размер малого блайнда. Во второй строке находится буква <<<code>L</code>>> или <<<code>T</code>>>, если первый малый блайнд у Локи или Тора соответственно. Количество денег у Тора можно считать достаточным для любой ставки.</p>

### 출력 

 <p>В единственной строке выходного файла выведите количество раундов в этой игре.</p>

