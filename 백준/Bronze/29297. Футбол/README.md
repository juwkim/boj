# [Bronze III] Футбол - 29297 

[문제 링크](https://www.acmicpc.net/problem/29297) 

### 성능 요약

메모리: 114328 KB, 시간: 124 ms

### 분류

사칙연산, 구현, 수학, 문자열

### 문제 설명

<p>Хаус с Уилсоном, смотря финальный матч Кубка MLS по футболу между командами LAG и DCU, в очередной раз поспорили. Хаус говорил, что победит команда LAG, Уилсон же говорил, что команда DCU. Когда закончился первый матч финальной серии (а финальная серия состоит из двух матчей), Уилсон задумался какие исходы второго матча помогут Уилсону выиграть спор.</p>

<p>Напомним, что команда выигрывает в серии из двух матчей, если по сумме двух игр она забила больше мячей, чем команда соперника. Если же обе команды забили суммарно одинаковое количество голов, то победителем считается команда, которая забила больше мячей ну чужом поле. Если же в гостях они также забили одинаковое количество голов, то проводится два дополнительных таймa. В рамках данной задачи будем считать этот исход ничейным.</p>

<p>Известно, что первый матч играют на поле LAG, а второй --- на поле DCU. Кроме того, Уилсон преположил, что никакая команда не забьёт более девяти голов. Ваша задача --- помочь Уилсону посчитать, сколько существует исходов, при которых кубок выиграет команда LAG и сколько существует исходов, при которых кубок выиграет команда DCU. При этом вам будет дан результат первого матча.</p>

### 입력 

 <p>В первой строке дано целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 100$</span></mjx-container>) --- количество тестов. В следующих <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> строках дан результат в первом матче между командами в формате <code>a:b</code>, где <code>a</code> --- количесто голов забитое командой LAG и <code>b</code> ---количество голов забитое DCU.</p>

### 출력 

 <p>В каждой из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> строк вывести по два числа: количество исходов, при которых выиграет команда LAG и количество исходов, при которых выиграет команда DCU.              </p>

