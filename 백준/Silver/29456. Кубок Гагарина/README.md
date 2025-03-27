# [Silver IV] Кубок Гагарина - 29456 

[문제 링크](https://www.acmicpc.net/problem/29456) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

비트마스킹, 브루트포스 알고리즘, 수학, 확률론

### 제출 일자

2025년 3월 27일 09:10:25

### 문제 설명

<p>Хоккей с шайбой --- один из самых распространенных в России видов спорта. На днях закончился розыгрыш самого престижного в Европе хоккейного клубного турнира --- Кубка Гагарина.</p>

<p>На первом этапе плей-офф борьбу начинает 16 клубов, разбитые по парам. Далее команды, попавшие в одну пару играют между собой серию из семи матчей до четырех побед. Если одна из команд выигрывает четыре матча, то серия прекращается и она признается победителем. Далее остается восемь команд, которые играют второй раунд по тем же правилам, и так далее, вплоть до победителя.</p>

<p>Первые два матча серии проходят на площадке первой команды, следующие два на площадке второй команды, после этого следующие матчи (если они нужны) проходят поочередно сначала на площадке первой команды, потом второй, то есть по схеме 2-2-1-1-1.</p>

<p>Вам дана вероятность победы каждой из команд на каждой из площадок. Вам нужно определить вероятность, с которой серия завершится именно с данным счетом.</p>

### 입력 

 <p>Первая строка входного файла содержит вещественных два числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container> --- вероятность победы каждой из команд на площадке первой команды (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>≤</mo><mn>1</mn><mo>,</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le a, b \le 1, a + b = 1$</span></mjx-container>), вторая строка в аналогичном формате вероятность побед из команд на площадке второй команды. Третья строка содержит счет, вероятность которого Вам нужно определить.</p>

### 출력 

 <p>Выведите одно число --- ответ на задачу. Ответ должен отличаться от правильного не более, чем на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mo>−</mo><mn>6</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{-6}$</span></mjx-container>.</p>

